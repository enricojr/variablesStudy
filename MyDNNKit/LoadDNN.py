from keras.models import Model,load_model

from HelperTools import *
from PrepareData import LoadData,LoadDataRNN
import PlotTools
import pickle

def LoadDNN(setupClient):
    modelpath = setupClient.TrainedModelPath

    # print ('---- START Configuration dump ----')
    # attrs = vars(setupClient)
    # print ('\n'.join("%s: %s" % item for item in attrs.items()))
    # print ('---- END Configuration dump ----')


    if not os.path.isfile(modelpath + '/model.h5'):
        print(Fore.RED+'Model path does not exist')
        quit()
    if not os.path.isfile(modelpath + '/DNN_Setup'):
        print(Fore.RED+'Training configuration pickle file not found')
        print("Will configure from path name")
        modelName = modelpath.split('/',1)[1]
        print(modelName.split('_'))
        setupClient.Params['BatchSize'] = int(modelName.split('_')[2])
        varSet_str = modelpath.split('VarSet',1)[1]
        setupClient.VarSet = int(varSet_str[:1])
        setupClient.ModelSavePath = os.path.join(setupClient.OutBaseDir,modelName)
    else:
        print ('{:<45}'.format('Opening Training pickle file',Fore.GREEN+modelpath+'DNN_Setup' ) )
        f = open(modelpath+'DNN_Setup', "rb")
        print ('{:<45}'.format('Loading savedSetupClient...Changing parameters' ) )
        savedSetupClient = pickle.load(f)

        # print ('---- START Configuration dump ----')
        # attrs = vars(savedSetupClient)
        # print ('\n'.join("%s: %s" % item for item in attrs.items()))
        # print ('---- END Configuration dump ----')

        print ('{:<45} {:<15} {:<15}'.format( Fore.RED+"setupClient.Params['BatchSize']", Fore.RESET+'replaced with... ',Fore.BLUE+str(savedSetupClient.Params['BatchSize']) ) )
        setupClient.Params['BatchSize'] = savedSetupClient.Params['BatchSize']

        print ('{:<45} {:<15} {:<15}'.format(Fore.RED+"setupClient.Params['VarSet']", Fore.RESET+'replaced with... ',Fore.BLUE+str(savedSetupClient.Params['VarSet']) ) )
        setupClient.Params['VarSet']    = savedSetupClient.Params['VarSet']

        print ('{:<45} {:<15} {:<15}'.format(Fore.RED+'VarSet'+str(setupClient.VarSet), Fore.RESET+'replaced with... ',Fore.BLUE+str(savedSetupClient.Params['VarSet']) ) )
        setupClient.VarSet              = savedSetupClient.Params['VarSet']
        setupClient.ModelSavePath       = os.path.join(setupClient.OutBaseDir,savedSetupClient.ModelParamCombo)
        if setupClient.runMode != savedSetupClient.runMode :
            print ('{:<45} {:<15}'.format(Fore.RED+'RunMode of Training was '+savedSetupClient.runMode +Fore.RESET,'Requested for testing is '+Fore.MAGENTA+setupClient.runMode ) )
            print ('{:<45} {:<15}'.format('Overriding run mode to',Fore.MAGENTA+savedSetupClient.runMode) )
            setupClient.runMode = savedSetupClient.runMode

        # if setupClient.InputDNNVariables != savedSetupClient.InputDNNVariables:
        #     print('ERROR: Variable inputs do not match')
        #     quit()

    # print ('---- START Configuration dump ----')
    # attrs = vars(savedSetupClient)
    # print ('\n'.join("%s: %s" % item for item in attrs.items()))
    # print ('---- END Configuration dump ----')

    print ('{:<45} {:<15}'.format('Save Results at', Fore.GREEN+setupClient.ModelSavePath), checkCreateDir(setupClient.ModelSavePath) )

    if setupClient.runMode == 'SimpleRNN':
        print ("In LoadDNN.py ---> LoadDataRNN")
        (X_train, y_train), (X_test, y_test), (w_train,w_test), (ix_train, ix_test) = LoadDataRNN(setupClient)
        print ("Number of input variables : ",X_train.shape[1])
        print('Loading RNN model',modelpath+'/model.h5')
        model = load_model(modelpath+'/model.h5')
        PlotTools.PlotResults(setupClient,model,X_train,X_test,y_train,y_test,w_train,w_test,ix_train, ix_test)

    elif setupClient.runMode == 'param':
        print('Loading pDNN model from',modelpath+'/model.h5')
        model = load_model(modelpath+'/model.h5')
        if setupClient.testModelOnFullSamples == True:
            PlotTools.TestParamModelOnFullSamples(setupClient,model)
        else:
            PlotTools.TestParamModelOnTestSamples(setupClient,model)

    elif setupClient.runMode == 'binary':
        print('Testing DNN model on test samples')
        (X_train, y_train), (X_test, y_test), (w_train,w_test), (ix_train, ix_test) = LoadData(setupClient)
        print('Loading DNN model from',modelpath+'/model.h5')
        model = load_model(modelpath+'/model.h5')
        PlotTools.PlotResults(setupClient,model,X_train,X_test,y_train,y_test,w_train,w_test,ix_train, ix_test)

    else:
        print('Not a valid run mode. Running nothing')
