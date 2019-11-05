cd ../MyDNNKit/

python RunML.py --CreateTrainTestPD --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ --inSignalFiles ggFH200,ggFH300,ggFH400,ggFH600,ggFH700,ggFH800,ggFH1000,ggFH1200,ggFH1400,ggFH1600,ggFH1800,ggFH2000,ggFH2400,ggFH2600,ggFH3000 --inBackgrFiles top,diboson,Wjets,Zjets --MixPD_TrainTestTag mixPD_merged_ggF -m binary

python RunML.py --CreateTrainTestPD --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ --inSignalFiles ggFH200,ggFH300,ggFH400,ggFH600,ggFH700,ggFH800,ggFH1000,ggFH1200,ggFH1400,ggFH1600,ggFH1800,ggFH2000,ggFH2400,ggFH2600,ggFH3000 --inBackgrFiles top,diboson,Wjets,Zjets --MixPD_TrainTestTag mixPD_resolved_ggF -m binary

python RunML.py --CreateTrainTestPD --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/ --inSignalFiles VBFH1000,VBFH1200,VBFH1400,VBFH1600,VBFH1800,VBFH2000,VBFH200,VBFH2400,VBFH2600,VBFH3000,VBFH300,VBFH400,VBFH600,VBFH700,VBFH800 --inBackgrFiles top,diboson,Wjets,Zjets --MixPD_TrainTestTag mixPD_merged_VBF -m binary

python RunML.py --CreateTrainTestPD --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/ --inSignalFiles VBFH1000,VBFH1200,VBFH1400,VBFH1600,VBFH1800,VBFH2000,VBFH200,VBFH2400,VBFH2600,VBFH3000,VBFH300,VBFH400,VBFH600,VBFH700,VBFH800 --inBackgrFiles top,diboson,Wjets,Zjets --MixPD_TrainTestTag mixPD_resolved_VBF -m binary

cd -
