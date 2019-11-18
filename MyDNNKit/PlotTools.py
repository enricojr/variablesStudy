import sys,os,glob,time,string,math,pickle,itertools,random

from keras.models import load_model
from keras.utils import plot_model

from sklearn.metrics import roc_curve, auc, roc_auc_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
np.random.seed(123)

import scipy.interpolate as interpolate
import scipy.optimize as optimize

from skhep.visual import MplPlotter as skh_plt
from skhep.math import vectors as skh_vec

import PrepareData
from HelperTools import *


def plotDFs(setupClient):
    pdtoLoad_train = setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Train.pkl'
    pdtoLoad_test = setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Test.pkl'
    print ("Loading train data from pkl file at", pdtoLoad_train)
    print ("Loading test data from pkl file at", pdtoLoad_test)
    if not os.path.isfile(pdtoLoad_train):
        print ("Loading pkl file", pdtoLoad_train, "not found")
        quit()
    if not os.path.isfile(pdtoLoad_test):
        print ("Loading pkl file", pdtoLoad_test, "not found")
        quit()
    df_train = pd.read_pickle(pdtoLoad_train)
    df_test = pd.read_pickle(pdtoLoad_test)
    df = pd.concat([df_train,df_test])

    for var in setupClient.VariablesToPlot:
        print ("Plotting variable",var)
        denom_norm = 1
        bins=np.linspace(min(df[var]), max(df[var]) + 1, 100)
        if 'NJETS' in var:
            bins=np.linspace(0, 15, 15)

        x_unit = " [GeV]"
        x_title = var
        if "_pt" in var or "_E" in var or "MET" in var or "Zll_mass" in var:
            # denom_norm = 1000
            bins = np.linspace(0, 2000, 40)
        elif "_zv_mass" in var:
            # denom_norm = 1000
            bins = np.linspace(500, 2500, 100)
        elif "_eta" in var or "_phi" in var:
            bins = np.linspace(-4, 4, 40)
            x_unit=""
        elif "_C2" in var:
            bins = np.linspace(0, 1, 100)
            x_unit=""
        elif "_D2" in var:
            bins = np.linspace(0, 5, 100)
            x_unit=""
        elif "isSignal" in var:
            bins = np.linspace(0, 2, 10)
            x_unit=""
        elif "Topology" in var or "FullEventWeight" in var or "_charge" in var:
            continue

        df_sig = df[df['Class']==1]
        df_bkg = df[df['Class']!=1]
        _ = plt.hist(df_sig[var]/denom_norm, histtype='stepfilled', bins=bins, alpha=0.5, normed=True, label='Signal', linewidth=1)
        _ = plt.hist(df_bkg[var]/denom_norm, histtype='stepfilled', bins=bins, alpha=0.5, normed=True, label='Background', linewidth=1)

        plt.xlabel(x_title+x_unit,fontsize=14)
        plt.ylabel('Norm.Entries',fontsize=14)
        plt.yscale('log')
        plt.legend(loc='best',prop={'size': 10})
        # plt.show()
        plt.savefig(setupClient.VarPlotPath+"/"+var+"_"+setupClient.MixPD_TrainTestTag+".png")
        plt.clf()


        df_sig_train = df_train[df_train['Class']==1]
        df_sig_test = df_test[df_test['Class']==1]
        df_bkg_train = df_train[df_train['Class']!=1]
        df_bkg_test = df_test[df_test['Class']!=1]
        _ = plt.hist(df_sig_train[var]/denom_norm, histtype='stepfilled', bins=bins, alpha=0.5, normed=True, label='Signal (train)', linewidth=1)
        _ = plt.hist(df_bkg_train[var]/denom_norm, histtype='stepfilled', bins=bins, alpha=0.5, normed=True, label='Background (train)', linewidth=1)

        plt.xlabel(x_title+x_unit,fontsize=14)
        plt.ylabel('Norm.Entries',fontsize=14)
        plt.yscale('log')
        plt.legend(loc='best',prop={'size': 10})
        # plt.show()
        plt.savefig(setupClient.VarPlotPath+"/"+var+"_"+setupClient.MixPD_TrainTestTag+"_train.png")
        plt.clf()

        _ = plt.hist(df_sig_test[var]/denom_norm, histtype='stepfilled', bins=bins, alpha=0.5, normed=True, label='Signal (test)', linewidth=1)
        _ = plt.hist(df_bkg_test[var]/denom_norm, histtype='stepfilled', bins=bins, alpha=0.5, normed=True, label='Background (test)', linewidth=1)

        plt.xlabel(x_title+x_unit,fontsize=14)
        plt.ylabel('Norm.Entries',fontsize=14)
        plt.yscale('log')
        plt.legend(loc='best',prop={'size': 10})
        # plt.show()
        plt.savefig(setupClient.VarPlotPath+"/"+var+"_"+setupClient.MixPD_TrainTestTag+"_test.png")
        plt.clf()




def plotDataMC(setupClient):

    topDF_list = []
    zjetsDF_list = []
    wjetsDF_list = []
    dibosonDF_list = []
    signalDF_list = []

    for itype in setupClient.InputFilesSB.keys():
        for ifile in setupClient.InputFilesSB[itype]:
            print(ifile)
            if 'Top' in ifile:
                topDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Train')]
                topDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Test')]
            if 'Data' in ifile:
                dataDF = getDFEvents(setupClient.PDPath,ifile,'Data')
            if 'Zjets' in ifile:
                zjetsDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Train')]
                zjetsDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Test')]
            if 'Diboson' in ifile:
                dibosonDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Train')]
                dibosonDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Test')]
            if 'ggF' in ifile:
                signalDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Train')]
                signalDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Test')]
            if 'Wjets' in ifile:
                wjetsDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Train')]
                wjetsDF_list += [getDFEvents(setupClient.PDPath,ifile,'_Test')]

    topDF = pd.concat(topDF_list,ignore_index=True)
    zjetsDF = pd.concat(zjetsDF_list,ignore_index=True)
    wjetsDF = pd.concat(wjetsDF_list,ignore_index=True)
    dibosonDF = pd.concat(dibosonDF_list,ignore_index=True)
    signalDF = pd.concat(signalDF_list,ignore_index=True)


    for var in setupClient.VariablesToPlot:
        print ("Plotting variable",var)
        # print ' min:',min(dibosonDF[var]), ' max', max(dibosonDF[var])
        bins=np.linspace(min(dibosonDF[var]), max(dibosonDF[var]), 20)

        plt.hist(
            [topDF[var],dibosonDF[var],zjetsDF[var],wjetsDF[var]],
             histtype='stepfilled',
             normed=False,
             bins=bins,
             weights=[ topDF['weight'],dibosonDF['weight'],zjetsDF['weight'],wjetsDF['weight'] ],
             label=[ 'Top', 'Diboson','Z + jets','W + jets', ],
             stacked=True)


        plt.hist(signalDF[var], histtype='step', normed=False, bins=bins, weights=signalDF['weight'], label=r'ggF', linewidth=1, color='red', linestyle='dashed')
        # plt.hist(dataDF[var], histtype='step', normed=False, bins=bins, label=r'Data', linewidth=2, color='black', linestyle='dashed')
        _ = skh_plt.hist(dataDF[var], bins=bins, errorbars=True, histtype='marker',label='Data', color='black')


        plt.legend(loc='best',prop={'size': 10})
        plt.xlabel(var,fontsize=14)
        plt.savefig(setupClient.VarPlotPath+"/"+var+"_DataMC.png")
        plt.yscale('log')
        plt.savefig(setupClient.VarPlotPath+"/"+var+"_DataMC_log.png")
        plt.clf()
        ##############

        # fig, (ax1, ax2) = plt.subplots(nrows=2)
        #
        # stackHist = skh_plt.hist(
        #     [topDF[var],dibosonDF[var],zjetsDF[var]],
        #      histtype='stepfilled',
        #      normed=False,
        #      bins=bins,
        #      weights=[ topDF['weight'],dibosonDF['weight'],zjetsDF['weight'] ],
        #      label=[ 'Top', 'Z + jets', 'Diboson' ],
        #      stacked=True,
        #      err_type='sumW2',
        #      err_return = True,
        #      errorbars=True,
        #      err_style = 'band',
        #      ax=ax1
        #      )
        #
        # sigHist = skh_plt.hist(signalDF[var], histtype='step', normed=False, bins=bins, weights=signalDF['weight'], label=r'ggF1000', linewidth=1, color='red', linestyle='dashed',err_type='sumW2',
        # err_return = True, ax=ax1,errorbars=True)
        # dataHist = skh_plt.hist(dataDF[var], bins=bins, errorbars=True, histtype='marker',label='Data', color='black',ax=ax1)
        #
        # ax1.legend(loc='best',prop={'size': 10})
        # # plt.xlabel(var,fontsize=14)
        # plt.savefig(setupClient.VarPlotPath+"/"+var+"_DataMC_TEST.png")


def plot_confusion_matrix(setupClient,cm, classes,normalize=False,title='Confusion matrix',cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        # print("Normalized confusion matrix")
    # else:
        # print('Confusion matrix, without normalization')

    # print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes)
    plt.yticks(tick_marks, classes, rotation=90)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    # plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig(setupClient.ModelSavePath+"/ConfusionMatrix.png")
    plt.clf()



def plotTrainPerformance(setupClient,modelMetricsHistory):

    plt.plot(modelMetricsHistory.history['acc'])
    plt.plot(modelMetricsHistory.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='lower right')
    plt.savefig(setupClient.ModelSavePath+"/Accuracy.png")
    plt.clf()

    # summarize history for loss
    plt.plot(modelMetricsHistory.history['loss'])
    plt.plot(modelMetricsHistory.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Val'], loc='upper right')
    plt.savefig(setupClient.ModelSavePath+"/Loss.png")
    plt.clf()


def applyPreselection(inPanda,cuts):
    inPanda =  eval(cuts)
    print ('{:<20} {:<15}'.format('Events after preselection:',Fore.BLUE+str(inPanda.shape[0])))
    return inPanda



def TestParamModelOnTestSamples(setupClient,model):
    print (Fore.BLUE+"---------------------------------")
    print (Back.BLUE+" Test pDNN Model on TEST Samples ")
    print (Fore.BLUE+"---------------------------------")

    VariablesSet =  setupClient.InputDNNVariables[setupClient.VarSet]
    modelpath = setupClient.TrainedModelPath
    print ('{:<45} {:<15}'.format('Getting Scaler of Training sample from file',Fore.GREEN+modelpath+'DNN_Setup' ) )
    if not os.path.isfile(modelpath+'/DNN_Setup'):
        print ("Pickle file not found!")
        quit()
    f = open(modelpath+'/DNN_Setup', "rb")
    savedSetupClient = pickle.load(f)

    # Load the samples
    for ifile in setupClient.InputFilesSB['Data']:
        if ifile=='None' or ifile==[]:
            continue
        print ("Variables",VariablesSet)
        print ('Opening DATAAAAA file',setupClient.PDPath+ifile)
        df_data_full = getDFEvents(setupClient.PDPath,ifile,'data')
        if setupClient.PreselectionCuts !='':
            df_data_full = applyPreselection(df_data_full,setupClient.PreselectionCuts)


        df_data = df_data_full[VariablesSet]
        print (df_data['truth_zv_mass'][:3])
        print('Mass Points to Test',setupClient.massPoint)
        massPoints = eval(setupClient.massPoint)
        for mass in massPoints:
            print('Fixing truth mass to',mass)
            df_data.loc[:,'truth_zv_mass'] = mass
            df_data_full.loc[:,'truth_zv_mass'] = mass
            print ('Opening DATA file after adding the truth_mass')
            print (df_data['truth_zv_mass'][:3])
            print (df_data_full['truth_zv_mass'][:3])

            X = df_data.as_matrix()
            X = savedSetupClient.Scaler.transform(X)
            yResult  = model.predict(X,verbose = True,batch_size=setupClient.Params['BatchSize'])
            df_data_full['DNN_Score'] = yResult
            df_data_full.to_pickle(setupClient.ModelSavePath+'/ResultspDNN_'+ifile+'_m'+str(mass)+'.pkl',protocol=2)
            del X



    for ifile in setupClient.InputFilesSB['Signal']:
        if ifile=='None' or ifile==[]:
            continue
        df_sig_full = getDFEvents(setupClient.PDPath,ifile,'_Test')
        if setupClient.PreselectionCuts !='':
            df_sig_full = applyPreselection(df_sig_full,setupClient.PreselectionCuts)
        df_sig = df_sig_full[VariablesSet]

        ## check truth mass
        print ('Opening signal file',ifile)
        print (df_sig['truth_zv_mass'][:3])
        print (df_sig_full['truth_zv_mass'][:3])

        X = df_sig.as_matrix()
        X = savedSetupClient.Scaler.transform(X)
        yResult  = model.predict(X,verbose = True,batch_size=setupClient.Params['BatchSize'])
        df_sig_full['DNN_Score'] = yResult
        df_sig_full.to_pickle(setupClient.ModelSavePath+'/ResultspDNN_'+ifile+'.pkl',protocol=2)
        del X
        del df_sig_full
        del df_sig


    for ifile in setupClient.InputFilesSB['Background']:
        if ifile=='None' or ifile==[]:
            continue
        df_bkg_full = getDFEvents(setupClient.PDPath,ifile,'_Test')
        if setupClient.PreselectionCuts !='':
            df_bkg_full = applyPreselection(df_bkg_full,setupClient.PreselectionCuts)
        df_bkg = df_bkg_full[VariablesSet]

        print ('Opening background file',ifile)
        print (df_bkg['truth_zv_mass'][:3])

        massPoints = eval(setupClient.massPoint)
        for mass in massPoints:
            print('Fixing truth mass to',mass)
            df_bkg.loc[:,'truth_zv_mass'] = mass
            df_bkg_full.loc[:,'truth_zv_mass'] = mass
            print ('Opening '+ifile+' file after adding the truth_mass')
            print (df_bkg['truth_zv_mass'][:3])
            print (df_bkg_full['truth_zv_mass'][:3])

            X = df_bkg.as_matrix()
            X = savedSetupClient.Scaler.transform(X)
            yResult  = model.predict(X,verbose = True,batch_size=setupClient.Params['BatchSize'])
            df_bkg_full['DNN_Score'] = yResult
            df_bkg_full.to_pickle(setupClient.ModelSavePath+'/ResultspDNN_'+ifile+'_m'+str(mass)+'.pkl',protocol=2)
            del X




def TestParamModelOnFullSamples(setupClient,model):
    print (Fore.BLUE+"---------------------------------")
    print (Back.BLUE+" Test pDNN Model on Full Samples ")
    print (Fore.BLUE+"---------------------------------")

    VariablesSet =  setupClient.InputDNNVariables[setupClient.VarSet]
    modelpath = setupClient.TrainedModelPath
    print ('{:<45} {:<15}'.format('Getting Scaler of Training sample from file',Fore.GREEN+modelpath+'DNN_Setup' ) )
    if not os.path.isfile(modelpath+'/DNN_Setup'):
        print ("Pickle file not found!")
        quit()
    f = open(modelpath+'/DNN_Setup', "rb")
    savedSetupClient = pickle.load(f)

    doPreselection = False
    if setupClient.PreselectionCuts != "":
        doPreselection = True

    # Load the samples
    for ifile in setupClient.InputFilesSB['Data']:
        if ifile=='None' or ifile==[]:
            continue
        print ("Variables",VariablesSet)
        print ('Opening DATA file',setupClient.PDPath+ifile+'_FullNoRandom')
        df_data_full = getDFEvents(setupClient.PDPath,ifile,'_FullNoRandom')

        if doPreselection:
            df_data_full = applyPreselection(df_data_full,setupClient.PreselectionCuts)


        df_data = df_data_full[VariablesSet]
        print (df_data['truth_zv_mass'][:3])
        print('Mass Points to Test',setupClient.massPoint)
        massPoints = eval(setupClient.massPoint)
        for mass in massPoints:
            print('Fixing truth mass to',mass)
            df_data.loc[:,'truth_zv_mass'] = mass
            df_data_full.loc[:,'truth_zv_mass'] = mass
            print ('Opening DATA file after adding the truth_mass')
            print (df_data['truth_zv_mass'][:3])
            # print (df_data_full['truth_zv_mass'][:3])

            X = df_data.as_matrix()
            X = savedSetupClient.Scaler.transform(X)
            yResult  = model.predict(X,verbose = True,batch_size=setupClient.Params['BatchSize'])
            df_data_full['DNN_Score'] = yResult

            # df_data_full.to_pickle(setupClient.ModelSavePath+'/ResultspDNN_'+ifile+'_m'+str(mass)+'.pkl')

            del X



    for ifile in setupClient.InputFilesSB['Signal']:
        if ifile=='None' or ifile==[]:
            continue
        df_sig_full = getDFEvents(setupClient.PDPath,ifile,'_FullNoRandom')
        if doPreselection:
            df_sig_full = applyPreselection(df_sig_full,setupClient.PreselectionCuts)
        df_sig = df_sig_full[VariablesSet]

        ## check truth mass
        print ('Opening signal file',ifile)
        print (df_sig['truth_zv_mass'][:3])
        print (df_sig_full['truth_zv_mass'][:3])

        X = df_sig.as_matrix()
        X = savedSetupClient.Scaler.transform(X)
        yResult  = model.predict(X,verbose = True,batch_size=setupClient.Params['BatchSize'])
        df_sig_full['DNN_Score'] = yResult
        # df_sig_full.to_pickle(setupClient.ModelSavePath+'/ResultspDNN_'+ifile+'.pkl',protocol=2)
        del X
        del df_sig_full
        del df_sig


    for ifile in setupClient.InputFilesSB['Background']:
        if ifile=='None' or ifile==[]:
            continue
        df_bkg_full = getDFEvents(setupClient.PDPath,ifile,'_FullNoRandom')
        if doPreselection:
            df_bkg_full = applyPreselection(df_bkg_full,setupClient.PreselectionCuts)

        df_bkg = df_bkg_full[VariablesSet]

        print ('Opening background file',ifile)
        print (df_bkg['truth_zv_mass'][:3])

        massPoints = eval(setupClient.massPoint)
        for mass in massPoints:
            print('Fixing truth mass to',mass)
            df_bkg.loc[:,'truth_zv_mass'] = mass
            df_bkg_full.loc[:,'truth_zv_mass'] = mass
            print ('Opening '+ifile+' file after adding the truth_mass')
            # print (df_bkg['truth_zv_mass'][:3])
            print (df_bkg_full['truth_zv_mass'][:3])

            X = df_bkg.as_matrix()
            X = savedSetupClient.Scaler.transform(X)
            yResult  = model.predict(X,verbose = True,batch_size=setupClient.Params['BatchSize'])
            df_bkg_full['DNN_Score'] = yResult
            # df_bkg_full.to_pickle(setupClient.ModelSavePath+'/ResultspDNN_'+ifile+'_m'+str(mass)+'.pkl',protocol=2)
            del X


def PlotResults(setupClient,model,X_train,X_test,y_train,y_test,w_train,w_test,ix_train, ix_test):

    print (Fore.BLUE+"--------------------------")
    print (Back.BLUE+"         RESULTS          ")
    print (Fore.BLUE+"--------------------------")

    if setupClient.runMode=='binary' or setupClient.runMode == 'param' or setupClient.runMode == 'SimpleRNN':
        print ('Evaluating model on X_test, y_test')
        score = model.evaluate(X_test, y_test, batch_size=setupClient.Params['BatchSize'])
        # testLoss = 'Test loss:%0.3f' % score[0]
        # testAccuracy = 'Test accuracy:%0.3f' % score[1]
        print ('{:<35} {:<25.3f}'.format(Fore.GREEN+'Test loss',score[0]))
        print ('{:<35} {:<25.3f}'.format(Fore.GREEN+'Test accuracy',score[1]))

    # get the architecture as a json string
    arch = model.to_json()
    with open(os.path.join(setupClient.ModelSavePath,'architecture.json'), 'w') as arch_file:
        print('Saving model as json',os.path.join(setupClient.ModelSavePath,'architecture.json'))
        arch_file.write(arch)
    # now save the weights as an HDF5 file
    model.save_weights(os.path.join(setupClient.ModelSavePath, 'ModelWeights.h5'), overwrite=True)

    if not os.path.isfile(setupClient.TrainedModelPath+'/DNN_Setup'):
        print ("Pickle file not found!")
        quit()
    foo = open(setupClient.TrainedModelPath+'DNN_Setup', "rb")
    bla = pickle.load(foo)
    minusMean = np.multiply(-1,bla.Scaler.mean_)
    OneOverStd = np.divide(1,np.sqrt(bla.Scaler.var_))


    with open(os.path.join(setupClient.ModelSavePath,'Scaling.txt'), 'w') as scaleFileOut:
        scaleFileOut.write(str(setupClient.InputDNNVariables[setupClient.VarSet])+'\n' )
        scaleFileOut.write('Mean\n'+str(bla.Scaler.mean_)+'\n')
        scaleFileOut.write('minusMean\n'+str(minusMean)+'\n')
        scaleFileOut.write('Var\n'+str(bla.Scaler.var_)+'\n')
        scaleFileOut.write('sqrtVar\n'+str(np.sqrt(bla.Scaler.var_))+'\n')
        scaleFileOut.write('OneOverStd\n'+str(OneOverStd)+'\n')


    theClasses = []
    print ('\nRunning model prediction on X train/test samples')
    yResult_test_cls = []
    yResult_train_cls = []

    yResult_test  = model.predict(X_test,verbose = True,batch_size=setupClient.Params['BatchSize'])
    yResult_train = model.predict(X_train,verbose = True,batch_size=setupClient.Params['BatchSize'])

    #insert the score result back into the original file
    # ix_test['DNN_Score'] = yResult_test
    # ix_train['DNN_Score'] = yResult_train

    # ix_test.to_pickle(setupClient.ModelSavePath+'/ResultsTestPD.pkl',protocol=2)
    # ix_train.to_pickle(setupClient.ModelSavePath+'/ResultsTrainPD.pkl',protocol=2)

    # np.save( os.path.join(setupClient.ModelSavePath, "ResultsTestPD.npy") , ix_test ) # antonio
    # np.save( os.path.join(setupClient.ModelSavePath, "ResultsTrainPD.npy") , ix_train ) # antonio
    # np.save( os.path.join(setupClient.ModelSavePath, "rootBranchSubSample.npy") , ix_test.columns.values) # antonio


    if setupClient.runMode == 'multi':
        yResult_test_cls  = np.argmax(yResult_test, axis=1) #stores the element with max score
        yResult_train_cls = np.argmax(yResult_train, axis=1) #stores the element with max score
        theClasses = ['Zjets','Signal','Diboson','Top']
    else:
        yResult_test_cls  = np.array([ int(round(x[0])) for x in yResult_test])
        yResult_train_cls = np.array([ int(round(x[0])) for x in yResult_train])
        theClasses = ['Background','Signal']

    # print(X_test[:20])
    # print ('')
    #
    # print(ix_test[:20])
    # print ('')
    # print(yResult_test)
    # quit()
    #
    # print(yResult_test_cls)
    # print ('')
    # print(yResult_train)
    # print ('')
    # print(yResult_train_cls)


    if setupClient.doConfusionMatrix:
        # Plot the confusion matrix
        plt.clf()
        # The class method is:  sklearn.metrics.confusion_matrix(y_true, y_pred, labels=None, sample_weight=None)
        cnf_matrix = confusion_matrix(y_test, yResult_test_cls, sample_weight=w_test)
        np.set_printoptions(precision=2)
        plot_confusion_matrix(setupClient,cnf_matrix, classes=theClasses,normalize=True, title='Normalized confusion matrix')

    if setupClient.doEfficiency:
        print ('Calculating Efficiencies on Test sample')
        if setupClient.runMode == 'binary' or setupClient.runMode == 'SimpleRNN':
            s_eff = w_test[(y_test == 1) & (yResult_test_cls > 0.5)].sum() / w_test[y_test == 1].sum()
            b_eff = w_test[(y_test != 1) & (yResult_test_cls > 0.5)].sum() / w_test[y_test != 1].sum()
            print (" ")
            print ('{:<35} {:<25.3f}'.format(Fore.GREEN+'Signal efficiency',s_eff))
            print ('{:<35} {:<25.3f}'.format(Fore.GREEN+'Background efficiency:', b_eff))
            print ('{:<35} {:<25.3f}'.format(Fore.GREEN+'Background rejection:', 1.0/b_eff))
        if setupClient.runMode == 'multi':
            channelEffi = channelDic.copy()
            for channel,i in channelDic.items():
                channelEffi[channel] = w_test[(y_test == i) & (yResult_test_cls == 1)].sum() / w_test[y_test == i].sum()
            for channel,eff in channelEffi.items():
                print ('{:<35} {:<25.3f}'.format(Fore.GREEN+channel+' efficiency',eff))

            b_eff = w_test[(y_test != 1) & (yResult_test_cls == 1)].sum() / w_test[y_test != 1].sum()
            print ('{:<30} {:<20.3f}'.format('Background efficiency', b_eff))
            print ('{:<30} {:<20.3f}'.format('Background rejection', 1.0/b_eff))
        print (" ")

    if setupClient.doScore:
        if setupClient.runMode == 'binary' or setupClient.runMode == 'SimpleRNN' or setupClient.runMode == 'param':
            # First create one sample of X_train only from signal and one only from background events
            Xtrain_signal     = X_train[y_train==1]
            Xtrain_background = X_train[y_train!=1]

            # Then do the same for Xtest
            Xtest_signal     = X_test[y_test==1]
            Xtest_background = X_test[y_test!=1]

            # Get predictions of the model on these -train- samples
            print ('Running model prediction on Xtrain_signal')
            yhat_train_signal     = model.predict(Xtrain_signal,batch_size=setupClient.Params['BatchSize'])
            print ('Running model prediction on Xtrain_background')
            yhat_train_background = model.predict(Xtrain_background,batch_size=setupClient.Params['BatchSize'])

            # Get predictions of the model on these -test- samples
            print ('Running model prediction on Xtest_signal')
            yhat_test_signal     = model.predict(Xtest_signal,batch_size=setupClient.Params['BatchSize'])
            print ('Running model prediction on Xtest_background')
            yhat_test_background = model.predict(Xtest_background,batch_size=setupClient.Params['BatchSize'])

        hasData = False
        if setupClient.runMode == 'binary' and setupClient.unblind==True:
            # Get the data PD file
            dataFileName = setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Data.pkl'
            if os.path.isfile(dataFileName):
                hasData = True
                print ('Reading Data file:',dataFileName)
                data_full = pd.read_pickle(dataFileName)
                data_full_matrix = data_full[setupClient.InputDNNVariables[setupClient.VarSet]].as_matrix()

                print ('{:<45} {:<15}'.format('Getting Scaler of Training sample from file',Fore.GREEN+setupClient.TrainedModelPath+'DNN_Setup' ) )
                if not os.path.isfile(setupClient.TrainedModelPath+'/DNN_Setup'):
                    print ("Pickle file not found!")
                    quit()
                f = open(setupClient.TrainedModelPath+'DNN_Setup', "rb")
                savedSetupClient = pickle.load(f)
                data_full_matrix = savedSetupClient.Scaler.transform(data_full_matrix)

                # Get predictions on data
                print ('Running model prediction on data')
                yhat_data = model.predict(data_full_matrix,verbose = True,batch_size=setupClient.Params['BatchSize'])
                yhat_data_rounded = np.array([round(x[0]) for x in yhat_data])
                # Save as numpy array
                # np.save( os.path.join(setupClient.ModelSavePath,"yhat_data.npy") , yhat_data)
            else:
                print ('Data file:',dataFileName,' not found. Will proceed to MC only')

        if setupClient.runMode == 'SimpleRNN': # antonio
            for ifile in setupClient.InputFilesSB['Data']:
                dataFileName = setupClient.PDPath + ifile + '_FullNoRandom.pkl'
                if os.path.isfile(dataFileName):
                    hasData = False
                    print ('Reading Data file:',dataFileName)
                    data_full = pd.read_pickle(dataFileName)

                    VariablesSet =  setupClient.InputDNNVariables[setupClient.VarSet]
                    data_full_matrix = data_full[VariablesSet].copy()
                    var_names = data_full_matrix.keys()
                    new_data_full_matrix = np.zeros( (data_full_matrix.shape[0], 6, 4) )

                    for i in range(0, data_full_matrix.shape[0]):
                        for j in range(0, data_full_matrix.shape[1]):
                            new_data_full_matrix[i, int(j/4), j%4] = data_full_matrix.iloc[i, j]
                    data_full_matrix = new_data_full_matrix

                    PrepareData.scale(data_full_matrix,  ['pt','eta','phi','E'], False, setupClient) # apply scaling to test set

                    # Get predictions on data
                    print ('Running model prediction on data')
                    yhat_data = model.predict(data_full_matrix,verbose = True,batch_size=setupClient.Params['BatchSize'])

                    data_full['RNN_Score'] = yhat_data
                    print(data_full.shape)
                    np.save( os.path.join(setupClient.ModelSavePath, "ResultsDataMLPD_" + ifile + ".npy") , data_full ) # antonio
                    np.save( os.path.join(setupClient.ModelSavePath, "rootBranchSubSampleForDataML_" + ifile + ".npy") , data_full.columns.values ) # antonio

                else:
                    print ('Data file:',dataFileName,' not found. Will proceed to MC only')


        sns.set_palette("coolwarm",4)
        # Plot scores
        bins=np.linspace(0,1, 50)
        plt.hist(yhat_train_signal,     bins=bins, histtype='step',       lw=2, alpha=0.5,  label=[r'Signal Train'],     normed=True)
        plt.hist(yhat_test_signal,      bins=bins, histtype='stepfilled', lw=2, alpha=0.5,  label=[r'Signal Test'],      normed=True)
        plt.hist(yhat_test_background,  bins=bins, histtype='stepfilled', lw=2, alpha=0.5,  label=[r'Background Test'],  normed=True)
        plt.hist(yhat_train_background, bins=bins, histtype='step',       lw=2, alpha=0.5,  label=[r'Background Train'], normed=True)
        if hasData and setupClient.unblind==True:
            # Plot the data as well. Using skh_plt because matplotlib does not come with markers for hist class
            skh_plt.hist(yhat_data, bins=bins, errorbars=True, histtype='marker', label='Data', color='black', normed=True)
        plt.ylabel('Norm. Entries')
        plt.xlabel('DNN score')
        plt.legend(loc="upper center")
        plt.savefig(setupClient.ModelSavePath+"/MC_Data_TrainTest_Score.png")
        plt.yscale('log')
        plt.savefig(setupClient.ModelSavePath+"/MC_Data_TrainTest_Score_log.png")
        plt.clf()


    if setupClient.doROC:
        if setupClient.runMode == 'binary' or setupClient.runMode == 'SimpleRNN' or setupClient.runMode == 'param':
            # Get 'Receiver operating characteristic' (ROC)
            fpr, tpr, thresholds = roc_curve(y_test, yResult_test)

            # Compute Area Under the Curve (AUC) from prediction scores
            roc_auc  = auc(fpr, tpr)
            print ('{:<35} {:<25.3f}'.format(Fore.GREEN+'ROC AUC',roc_auc))

            # print "ROC AUC: %0.3f" % roc_auc
            plt.plot(fpr, tpr, color='darkorange',  lw=2, label='Full curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 0], [1, 1], color='navy', lw=2, linestyle='--')
            plt.xlim([-0.05, 1.0])
            plt.ylim([0.0, 1.05])
            plt.ylabel('True Positive Rate')
            plt.xlabel('False Positive Rate')
            plt.title('ROC curves for Signal vs Background')
            plt.legend(loc="lower right")
            # plt.plot([0.038], [0.45], marker='*', color='red',markersize=5, label="Cut-based",linestyle="None")
            # plt.plot([0.038, 0.038], [0,1], color='red', lw=1, linestyle='--') # same background rejection point
            plt.savefig(setupClient.ModelSavePath+"/ROC.png")
            plt.clf()

            ### NOW try the weighted ROC curve
            fpr_w, tpr_w, thresholds_w = roc_curve(y_test, yResult_test,sample_weight=w_test)
            roc_auc_w  = auc(fpr_w, tpr_w,reorder=True)
            print ('{:<35} {:<25.3f}'.format(Fore.GREEN+'ROC AUC weighted',roc_auc_w))
            plt.plot(fpr_w, tpr_w, color='darkorange',  lw=2, label='Full curve (area = %0.2f)' % roc_auc_w)
            plt.plot([0, 0], [1, 1], color='navy', lw=2, linestyle='--')
            plt.xlim([-0.05, 1.0])
            plt.ylim([0.0, 1.05])
            plt.ylabel('True Positive Rate (weighted)')
            plt.xlabel('False Positive Rate (weighted)')
            plt.title('ROC curve for Signal vs Background')
            plt.legend(loc="lower right")
            # plt.plot([0.038], [0.45], marker='*', color='red',markersize=5, label="Cut-based",linestyle="None")
            # plt.plot([0.038, 0.038], [0,1], color='red', lw=1, linestyle='--') # same background rejection point
            plt.savefig(setupClient.ModelSavePath+"/ROC_weighted.png")
            plt.clf()

            np.save( os.path.join(setupClient.ModelSavePath,"tpr_w.npy") , tpr_w)
            np.save( os.path.join(setupClient.ModelSavePath,"fpr_w.npy") , fpr_w)
            np.save( os.path.join(setupClient.ModelSavePath,"thresholds_w.npy") , thresholds_w)
            np.save( os.path.join(setupClient.ModelSavePath,"thresholds.npy") , thresholds)
            np.save( os.path.join(setupClient.ModelSavePath,"tpr.npy") , tpr)
            np.save( os.path.join(setupClient.ModelSavePath,"fpr.npy") , fpr)

            np.save( os.path.join(setupClient.ModelSavePath,"AUC.npy") , roc_auc)
            np.save( os.path.join(setupClient.ModelSavePath,"AUC_w.npy") , roc_auc_w)
