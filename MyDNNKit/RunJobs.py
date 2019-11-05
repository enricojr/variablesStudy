#! /usr/bin/env python
import os

doConvertToPD      = 0
doTrainTestSamples = 1
doTraining         = 0
doTestTrainedModel = 0
doPlotValidation   = 0

# massPoints = ['1000','1200','1400','1600','1800','2000']
massPoints = ['1000']
commands = []

bkgFiles = 'Top,Diboson,Wjets,mc16a_Zjets,mc16d_Zjets,mc16e_Zjets'
dataFiles = 'Data'
signalFiles = 'ggFH200_,ggFH300_,ggFH400,ggFH600,ggFH700,ggFH800,ggFH1000,ggFH1200,ggFH1400,ggFH1600,ggFH1800,ggFH2000,ggFH2400,ggFH2600,ggFH3000'

PDPath = 'DNN_InputDataFrames/'

mixedFileName = 'MixPD_MergedGGFH'
mode = 'binary'

if doConvertToPD:
    commands += ['python RunML.py --ConvertRootToPD --InputMLNtuplePath /nfs/kloe/einstein2/dinos/DNN_InputFlatNtuples/mc16ade_RNN_2jets_25apr/CutRNN_0p8_SelSpin0/ --inROOTFiles '+bkgFiles+ ',Data,'+signalFiles+' --PreselectionCommand "inPanda[(inPanda.Pass_MergHP_GGF_ZZSR==1) | (inPanda.Pass_MergLP_GGF_ZZSR==1) | (inPanda.Pass_MergHP_GGF_ZZZCR==1) | (inPanda.Pass_MergLP_GGF_ZZZCR==1)]" --PDPath '+PDPath ]
    # for mass in massPoints:
        # commands += ['python RunML.py -c --inROOTFiles '+signalFiles+mass+' --PreselectionCommand "inPanda[(inPanda.isMerged == 1 )]" ']


if doTrainTestSamples:
    # commands += ['python RunML.py --CreateTrainTestPD --PDPath '+PDPath+' --inDataFiles '+dataFiles+' --inSignalFiles ggFH1000  --inBackgrFiles '+bkgFiles+ ' --MixPD_TrainTestTag '+mixedFileName+ ' -m '+mode]
    # commands += ['python RunML.py --CreateTrainTestPD --useEqualSizeSandB --PDPath '+PDPath+' --inDataFiles '+dataFiles+' --inSignalFiles ggFH1000  --inBackgrFiles '+bkgFiles+ ' --MixPD_TrainTestTag '+mixedFileName+ '_EqualSB -m '+mode]
    commands += ['python RunML.py --CreateTrainTestPD --PDPath '+PDPath+' --inDataFiles '+dataFiles+' --inSignalFiles ggFH1000,ggFH1200,ggFH1400,ggFH1600,ggFH1800,ggFH2000,ggFH2400,ggFH2600,ggFH3000  --inBackgrFiles '+bkgFiles+ ' --MixPD_TrainTestTag '+mixedFileName+ '_param -m param']
    # for mass in massPoints:
        # commands += ['python RunML.py -p --inSignalFiles '+signalFiles+mass+'  --inBackgrFiles '+bkgFiles+' --inDataFiles '+dataFiles+'  -N '+mixedFileName+mass+ ' --PreselectionCommand "inPanda[(inPanda.isMerged == 1 ) & (inPanda.isVBFevent == 0)]" ' ]



comboList = [0]
# comboList = range(0,48)

if doTraining:
    for mass in massPoints:
        for combo in comboList:
            # commands += ['python RunML.py --Train --PDPath '+PDPath+' -y '+str(combo)+' --MixPD_TrainTestTag '+mixedFileName+ '  -o DNN_Trained/Train_S1000 -m binary' ]
            commands += ['python RunML.py --Train --PDPath '+PDPath+' -y '+str(combo)+' --MixPD_TrainTestTag '+mixedFileName+ '_param  -o DNN_Trained/Train_param -m param' ]



modelpath = 'llqqDNN_64_1024_3_0.0003_VarSet0/'

if doTestTrainedModel:
    # commands += ['python RunML.py --LoadTrainedModel --doConfusionMatrix --doScore --doEfficiency --doROC --PDPath '+PDPath+' --MixPD_TrainTestTag '+mixedFileName+'  --TrainedModelPath DNN_Trained/Train_S1000/'+modelpath+'  -o  DNN_Tests/binary/ -m binary']
    commands += ['python RunML.py --LoadTrainedModel --massPointToTest '"[1000,1200,1400,1600]"' --inSignalFiles=ggFH1000,ggFH1200,ggFH1400 --inDataFiles Data --inBackgrFiles mc16a_Zjets,mc16d_Zjets,mc16e_Zjets,Wjets,Diboson,Top --PDPath '+PDPath+' --MixPD_TrainTestTag '+mixedFileName+'  --TrainedModelPath DNN_Trained/Train_param/'+modelpath+'  -o  DNN_Tests/param/ -m param']





if doPlotValidation:
    for mass in massPoints:
        # commands += ['python RunML.py --ValidPlotsFromTrainTestDF  -N '+mixedFileName+mass]
        commands += ['python RunML.py --ValidPlotsDataMC --inSignalFiles '+signalFiles+mass+' --inBackgrFiles '+bkgFiles+' --inDataFiles '+dataFiles]



for n,i in enumerate(commands):
    print (" ")
    print ("--------------------------------------------")
    print (n,' -- ',i)
#    os.system(i)
