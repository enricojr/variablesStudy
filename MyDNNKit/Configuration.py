import random,os
from Permutator import *
from ConfigClass import ConfigClass
from HelperTools import *

## All available variables 2-lep
# ['VTEventID', 'hasOSEtaJetsPair', 'NNScore', 'NNScore_ZZ', 'NNScore_ZW', 'isTestEvent', 'DR_Zmass', 'l1_e', 'l1_pt', 'l1_eta', 'l1_phi', 'l1_charge', 'l2_e', 'l2_pt', 'l2_eta', 'l2_phi', 'l2_charge', 'll_m', 'll_pt', 'jj_pt', 'jj_eta', 'jj_phi', 'jj_m', 'jj_j1pt', 'jj_j1eta', 'jj_j1phi', 'jj_j1M', 'jj_j1NTracks', 'jj_j2pt', 'jj_j2eta', 'jj_j2phi', 'jj_j2M', 'jj_j2NTracks', 'fat_jet_M', 'fat_jet_E', 'fat_jet_pt', 'fat_jet_eta', 'fat_jet_phi', 'fat_jet_D2', 'fat_jet_C2', 'fat_jet_ntrack', 'fat_jet_nbtags', 'fat_jet_D2Eff50', 'fat_jet_D2Eff80', 'fat_jet_ntrackjet', 'fat_jet_trackjet1_pt', 'fat_jet_trackjet1_eta', 'fat_jet_trackjet1_phi', 'fat_jet_trackjet1_E', 'fat_jet_trackjet1_M', 'fat_jet_trackjet1_MV2c10', 'fat_jet_trackjet1_isBtag', 'fat_jet_trackjet2_pt', 'fat_jet_trackjet2_eta', 'fat_jet_trackjet2_phi', 'fat_jet_trackjet2_E', 'fat_jet_trackjet2_M', 'fat_jet_trackjet2_MV2c10', 'fat_jet_trackjet2_isBtag', 'DSID', 'weight', 'WEIGHT', 'bTagSF', 'trkJetBTagSF', 'weight_lumi', 'weight_SFTrigger', 'weight_PUReweight', 'weight_MCEventWeight', 'weight_VZqqZbbWeight', 'weight_sumOfWeightsScaling', 'MET', 'muCross', 'Topology', 'isSignal', 'isResolvedPresel', 'isVBFevent', 'isVBFMergedOverlap', 'isVBFMergedPresel', 'isResolved_before_ratio', 'isMerged_before_ratio', 'Pass_MergHP_VBF_ZZSR', 'Pass_MergHP_VBF_WZSR', 'Pass_MergHPT_VBF_ZZSR', 'Pass_MergHPT_VBF_WZSR', 'Pass_MergHPU_VBF_ZZSR', 'Pass_MergHPU_VBF_WZSR', 'Pass_MergLP_VBF_ZZSR', 'Pass_MergLP_VBF_WZSR', 'Pass_MergLPT_VBF_ZZSR', 'Pass_MergLPT_VBF_WZSR', 'Pass_MergLPU_VBF_ZZSR', 'Pass_MergLPU_VBF_WZSR', 'Pass_MergHP_VBF_ZZZCR', 'Pass_MergLP_VBF_ZZZCR', 'Pass_MergHP_VBF_ZZTCR', 'Pass_MergLP_VBF_ZZTCR', 'isVBFResolvedOverlap', 'Pass_Res_VBF_ZZSR', 'Pass_Res_VBF_WZSR', 'Pass_Res_VBF_ZZZCR', 'Pass_Res_VBF_WZZCR', 'Pass_Res_VBF_ZZTCR', 'Pass_Res_VBF_WZTCR', 'isGGFMergedOverlap', 'isGGFMergedPresel', 'Pass_MergHP_GGF_ZZSR', 'Pass_MergHP_GGF_WZSR', 'Pass_MergHPT_GGF_ZZSR', 'Pass_MergHPT_GGF_WZSR', 'Pass_MergHPU_GGF_ZZSR', 'Pass_MergHPU_GGF_WZSR', 'Pass_MergLP_GGF_ZZSR', 'Pass_MergLP_GGF_WZSR', 'Pass_MergLPT_GGF_ZZSR', 'Pass_MergLPT_GGF_WZSR', 'Pass_MergLPU_GGF_ZZSR', 'Pass_MergLPU_GGF_WZSR', 'Pass_MergHP_GGF_ZZZCR', 'Pass_MergHPU_GGF_ZZZCR', 'Pass_MergHPT_GGF_ZZZCR', 'Pass_MergLP_GGF_ZZZCR', 'Pass_MergLPU_GGF_ZZZCR', 'Pass_MergLPT_GGF_ZZZCR', 'Pass_MergHP_GGF_ZZTCR', 'Pass_MergHPU_GGF_ZZTCR', 'Pass_MergHPT_GGF_ZZTCR', 'Pass_MergLP_GGF_ZZTCR', 'Pass_MergLPU_GGF_ZZTCR', 'Pass_MergLPT_GGF_ZZTCR', 'Pass_Res_GGF_ZZSR', 'Pass_Res_GGF_WZSR', 'Pass_Res_GGF_ZZZCR', 'Pass_Res_GGF_WZZCR', 'Pass_Res_GGF_ZZTCR', 'Pass_Res_GGF_WZTCR', 'Pass_ResT_GGF_ZZSR', 'Pass_ResT_GGF_WZSR', 'Pass_ResT_GGF_ZZZCR', 'Pass_ResT_GGF_WZZCR', 'Pass_ResT_GGF_ZZTCR', 'Pass_ResT_GGF_WZTCR', 'isMerged', 'isResolved', 'isCR', 'xsec', 'BR', 'FilterEff', 'kFact', 'ratio_merged', 'ratio_resolved', 'X_boosted_m', 'X_resolved_ZZ_m', 'X_resolved_WZ_m', 'truth_zv_mass', 'signal_jet1_E', 'signal_jet1_pt', 'signal_jet1_eta', 'signal_jet1_phi', 'signal_jet1_ntrack', 'signal_jet1_PartonID', 'signal_jet1_MV2c10', 'signal_jet1_TrackWidth', 'signal_jet1_CaloWidth', 'signal_jet2_E', 'signal_jet2_pt', 'signal_jet2_eta', 'signal_jet2_phi', 'signal_jet2_ntrack', 'signal_jet2_PartonID', 'signal_jet2_MV2c10', 'signal_jet2_TrackWidth', 'signal_jet2_CaloWidth', 'NSignalBJets', 'mjj', 'detajj', 'tag1_jet_pt', 'tag1_jet_eta', 'tag1_jet_phi', 'tag1_jet_E', 'tag1_jet_nTrack', 'tag1_jet_PartonID', 'tag1_jet_TrackWidth', 'tag1_jet_CaloWidth', 'tag2_jet_pt', 'tag2_jet_eta', 'tag2_jet_phi', 'tag2_jet_E', 'tag2_jet_nTrack', 'tag2_jet_PartonID', 'tag2_jet_TrackWidth', 'tag2_jet_CaloWidth', 'NJETS', 'NSIGJETS', 'nQuarkJets', 'nGluonJets', 'nUndefJets', 'Jet1_MV2c10', 'Jet2_MV2c10', 'Jet3_MV2c10', 'Jet4_MV2c10', 'Jet5_MV2c10', 'Jet6_MV2c10', 'NFATJETS', 'FatJet1_pt', 'FatJet1_eta', 'FatJet1_phi', 'FatJet1_E', 'FatJet2_pt', 'FatJet2_eta', 'FatJet2_phi', 'FatJet2_E', 'FatJet3_pt', 'FatJet3_eta', 'FatJet3_phi', 'FatJet3_E', 'Jet1_pt', 'Jet1_eta', 'Jet1_phi', 'Jet1_E', 'Jet1_nTrack', 'Jet1_TrackWidth', 'Jet1_CaloWidth', 'Jet1_PartonID', 'Jet1_isbjet', 'Jet2_pt', 'Jet2_eta', 'Jet2_phi', 'Jet2_E', 'Jet2_nTrack', 'Jet2_TrackWidth', 'Jet2_CaloWidth', 'Jet2_PartonID', 'Jet2_isbjet', 'Jet3_pt', 'Jet3_eta', 'Jet3_phi', 'Jet3_E', 'Jet3_nTrack', 'Jet3_TrackWidth', 'Jet3_CaloWidth', 'Jet3_PartonID', 'Jet3_isbjet', 'Jet4_pt', 'Jet4_eta', 'Jet4_phi', 'Jet4_E', 'Jet4_nTrack', 'Jet4_TrackWidth', 'Jet4_CaloWidth', 'Jet4_PartonID', 'Jet4_isbjet', 'Jet5_pt', 'Jet5_eta', 'Jet5_phi', 'Jet5_E', 'Jet5_nTrack', 'Jet5_TrackWidth', 'Jet5_CaloWidth', 'Jet5_PartonID', 'Jet5_isbjet', 'Jet6_pt', 'Jet6_eta', 'Jet6_phi', 'Jet6_E', 'Jet6_nTrack', 'Jet6_TrackWidth', 'Jet6_CaloWidth', 'Jet6_PartonID', 'Jet6_isbjet']


# rootBranchSubSample= ['l1_e', 'l1_pt', 'l1_eta', 'l1_phi', 'l2_e','l2_pt', 'l2_eta', 'l2_phi', 'fat_jet_E', 'fat_jet_pt', 'fat_jet_eta', 'fat_jet_phi', 'fat_jet_M', 'fat_jet_D2', 'll_m', 'll_pt', 'NJETS', 'isSignal','weight', 'truth_zv_mass','isMerged','X_boosted_m','isCR','isVBFevent']

rootBranchSubSample = ['VTEventID', 'NNScore', 'l1_e', 'l1_pt', 'l1_eta', 'l1_phi', 'l2_e', 'l2_pt', 'l2_eta', 'l2_phi', 'll_m', 'll_pt', 'jj_pt', 'jj_eta', 'jj_phi', 'jj_m', 'jj_j1pt', 'jj_j1eta', 'jj_j1phi', 'jj_j1M','jj_j1NTracks', 'jj_j2pt', 'jj_j2eta', 'jj_j2phi', 'jj_j2M', 'jj_j2NTracks', 'fat_jet_M', 'fat_jet_E', 'fat_jet_pt', 'fat_jet_eta', 'fat_jet_phi', 'fat_jet_D2', 'fat_jet_C2', 'fat_jet_ntrack', 'DSID', 'weight', 'WEIGHT', 'bTagSF', 'weight_lumi', 'weight_SFTrigger', 'weight_PUReweight', 'weight_MCEventWeight', 'weight_VZqqZbbWeight', 'weight_sumOfWeightsScaling', 'trkJetBTagSF','MET', 'isSignal', 'isResolvedPresel', 'isVBFevent', 'isVBFMergedOverlap', 'isVBFMergedPresel', 'Pass_MergHP_VBF_ZZSR', 'Pass_MergHP_VBF_WZSR', 'Pass_MergHPT_VBF_ZZSR', 'Pass_MergHPT_VBF_WZSR', 'Pass_MergHPU_VBF_ZZSR', 'Pass_MergHPU_VBF_WZSR', 'Pass_MergLP_VBF_ZZSR', 'Pass_MergLP_VBF_WZSR', 'Pass_MergLPT_VBF_ZZSR', 'Pass_MergLPT_VBF_WZSR', 'Pass_MergLPU_VBF_ZZSR', 'Pass_MergLPU_VBF_WZSR', 'Pass_MergHP_VBF_ZZZCR', 'Pass_MergLP_VBF_ZZZCR', 'Pass_MergHP_VBF_ZZTCR', 'Pass_MergLP_VBF_ZZTCR', 'isVBFResolvedOverlap', 'Pass_Res_VBF_ZZSR', 'Pass_Res_VBF_WZSR', 'Pass_Res_VBF_ZZZCR', 'Pass_Res_VBF_WZZCR', 'Pass_Res_VBF_ZZTCR', 'Pass_Res_VBF_WZTCR', 'isGGFMergedOverlap', 'isGGFMergedPresel', 'Pass_MergHP_GGF_ZZSR', 'Pass_MergHP_GGF_WZSR', 'Pass_MergHPT_GGF_ZZSR', 'Pass_MergHPT_GGF_WZSR', 'Pass_MergHPU_GGF_ZZSR', 'Pass_MergHPU_GGF_WZSR', 'Pass_MergLP_GGF_ZZSR', 'Pass_MergLP_GGF_WZSR', 'Pass_MergLPT_GGF_ZZSR', 'Pass_MergLPT_GGF_WZSR', 'Pass_MergLPU_GGF_ZZSR', 'Pass_MergLPU_GGF_WZSR', 'Pass_MergHP_GGF_ZZZCR', 'Pass_MergHPU_GGF_ZZZCR', 'Pass_MergHPT_GGF_ZZZCR', 'Pass_MergLP_GGF_ZZZCR', 'Pass_MergLPU_GGF_ZZZCR', 'Pass_MergLPT_GGF_ZZZCR', 'Pass_MergHP_GGF_ZZTCR', 'Pass_MergHPU_GGF_ZZTCR', 'Pass_MergHPT_GGF_ZZTCR', 'Pass_MergLP_GGF_ZZTCR', 'Pass_MergLPU_GGF_ZZTCR', 'Pass_MergLPT_GGF_ZZTCR', 'Pass_Res_GGF_ZZSR', 'Pass_Res_GGF_WZSR', 'Pass_Res_GGF_ZZZCR', 'Pass_Res_GGF_WZZCR', 'Pass_Res_GGF_ZZTCR', 'Pass_Res_GGF_WZTCR', 'Pass_ResT_GGF_ZZSR', 'Pass_ResT_GGF_WZSR', 'Pass_ResT_GGF_ZZZCR', 'Pass_ResT_GGF_WZZCR', 'Pass_ResT_GGF_ZZTCR', 'Pass_ResT_GGF_WZTCR', 'isMerged', 'isResolved', 'isCR', 'xsec', 'BR', 'FilterEff', 'kFact', 'ratio_merged', 'ratio_resolved', 'X_boosted_m', 'X_resolved_ZZ_m', 'X_resolved_WZ_m', 'truth_zv_mass', 'mjj', 'detajj', 'NJETS']


VariablesToPlot = [
    # 'lep1_pt','lep1_eta','lep2_pt','lep2_eta','Zll_mass','fatjet_pt','Zll_pt','truth_zv_mass'
]

InputDNNVariables = [

    # MERGED
    ['NJETS','l1_eta','l2_eta','l2_phi','l1_phi','ll_pt','fat_jet_eta','fat_jet_phi','fat_jet_pt','fat_jet_E','MET','l1_pt'],
    ['NJETS','l1_eta','l2_eta','l2_phi','l1_phi','ll_pt','fat_jet_eta','fat_jet_phi','fat_jet_pt','fat_jet_E','MET','l1_e'],
    ['NJETS','l1_eta','l2_eta','l2_phi','l1_phi','ll_pt','fat_jet_eta','fat_jet_phi','fat_jet_pt','fat_jet_E','MET','l2_pt'],
    ['NJETS','l1_eta','l2_eta','l2_phi','l1_phi','ll_pt','fat_jet_eta','fat_jet_phi','fat_jet_pt','fat_jet_E','MET','l2_e'],
    ['NJETS','l1_eta','l2_eta','l2_phi','l1_phi','ll_pt','fat_jet_eta','fat_jet_phi','fat_jet_pt','fat_jet_E','MET','fat_jet_D2'],
    ['NJETS','l1_eta','l2_eta','l2_phi','l1_phi','ll_pt','fat_jet_eta','fat_jet_phi','fat_jet_pt','fat_jet_E','MET','fat_jet_C2'],
    ['NJETS','l1_eta','l2_eta','l2_phi','l1_phi','ll_pt','fat_jet_eta','fat_jet_phi','fat_jet_pt','fat_jet_E','MET','ratio_merged'],
    ['NJETS','l1_eta','l2_eta','l2_phi','l1_phi','ll_pt','fat_jet_eta','fat_jet_phi','fat_jet_pt','fat_jet_E','MET','ratio_resolved'],
    ['NJETS','l1_eta','l2_eta','l2_phi','l1_phi','ll_pt','fat_jet_eta','fat_jet_phi','fat_jet_pt','fat_jet_E','MET','fat_jet_ntrack']

    # RESOLVED
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j2pt'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j1M'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j1pt'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','l1_pt'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','l2_pt'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','l2_e'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','ratio_resolved'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','l1_e'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j2NTracks'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j1NTracks'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j2M'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','ratio_merged'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','detajj'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j1eta'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j2eta'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j2phi'],
#    ['NJETS','l2_eta','l1_eta','l1_phi','l2_phi','ll_pt','jj_eta','jj_phi','jj_pt','MET','jj_j1phi']   
        ]

ScanParams = {
    "Width":[64]
    ,"BatchSize": [1024]
    ,"Depth":[4]
    ,"LearningRate": [0.0003]
    ,"VarSet": [ i for i in range(0,len(InputDNNVariables))]

}

#FixedParams
Params = {
    "WeightInitialization": "'normal'",
    "Epochs": 200,
    "Optimizer": "Adam"
}

# Apply dropout when building the NN(see ModelBuilder.py)
Dropout       = 0.2 #0.2-->20% of the nodes will be ommitted. Put a negative value if you want to switch off the dropout


def getScanParamCombos(setupClient):
    PS=Permutator(setupClient.ScanParams)
    Combos=PS.Permutations()
    return Combos

def printScanParamCombos(setupClient):
    Combos = getScanParamCombos(setupClient)
    print ("Parameter Scan: ", len(Combos), "possible combinations.")
    for j in range(0,len(Combos)):
        print (j,":",Combos[j])

def pickModelParamSet(setupClient):
    i=-1
    Combos = getScanParamCombos(setupClient)
    if setupClient.HyperParamSet >=0:
        i=int(setupClient.HyperParamSet)

    if i<0:
        random.seed()
        i=int(round(len(Combos)*random.random()))

    print ('{:<45} {:<15}'.format('Picked combination',Fore.GREEN + str(i) + (' Manualy' if setupClient.HyperParamSet >=0 else ' Randomly')) )
    if i==len(Combos):
        i=i-1

    for k in Combos[i]:
        setupClient.Params[k]=Combos[i][k]


    ModelName=setupClient.modelPrefixName

    for param in ScanParams.keys():
        val=str(setupClient.Params[param]).replace('"',"")
        if param=='VarSet':
            ModelName+="_VarSet"+val.replace("'","")
        else:
            ModelName+="_"+val.replace("'","")

    setupClient.ModelParamCombo = ModelName
    print ('{:<45} {:<15}'.format('Model Name',Fore.GREEN+ModelName))
    ModelSavePath = os.path.join(setupClient.OutBaseDir, ModelName)
    # ModelSavePath will point to OutBaseDir+ModelName
    setupClient.ModelSavePath = ModelSavePath
    print ('{:<45} {:<15}'.format('ModelOuput directory',Fore.GREEN + setupClient.ModelSavePath ), checkCreateDir(setupClient.ModelSavePath) )

    setupClient.HyperParamSet = i
    setupClient.VarSet = setupClient.Params['VarSet']
