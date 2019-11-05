#!/bin/python
import os, re, pickle

import uproot
import numpy as np
np.random.seed(123)
import pandas as pd

from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, LabelEncoder
import sklearn.utils
import itertools,random
from  collections  import Counter

from HelperTools import *

def convertToPanda(setupClient):
    listFiles = os.listdir(setupClient.InputMLNtuplePath) # returns list

    for i in setupClient.InputROOTFiles:
        found = False
        print ('Looking for ',Fore.BLUE+i)
        for fileInDir in listFiles:
            if i in fileInDir and '.root' in fileInDir:
                flatNtuple = setupClient.InputMLNtuplePath+fileInDir
                if os.path.isfile(flatNtuple):
                    found = True
                    print ('{:>13}{:<20}'.format('==> Found ',Fore.GREEN+fileInDir))
                    theFile = uproot.open(flatNtuple)
                    theTree = theFile.keys()
                    print ('{:>20}{:<20}'.format('Available TTrees:',Fore.GREEN+str(theTree)))
                    tree = uproot.open(flatNtuple)[theTree[0]]
                    Nevents = uproot.open(flatNtuple)[theTree[0]].numentries
                    print ('Num entries',Nevents)
                    counter = 0
                    ###############
                    df_list = []
                    for chunk in tree.iterate(branches=setupClient.rootBranchSubSample,entrysteps=5000000,outputtype=pd.DataFrame):
                        # chunk.to_pickle(setupClient.PDPath+i+'_FullNoRandom'+str(counter)+'.pkl')

                        if (setupClient.PreselectionCuts !=''):
                            print('Applying preselection',setupClient.PreselectionCuts)
                            chunk = applyPreselection(chunk,setupClient.PreselectionCuts)
                        df_list += [ chunk ]
                            # chunk.to_pickle(setupClient.PDPath+i+'_FullNoRandom'+str(counter)+'.pkl')

                    df_full = pd.concat(df_list,ignore_index=True)
                    print ('Total Num entries after presel',df_full.shape[0])


                    X = Randomizing(df_full,False) # False means that a new column with the original event index will be generated and saved

                    fileInDir = re.sub('\.root$', '', fileInDir)
                    if 'data' in fileInDir:
                        print ('{:>20} {:<15}'.format('Data  events',Fore.GREEN+str(X.shape[0])+'\n'))
                        X.to_pickle(setupClient.PDPath+i+'.pkl')
                    else:
                        if 'VBF' in fileInDir                      : X['ggFVBF'] = 1 # antonio
                        if 'ggF' in fileInDir or 'DY' in fileInDir : X['ggFVBF'] = 0 # antonio

                        print ('{:>20} {:<15} {:<15}'.format('Number of events',Fore.GREEN+str(X.shape[0])," Splitting to..."))
                        Ntrain_stop = int(round(X.shape[0] * 0.7))
                        X_Train = X[:Ntrain_stop]
                        X_Test = X[Ntrain_stop:]
                        print ('{:>20} {:<15}'.format('Train events',Fore.GREEN+str(X_Train.shape[0])))
                        print ('{:>20} {:<15}'.format('Test events',Fore.GREEN+str(X_Test.shape[0])+'\n' ))

                        X_Test.to_pickle(setupClient.PDPath+i+'_Test.pkl')
                        del X_Test
                        X_Train.to_pickle(setupClient.PDPath+i+'_Train.pkl')
                        del X_Train

                        del X
                        del chunk
                        counter += 1
                else:
                    print ('{:<20}'.format(Fore.RED+'==> NOT Found!') )
        if found == False:
            print ('{:<20}'.format(Fore.RED+'==> NOT Found!'))


def applyPreselection(inPanda,cuts):
    inPanda =  eval(cuts)
    print ('{:<20} {:<15}'.format('Events after preselection:',Fore.BLUE+str(inPanda.shape[0])))
    return inPanda

def preparePandas(setupClient):
    df_sig_Train  = []
    df_bkg_Train  = []
    df_sig_Test   = []
    df_bkg_Test   = []
    df_data  = []

    doPreselection = setupClient.PreselectionCuts !=''

    #First get the train samples
    for ifile in setupClient.InputFilesSB['Data']:
        if ifile=='None' or ifile==[]:
            continue
        df_data_tmp = getDFEvents(setupClient.PDPath,ifile,'Data')
        if doPreselection:
            df_data_tmp = applyPreselection(df_data_tmp,setupClient.PreselectionCuts)
        df_data_tmp['Class'] = channelDic['Data']
        df_data += [ df_data_tmp ]
        print('')

    for ifile in setupClient.InputFilesSB['Signal']:
        if ifile=='None' or ifile==[]:
            continue
        df_sig_Train_tmp = getDFEvents(setupClient.PDPath,ifile,'_Train')
        df_sig_Test_tmp = getDFEvents(setupClient.PDPath,ifile,'_Test')

        if doPreselection:
            df_sig_Train_tmp = applyPreselection(df_sig_Train_tmp,setupClient.PreselectionCuts)
            df_sig_Test_tmp = applyPreselection(df_sig_Test_tmp,setupClient.PreselectionCuts)
        df_sig_Train_tmp['Class'] = channelDic['Signal']
        df_sig_Test_tmp['Class'] = channelDic['Signal']
        df_sig_Train += [ df_sig_Train_tmp ]
        df_sig_Test += [ df_sig_Test_tmp ]
        print('')

    #make all signal files have the same number of events.
    if setupClient.runMode == 'param' and setupClient.useEqualSizeSandB==True:
        finalListofDfs, totEvents, minEvents = makeEqualSizeDFs(df_sig_Train)
        df_sig_Train = finalListofDfs
        print('totEvents=',totEvents, 'minEvents=',minEvents)



    for ifile in setupClient.InputFilesSB['Background']:
        if ifile=='None' or ifile==[]:
            continue
        df_bkg_Train_tmp = getDFEvents(setupClient.PDPath,ifile,'_Train')
        df_bkg_Test_tmp = getDFEvents(setupClient.PDPath,ifile,'_Test')

        if doPreselection:
            df_bkg_Train_tmp = applyPreselection(df_bkg_Train_tmp,setupClient.PreselectionCuts)
            df_bkg_Test_tmp = applyPreselection(df_bkg_Test_tmp,setupClient.PreselectionCuts)
        classID = channelDic['Zjets']

        # if setupClient.runMode == 'multi':
        if 'Diboson' in ifile:
            classID = channelDic['Diboson']
        if 'Top' in ifile:
            classID = channelDic['Top']
        if 'VBF' in ifile:
            classID = channelDic['VBF']
        if 'ggF' in ifile:
            classID = channelDic['ggF']

        df_bkg_Train_tmp['Class'] = classID
        df_bkg_Test_tmp['Class'] = classID
        df_bkg_Train += [ df_bkg_Train_tmp ]
        df_bkg_Test += [ df_bkg_Test_tmp ]
        # print(ifile)
        print('')

    # Put all signal samples together and shuffle
    sigPD_Train = Randomizing(pd.concat(df_sig_Train,ignore_index=True))
    sigPD_Test = Randomizing(pd.concat(df_sig_Test,ignore_index=True))
    # Put all background samples together and shuffle
    bkgPD_Train = Randomizing(pd.concat(df_bkg_Train,ignore_index=True))
    bkgPD_Test = Randomizing(pd.concat(df_bkg_Test,ignore_index=True))
    # Put all data files together
    if df_data != []:
        dataPD = pd.concat(df_data,ignore_index=True)

    # If requested, make sure signal and background have the same N events
    if setupClient.useEqualSizeSandB:
        NtrainEventsMax = 0
        if sigPD_Train.shape[0] > bkgPD_Train.shape[0]:
            print ('{:<20}'.format(Fore.RED+'Signal Train events '+str(sigPD_Train.shape[0])+' are more that Background Train events '+str(bkgPD_Train.shape[0])))
            NtrainEventsMax = bkgPD_Train.shape[0]
        else:
            print ('{:<20}'.format(Fore.RED+'Background Train events '+str(bkgPD_Train.shape[0])+' are more that Signal Train events '+str(sigPD_Train.shape[0])))
            NtrainEventsMax = sigPD_Train.shape[0]

        print ('Going to use bkgPD_Train[:'+str(NtrainEventsMax)+']')
        print ('Going to use sigPD_Train[:'+str(NtrainEventsMax)+']')
        bkgPD_Train = bkgPD_Train[:int(NtrainEventsMax)]
        sigPD_Train = sigPD_Train[:int(NtrainEventsMax)]

    print ('{:<45} {:<15}'.format('Total signal events',Fore.BLUE+str(sigPD_Train.shape[0]+sigPD_Test.shape[0])))
    print ('{:<45} {:<15}'.format('Total signal events in Train Sample',Fore.BLUE+str(sigPD_Train.shape[0])))
    print ('{:<45} {:<15}'.format('Total signal events in Test Sample',Fore.BLUE+str(sigPD_Test.shape[0])))
    print ('{:<45} {:<15}'.format('Total backgr events',Fore.BLUE+str(bkgPD_Train.shape[0]+bkgPD_Test.shape[0])))
    print ('{:<45} {:<15}'.format('Total backgr events in Train Sample',Fore.BLUE+str(bkgPD_Train.shape[0])))
    print ('{:<45} {:<15}'.format('Total backgr events in Test Sample',Fore.BLUE+str(bkgPD_Test.shape[0])))
    if df_data != []:
        print ('{:<45} {:<15}'.format('Total data events  ',Fore.BLUE+str(dataPD.shape[0])))



    ################# Copy random signal truth mass to background truth mass ###################
    truthMassVarName = 'truth_zv_mass'
    if setupClient.runMode == 'param':
        cls_ytrain_count = Counter(sigPD_Train[truthMassVarName])
        Nclass = len(cls_ytrain_count)
        massPoints = list(cls_ytrain_count.keys())
        print ('{:<45} {:<15}'.format('Number of mass points in signal DF',Fore.BLUE+str(Nclass)))
        print (massPoints)

        tmassToCopy = []
        for _ in itertools.repeat(None, bkgPD_Train.shape[0]):
            tmassToCopy += [random.choice(massPoints)]
        bkgPD_Train.loc[:,truthMassVarName] = tmassToCopy

        tmassToCopy = []
        for _ in itertools.repeat(None, bkgPD_Test.shape[0]):
            tmassToCopy += [random.choice(massPoints)]
        bkgPD_Test.loc[:,truthMassVarName] = tmassToCopy
    ################# END ###################

    # Put S+B together
    df_All_Train = [ bkgPD_Train,sigPD_Train ]
    df_All_Test = [ bkgPD_Test,sigPD_Test ]

    df_MixSB_Train = Randomizing(pd.concat(df_All_Train,ignore_index=True))
    df_MixSB_Test = Randomizing(pd.concat(df_All_Test,ignore_index=True))

    print ('')
    print ('{:<45} {:<15}'.format('Total Train events',Fore.MAGENTA+str(df_MixSB_Train.shape[0])))
    print ('{:<45} {:<15}'.format('Total Test events',Fore.MAGENTA+str(df_MixSB_Test.shape[0])))

    df_MixSB_Train.to_pickle(setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Train.pkl')
    df_MixSB_Test.to_pickle(setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Test.pkl')
    if df_data  != []:
        dataPD.to_pickle(setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Data.pkl')
    print(df_MixSB_Train[:20])
    print(df_MixSB_Test[:20])


def LoadData(setupClient):
    print (Fore.BLUE+"--------------------------")
    print (Back.BLUE+"   LOAD TRAIN/TEST DATA   ")
    print (Fore.BLUE+"--------------------------")
    pdtoLoad_Train = setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Train.pkl'
    pdtoLoad_Test = setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Test.pkl'

    print ('{:<45}{:<25}'.format("Train sample",Fore.GREEN+pdtoLoad_Train) )
    print ('{:<45}{:<25}'.format("Test sample", Fore.GREEN+pdtoLoad_Test) )
    if not os.path.isfile(pdtoLoad_Train):
        print ("PD file",pdtoLoad_Train," not found!")
        quit()
    if not os.path.isfile(pdtoLoad_Test):
        print ("PD file",pdtoLoad_Test," not found!")
        quit()

    df_Train = pd.read_pickle(pdtoLoad_Train)
    df_Test = pd.read_pickle(pdtoLoad_Test)

    ## convert PD to numpy and normalize variables
    ## This is where the set of input variables is selected
    # diboson_Test = pd.read_pickle(setupClient.PDPath+'Diboson_Test.pkl')
    # print(diboson_Test[:20])
    # print(df_Test[:20])

    VariablesSet =  setupClient.InputDNNVariables[setupClient.VarSet]
    print('{:<45}{:<25}'.format("Variable set",Fore.GREEN+str(setupClient.VarSet)+' '+str(VariablesSet)) )
    truthMassVarName = 'truth_zv_mass'
    if setupClient.runMode == 'param':
        if truthMassVarName not in VariablesSet:
            print ('Running on Parametrized Network and you have forgotten to add truth_zv_mass in the list of input variables for the training!')
            quit()


    # print(df_Test[VariablesSet][:20])
    X_Train=df_Train[VariablesSet].as_matrix()
    X_Test=df_Test[VariablesSet].as_matrix()


    if setupClient.Train:
        scaler = preprocessing.StandardScaler().fit(X_Train)
        setupClient.Scaler = scaler
        X_Train = scaler.transform(X_Train)
        X_Test = scaler.transform(X_Test)
    elif setupClient.LoadTrainedModel:
        modelpath = setupClient.TrainedModelPath
        print ('{:<45} {:<15}'.format('Getting Scaler of Training sample from file',Fore.GREEN+modelpath+'DNN_Setup' ) )
        if not os.path.isfile(modelpath+'/DNN_Setup'):
            print ("Pickle file not found!")
            quit()
        f = open(modelpath+'/DNN_Setup', "rb")
        savedSetupClient = pickle.load(f)
        X_Train = savedSetupClient.Scaler.transform(X_Train)
        X_Test = savedSetupClient.Scaler.transform(X_Test)


    ## The truth is out...here!
    le = LabelEncoder()
    if setupClient.runMode == 'multi':
        y_Train = le.fit_transform(df_Train['Class'])
        y_Test  = le.fit_transform(df_Test['Class'])
    else:
        y_Train = le.fit_transform(df_Train['isSignal'])
        y_Test  = le.fit_transform(df_Test['isSignal'])


    w_Train=df_Train['weight'].as_matrix() # WEIGHT: All weights except xsection norm. weight: All weights
    w_Test=df_Test['weight'].as_matrix() # WEIGHT: All weights except xsection norm. weight: All weights

    ix_Train = df_Train
    ix_Test = df_Test

    return (X_Train, y_Train), (X_Test, y_Test), (w_Train, w_Test), (ix_Train, ix_Test)


def create_stream(df, num_obj, sort_col):

    n_variables = df.shape[1]
    var_names = df.keys()

    data = np.zeros((df.shape[0], num_obj, n_variables), dtype='float32')

    # -- call functions to build X (a.k.a. data)
    sort_objects(df, data, sort_col, num_obj)

    # -- ix_{train, test} from above or from previously stored ordering
    Xobj_train = data[ix_train]
    Xobj_test = data[ix_test]

    #print 'Scaling features ...'
    scale(Xobj_train, var_names, savevars=True) # scale training sample and save scaling
    scale(Xobj_test, var_names, savevars=False) # apply scaling to test set
    return Xobj_train, Xobj_test

def LoadDataRNN(setupClient):
    print (Fore.BLUE+"---------------------------------")
    print (Back.BLUE+"   LOAD TRAIN/TEST DATA for RNN  ")
    print (Fore.BLUE+"---------------------------------")
    pdtoLoad_Train = setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Train.pkl'
    pdtoLoad_Test = setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Test.pkl'

    print ('{:<45}{:<25}'.format("Train sample",Fore.GREEN+pdtoLoad_Train) )
    print ('{:<45}{:<25}'.format("Test sample", Fore.GREEN+pdtoLoad_Test) )
    if not os.path.isfile(pdtoLoad_Train):
        print ("PD file",pdtoLoad_Train," not found!")
        quit()
    if not os.path.isfile(pdtoLoad_Test):
        print ("PD file",pdtoLoad_Test," not found!")
        quit()

    df_Train_full = pd.read_pickle(pdtoLoad_Train)
    df_Test_full = pd.read_pickle(pdtoLoad_Test)

    VariablesSet =  setupClient.InputDNNVariables[setupClient.VarSet]

    Xjet_train = df_Train_full[VariablesSet].copy()
    Xjet_test = df_Test_full[VariablesSet].copy()

    #print 'Scaling features ...'
    var_names = Xjet_train.keys()
    new_Xjet_train = np.zeros( (Xjet_train.shape[0], 6, 4) )
    new_Xjet_test = np.zeros( (Xjet_test.shape[0], 6, 4) )

    for i in range(0, Xjet_train.shape[0]):
        for j in range(0, Xjet_train.shape[1]):
            new_Xjet_train[i, int(j/4), j%4] = Xjet_train.iloc[i, j]
    Xjet_train = new_Xjet_train

    for i in range(0, Xjet_test.shape[0]):
        for j in range(0, Xjet_test.shape[1]):
            new_Xjet_test[i, int(j/4), j%4] = Xjet_test.iloc[i, j]
    Xjet_test = new_Xjet_test

    # print(Xjet_train)
    scale(Xjet_train, ['pt','eta','phi','E'], True, setupClient) # scale training sample and save scaling
    scale(Xjet_test,  ['pt','eta','phi','E'], False, setupClient) # apply scaling to test set

    le = LabelEncoder()
    y_Train = le.fit_transform(df_Train_full['ggFVBF'])
    y_Test  = le.fit_transform(df_Test_full['ggFVBF'])

    w_Train=df_Train_full['weight'].as_matrix() # WEIGHT: All weights except xsection norm. weight: All weights
    w_Test=df_Test_full['weight'].as_matrix() # WEIGHT: All weights except xsection norm. weight: All weights

    ix_Train = df_Train_full
    ix_Test = df_Test_full

    return (Xjet_train, y_Train), (Xjet_test, y_Test), (w_Train, w_Test), (ix_Train, ix_Test)


def scale(data, var_names, savevars, setupClient, VAR_FILE_NAME='scaling'):
    '''
    Args:
    -----
        data: a numpy array of shape (nb_events, nb_particles, n_variables)
        var_names: list of keys to be used for the model
        savevars: bool -- True for training, False for testing
                  it decides whether we want to fit on data to find mean and std
                  or if we want to use those stored in the json file

    Returns:
    --------
        modifies data in place, writes out scaling dictionary
    '''
    # import json
    modelpath = setupClient.ModelSavePath

    scale = {}
    if savevars:
        for v, name in enumerate(var_names):
            print ('Scaling feature %s of %s (%s).' % (v + 1, len(var_names), name))
            f = data[:, :, v]
            # print(f)
            slc = f[f != setupClient.MaskValue]
            m, s = slc.mean(), slc.std()
            slc -= m
            slc /= s
            data[:, :, v][f != setupClient.MaskValue] = slc.astype('float32')
            scale[name] = {'mean' : float(m), 'sd' : float(s)}

        with open(modelpath+'/'+VAR_FILE_NAME, 'wb') as varfile:
            pickle.dump(scale, varfile)
            varfile.close()

    else:
        f = open(modelpath+'/'+VAR_FILE_NAME, "rb")
        varinfo = pickle.load(f)

        for v, name in enumerate(var_names):
            #print 'Scaling feature %s of %s (%s).' % (v + 1, len(var_names), name)
            f = data[:, :, v]
            slc = f[f != setupClient.MaskValue]
            m = varinfo[name]['mean']
            s = varinfo[name]['sd']
            slc -= m
            slc /= s
            data[:, :, v][f != setupClient.MaskValue] = slc.astype('float32')
