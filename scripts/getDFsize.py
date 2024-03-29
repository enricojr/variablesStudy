import pandas as pd

fileName = []

fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/data.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/diboson_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/diboson_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1200_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1200_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1800_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH1800_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH2000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH2000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH200_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH200_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH2400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH2400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH2600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH2600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH3000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH3000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH300_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH300_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH700_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH700_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH800_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ggFH800_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/mixPD_merged_ggF_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/mixPD_merged_ggF_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/top_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/top_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/Wjets_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/Wjets_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/Zjets_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/Zjets_Train.pkl')

fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/data.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/diboson_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/diboson_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1200_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1200_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1800_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH1800_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH2000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH2000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH200_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH200_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH2400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH2400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH2600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH2600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH3000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH3000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH300_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH300_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH700_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH700_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH800_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ggFH800_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/mixPD_resolved_ggF_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/mixPD_resolved_ggF_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/top_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/top_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/Wjets_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/Wjets_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/Zjets_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/Zjets_Train.pkl')

fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/data.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/diboson_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/diboson_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/mixPD_resolved_VBF_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/mixPD_resolved_VBF_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/top_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/top_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1200_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1200_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1800_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH1800_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH2000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH2000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH200_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH200_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH2400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH2400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH2600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH2600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH3000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH3000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH300_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH300_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH700_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH700_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH800_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/VBFH800_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/Wjets_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/Wjets_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/Zjets_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/Zjets_Train.pkl')

fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/data.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/diboson_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/diboson_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/mixPD_merged_VBF_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/mixPD_merged_VBF_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/top_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/top_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1200_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1200_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1800_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH1800_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH2000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH2000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH200_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH200_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH2400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH2400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH2600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH2600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH3000_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH3000_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH300_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH300_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH400_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH400_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH600_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH600_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH700_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH700_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH800_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/VBFH800_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/Wjets_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/Wjets_Train.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/Zjets_Test.pkl')
fileName.append('/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/Zjets_Train.pkl')

for i in fileName:
    print(i)
    print(len(pd.read_pickle(i)))
