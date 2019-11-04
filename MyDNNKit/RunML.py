import sys,argparse,glob

import PrepareData
import PlotTools
from Configuration import *
from HelperTools import *
from TrainDNN import TrainDNN,TrainRNN
from LoadDNN import LoadDNN
from KFold_xval import doKFold
from ConfigClass import ConfigClass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deep Neural Network Training and testing Framework')
    group = parser.add_mutually_exclusive_group()

    # Main Job to Run
    group.add_argument('-c',  '--ConvertRootToPD',     action="store_true",  help="Takes flat ROOT Ntuples as input and outputs Panda Dataframes")
    group.add_argument('-p',  '--CreateTrainTestPD',   action="store_true",  help="Mixing and shuffling of Panda Dataframes Signal and Background MC samples")
    group.add_argument('-t',  '--Train',               action="store_true",  help="Train a DNN model")
    group.add_argument('-l',  '--LoadTrainedModel',    action="store_true",  help="Will load an existing trained model")
    group.add_argument('--ValidPlotsFromTrainTestDF',  action="store_true",  help="plot input variables")
    group.add_argument('--ValidPlotsDataMC',                 action="store_true",  help="plot Data/MC variables")
    group.add_argument('-d',  '--printParamSet',       action="store_true",  help="Dump the available HyperParameter sets")
    group.add_argument('-D',  '--printSetup',          action="store_true",  help="Dump the setup")

    #Options on Convert ROOT Files to Pandas
    parser.add_argument('--inROOTFiles', required='--ConvertRootToPD' in sys.argv, help='input ROOT file list, comma separated', type=str)
    parser.add_argument('--InputMLNtuplePath', required='--ConvertRootToPD' in sys.argv, help='input ROOT file directory', type=str)

    #Options on Create the mixed S+B Pandas file to be used as input for training and testing
    parser.add_argument('--inSignalFiles',    required=('--ValidPlotsDataMC' in sys.argv) or  '--CreateTrainTestPD' in sys.argv or '-p' in sys.argv, default='None',  help='input Signal file list, comma separated',type=str)
    parser.add_argument('--inBackgrFiles',    required=('--ValidPlotsDataMC' in sys.argv) or  '--CreateTrainTestPD' in sys.argv or '-p' in sys.argv, default='None',  help='input Background file list, comma separated',type=str)
    parser.add_argument('--inDataFiles' ,     required=('--ValidPlotsDataMC' in sys.argv), default='None',  help='input Data file list, comma separated',type=str)

    #Options on Training
    parser.add_argument('-y',  '--hyperparamset',   default="-1",        required='--Train' in sys.argv or '-t' in sys.argv, help="Select of the parameter set to train with. With -1 you get a random one out of all the permutations",type=int)
    parser.add_argument('-k',  '--doKFold',         action="store_true", help="Do K-Fold validation")
    parser.add_argument('-M',  '--modelPrefixName', default="llqqDNN",   help="output prefix of the model name",type=str)
    parser.add_argument('--useEqualSizeSandB', action="store_true",    help="Use exactly 50:50 N events for sig:bkg")

    #Options on Testing an existing Trained Model
    parser.add_argument('-L',  '--TrainedModelPath',  required='--LoadTrainedModel' in sys.argv or '-l' in sys.argv, help="Will load an existing trained model from specific path",type=str)
    parser.add_argument('--doConfusionMatrix', action="store_true",       help="")
    parser.add_argument('--doEfficiency',      action="store_true",       help="")
    parser.add_argument('--doScore',           action="store_true",       help="")
    parser.add_argument('--doROC',             action="store_true",       help="")
    parser.add_argument('--unblind',           action="store_true",       help="")
    parser.add_argument('--massPointToTest',       help="When running the param network this defines which mass point in GeV will be tested")
    parser.add_argument('--testModelOnFullSamples',action="store_true",       help="")

    # general Common options
    parser.add_argument('--PreselectionCommand' , default="",  help='String which will be translated to python command when creating the train/test PDs and filter the initial PDs according to it. E.g inPanda[(inPanda.isMerged == 1 ) & (inPanda.isVBFevent == 0)]',type=str)
    parser.add_argument('--PDPath', required=('--printParamSet' not in sys.argv and '-d' not in sys.argv and '-D' not in sys.argv), help='output directory containing Pandas DF', type=str)
    parser.add_argument('-N',  '--MixPD_TrainTestTag', required=('--ValidPlotsFromTrainTestDF' in sys.argv) or ('--CreateTrainTestPD' in sys.argv or '-p' in sys.argv) or ('--Train' in sys.argv or '-t' in sys.argv) or ('--LoadTrainedModel' in sys.argv  or '-l' in sys.argv), default="Mix",  help="Name of the PD train/test file",type=str)
    parser.add_argument('-m',  '--mode',  required=('--Train' in sys.argv or '-t' in sys.argv) or ('--LoadTrainedModel' in sys.argv or '-l' in sys.argv),      default="binary", choices=['binary', 'multi', 'param', 'SimpleRNN', 'CNN', 'SVM'], help="Decide whether to run on binary or multi classification mode or in the parameterized DNN mode")
    parser.add_argument('-o',  '--outBaseDir', default="ModelOutput",help="directory to output the training/testing results",type=str)

    #Options on Validation
    parser.add_argument('--VarPlotPath',required=('--ValidPlotsFromTrainTestDF' in sys.argv) or ('--ValidPlotsDataMC' in sys.argv), default="VarPlotPath",help="directory to output the validation plots",type=str)


    #store the user defined options
    args = parser.parse_args()
    inROOTFiles = []

    if args.ConvertRootToPD:
        inROOTFiles = (args.inROOTFiles).split(',')

    InputFilesSB = {}
    if args.CreateTrainTestPD or args.ValidPlotsDataMC or args.LoadTrainedModel :
        InputFilesSB = {
            'Signal': (args.inSignalFiles).split(','),
            'Background': (args.inBackgrFiles).split(','),
            'Data': (args.inDataFiles).split(',')
        }

    setupClient = ConfigClass(
        runMode       = args.mode,
        HyperParamSet = args.hyperparamset,
        PrintParamSet = args.printParamSet,
        printSetup    = args.printSetup,
        ValidPlotsFromTrainTestDF     = args.ValidPlotsFromTrainTestDF,
        ValidPlotsDataMC    = args.ValidPlotsDataMC,
        VariablesToPlot  = VariablesToPlot,
        VarPlotPath      = args.VarPlotPath,

        ConvertRootToPD   = args.ConvertRootToPD,
        InputMLNtuplePath= args.InputMLNtuplePath,
        InputROOTFiles   = inROOTFiles,
        rootBranchSubSample=rootBranchSubSample,

        CreateTrainTestPD   = args.CreateTrainTestPD,
        InputFilesSB     = InputFilesSB,
        MixPD_TrainTestTag   = args.MixPD_TrainTestTag,

        Train         = args.Train,
        DoKFold       = args.doKFold,
        Dropout          = Dropout,
        Params           = Params,
        ScanParams       = ScanParams,

        LoadTrainedModel     = args.LoadTrainedModel,
        TrainedModelPath = args.TrainedModelPath,

        OutBaseDir    = args.outBaseDir,
        modelPrefixName      = args.modelPrefixName,
        useEqualSizeSandB = args.useEqualSizeSandB,

        PDPath           = args.PDPath,
        InputDNNVariables   = InputDNNVariables,
        massPoint = args.massPointToTest,
        MaskValue        = -99.,
        PreselectionCuts = args.PreselectionCommand,
        doConfusionMatrix = args.doConfusionMatrix,
        doEfficiency      = args.doEfficiency,
        doScore           = args.doScore,
        doROC             = args.doROC,
        unblind           = args.unblind,
        testModelOnFullSamples = args.testModelOnFullSamples
    )

    if setupClient.ConvertRootToPD:
        print (Fore.BLUE+"--------------------------")
        print (Back.BLUE+' CONVERTING ROOT-->PANDAS ')
        print (Fore.BLUE+"--------------------------")
        print ('{:<45} {:<15}'.format("Input Flat Ntuples directory",Fore.GREEN+setupClient.InputMLNtuplePath))
        print ('{:<45} {:<15}'.format('Output Pandas Dataframe directory',Fore.GREEN+ setupClient.PDPath), checkCreateDir(setupClient.PDPath) )
        print ('{:<45} {:<15}'.format('Branches to keep from ROOT file',Fore.GREEN+str(setupClient.rootBranchSubSample)))
        PrepareData.convertToPanda(setupClient)
    elif setupClient.CreateTrainTestPD:
        print (Fore.BLUE+"--------------------------")
        print (Back.BLUE+'  CREATING TRAIN/TEST PDs ')
        print (Fore.BLUE+"--------------------------")
        print ('{:<45} {:<15}'.format('InputFilesSB',Fore.GREEN+str(InputFilesSB)))
        print ('{:<45} {:<15}'.format('I/O Pandas Dataframe directory',Fore.GREEN+ setupClient.PDPath), checkCreateDir(setupClient.PDPath) )
        print ('{:<45} {:<15}'.format('PD Train/Test Name Tag',Fore.MAGENTA + setupClient.MixPD_TrainTestTag))
        print ('{:<45} {:<15}'.format('PreselectionCuts',Fore.MAGENTA + setupClient.PreselectionCuts))
        PrepareData.preparePandas(setupClient)
    elif setupClient.Train:
        print (Fore.BLUE+"--------------------------")
        print (Back.BLUE+"    TRAIN A DNN MODEL     ")
        print (Fore.BLUE+"--------------------------")
        print ('{:<45} {:<15}'.format('I/O Pandas Dataframe directory',Fore.GREEN+ setupClient.PDPath), checkCreateDir(setupClient.PDPath) )
        print ('{:<45} {:<15}'.format('Train Ouput top directory',Fore.GREEN + setupClient.OutBaseDir), checkCreateDir(setupClient.OutBaseDir) )
        print ('{:<45} {:<15}'.format('RunMode',Fore.GREEN + setupClient.runMode) )
        print ('{:<45} {:<15}'.format('PD Train Name Tag',Fore.GREEN + setupClient.MixPD_TrainTestTag))
        print ('{:<45} {:<15}'.format('Do KFold validation',(Fore.GREEN if setupClient.DoKFold else Fore.RED)+str(setupClient.DoKFold)) )
        pickModelParamSet(setupClient)
        if setupClient.runMode == 'SimpleRNN':
            modelMetricsHistory = TrainRNN(setupClient)
            PlotTools.plotTrainPerformance(setupClient,modelMetricsHistory)
        else:
            modelMetricsHistory = TrainDNN(setupClient)
            PlotTools.plotTrainPerformance(setupClient,modelMetricsHistory)
            if setupClient.DoKFold:
                doKFold(setupClient)
    elif setupClient.LoadTrainedModel:
        print (Fore.BLUE+"--------------------------")
        print (Back.BLUE+" TEST A TRAINED DNN MODEL ")
        print (Fore.BLUE+"--------------------------")
        print ('{:<45} {:<15}'.format('I/O Pandas Dataframe directory',Fore.GREEN+ setupClient.PDPath), checkCreateDir(setupClient.PDPath) )
        print ('{:<45} {:<15}'.format('Test Ouput top directory',Fore.GREEN + setupClient.OutBaseDir), checkCreateDir(setupClient.OutBaseDir) )
        print ('{:<45} {:<15}'.format('RunMode',Fore.GREEN + setupClient.runMode) )
        print ('{:<45} {:<15}'.format('PD Test Name Tag',Fore.GREEN + setupClient.MixPD_TrainTestTag))
        print ('{:<45} {:<15}'.format('Load Model from path', Fore.GREEN+setupClient.TrainedModelPath) )
        print ('{:<45} {:<15}'.format('Create the Confusion Matrix', Fore.GREEN+str(setupClient.doConfusionMatrix)) )
        print ('{:<45} {:<15}'.format('Calculate Signal and Background Efficienies', Fore.GREEN+str(setupClient.doEfficiency)) )
        print ('{:<45} {:<15}'.format('Plot the NN-Score from Train/Test samples', Fore.GREEN+str(setupClient.doScore)) )
        print ('{:<45} {:<15}'.format('Create the ROC curve', Fore.GREEN+str(setupClient.doROC)) )
        print ('{:<45} {:<15}'.format('Data unblind', Fore.GREEN+str(setupClient.unblind)) )
        LoadDNN(setupClient)
    elif setupClient.ValidPlotsFromTrainTestDF:
        print (Fore.BLUE+"--------------------------")
        print (Back.BLUE+" VALIDATION PLOTS FROM DF ")
        print (Fore.BLUE+"--------------------------")
        print ('{:<45} {:<15}'.format('Plots Save directory',Fore.GREEN + setupClient.VarPlotPath),checkCreateDir(setupClient.VarPlotPath) )
        PlotTools.plotDFs(setupClient)
    elif setupClient.ValidPlotsDataMC:
        print (Fore.BLUE+"--------------------------")
        print (Back.BLUE+"  DATA/MC PLOTS FROM DF   ")
        print (Fore.BLUE+"--------------------------")
        print ('{:<45} {:<15}'.format('Validation Plots Save directory',Fore.GREEN + setupClient.VarPlotPath),checkCreateDir(setupClient.VarPlotPath) )
        PlotTools.plotDataMC(setupClient)
    elif args.printSetup:
        setupClient.printSetupParameters()
    elif args.printParamSet:
        printScanParamCombos(setupClient)

    print('')
