### WARNING:
#   remember to edit Configuration.py and enable the corresponding set of variables

cd ../MyDNNKit/

python RunML.py --LoadTrainedModel --doConfusionMatrix --doScore --doEfficiency --doROC --massPointToTest [1000] --inSignalFiles=ggFH1000 --inDataFiles data --inBackgrFiles top,diboson,Wjets,Zjets --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ --MixPD_TrainTestTag mixPD_merged_ggF  --TrainedModelPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/train_2variables/llqqDNN_64_1024_4_0.0003_VarSet0/ -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/test_2variables/ -m binary

python RunML.py --LoadTrainedModel --doConfusionMatrix --doScore --doEfficiency --doROC --massPointToTest [1000] --inSignalFiles=ggFH1000 --inDataFiles data --inBackgrFiles top,diboson,Wjets,Zjets --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ --MixPD_TrainTestTag mixPD_merged_ggF  --TrainedModelPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/train_2variables/llqqDNN_64_1024_4_0.0003_VarSet1/ -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/test_2variables/ -m binary

python RunML.py --LoadTrainedModel --doConfusionMatrix --doScore --doEfficiency --doROC --massPointToTest [1000] --inSignalFiles=ggFH1000 --inDataFiles data --inBackgrFiles top,diboson,Wjets,Zjets --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ --MixPD_TrainTestTag mixPD_merged_ggF  --TrainedModelPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/train_2variables/llqqDNN_64_1024_4_0.0003_VarSet2/ -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/test_2variables/ -m binary

python RunML.py --LoadTrainedModel --doConfusionMatrix --doScore --doEfficiency --doROC --massPointToTest [1000] --inSignalFiles=VBFH1000 --inDataFiles data --inBackgrFiles top,diboson,Wjets,Zjets --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/ --MixPD_TrainTestTag mixPD_merged_VBF  --TrainedModelPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/train_2variables/llqqDNN_64_1024_4_0.0003_VarSet0/ -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/test_2variables/ -m binary

python RunML.py --LoadTrainedModel --doConfusionMatrix --doScore --doEfficiency --doROC --massPointToTest [1000] --inSignalFiles=VBFH1000 --inDataFiles data --inBackgrFiles top,diboson,Wjets,Zjets --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/ --MixPD_TrainTestTag mixPD_merged_VBF  --TrainedModelPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/train_2variables/llqqDNN_64_1024_4_0.0003_VarSet1/ -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/test_2variables/ -m binary

python RunML.py --LoadTrainedModel --doConfusionMatrix --doScore --doEfficiency --doROC --massPointToTest [1000] --inSignalFiles=VBFH1000 --inDataFiles data --inBackgrFiles top,diboson,Wjets,Zjets --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/ --MixPD_TrainTestTag mixPD_merged_VBF  --TrainedModelPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/train_2variables/llqqDNN_64_1024_4_0.0003_VarSet2/ -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/test_2variables/ -m binary

cd -
