cd ../MyDNNKit/

python RunML.py --ConvertRootToPD --InputMLNtuplePath /nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ --inROOTFiles top,diboson,Wjets,Zjets,data,ggFH200_,ggFH300_,ggFH400,ggFH600,ggFH700,ggFH800,ggFH1000,ggFH1200,ggFH1400,ggFH1600,ggFH1800,ggFH2000,ggFH2400,ggFH2600,ggFH3000 --PreselectionCommand "inPanda[(inPanda.Pass_MergHP_GGF_ZZSR==1) | (inPanda.Pass_MergLP_GGF_ZZSR==1) | (inPanda.Pass_MergHP_GGF_ZZZCR==1) | (inPanda.Pass_MergLP_GGF_ZZZCR==1)]" --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/

python RunML.py --ConvertRootToPD --InputMLNtuplePath /nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ --inROOTFiles top,diboson,Wjets,Zjets,data --PreselectionCommand "inPanda[(inPanda.Pass_MergHP_VBF_ZZSR==1) | (inPanda.Pass_MergLP_VBF_ZZSR==1) | (inPanda.Pass_MergHP_VBF_ZZZCR==1) | (inPanda.Pass_MergLP_VBF_ZZZCR==1)]" --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/

python RunML.py --ConvertRootToPD --InputMLNtuplePath /nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ --inROOTFiles top,diboson,Wjets,Zjets,data,ggFH200_,ggFH300_,ggFH400,ggFH600,ggFH700,ggFH800,ggFH1000,ggFH1200,ggFH1400,ggFH1600,ggFH1800,ggFH2000,ggFH2400,ggFH2600,ggFH3000 --PreselectionCommand "inPanda[(inPanda.Pass_Res_GGF_ZZSR==1) | (inPanda.Pass_ResT_GGF_ZZSR==1) | (inPanda.Pass_Res_GGF_ZZZCR==1) | (inPanda.Pass_ResT_GGF_ZZZCR==1)]" --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/

python RunML.py --ConvertRootToPD --InputMLNtuplePath /nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ --inROOTFiles top,diboson,Wjets,Zjets,data --PreselectionCommand "inPanda[(inPanda.Pass_Res_VBF_ZZSR==1) | (inPanda.Pass_ResT_VBF_ZZSR==1) | (inPanda.Pass_Res_VBF_ZZZCR==1) | (inPanda.Pass_ResT_VBF_ZZZCR==1)]" --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/

cd -
