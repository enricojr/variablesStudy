cd ../MyDNNKit/

python RunML.py --CreateTrainTestPD --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ --inSignalFiles ggFH1000 --inBackgrFiles top,diboson,Wjets,Zjets --MixPD_TrainTestTag mixPD_merged_ggF -m binary

python RunML.py --CreateTrainTestPD --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ --inSignalFiles ggFH400 --inBackgrFiles top,diboson,Wjets,Zjets --MixPD_TrainTestTag mixPD_resolved_ggF -m binary

python RunML.py --CreateTrainTestPD --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/ --inSignalFiles VBFH1000 --inBackgrFiles top,diboson,Wjets,Zjets --MixPD_TrainTestTag mixPD_merged_VBF -m binary

python RunML.py --CreateTrainTestPD --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/ --inSignalFiles VBFH700 --inBackgrFiles top,diboson,Wjets,Zjets --MixPD_TrainTestTag mixPD_resolved_VBF -m binary

cd -
