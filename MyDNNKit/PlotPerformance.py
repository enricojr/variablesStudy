import sys,os,time,string,math

from sklearn.metrics import roc_curve, auc, roc_auc_score, classification_report, confusion_matrix
import pandas as pd
import seaborn as sns

import numpy as np
np.random.seed(123)

from matplotlib import pyplot as plt
from skhep.visual import MplPlotter as skh_plt
from matplotlib.patches import Rectangle

def asymSignificance(hsig,hbkg):
    asymSig = 0
    for i,S in enumerate(hsig):
        B = hbkg[i]
        #print(S,B)
        SoB = 0
        if B>0:
            SoB = S/B
        SpB = S+B
        asymSig += 2.0*(SpB * math.log(1+SoB) - S)

    return math.sqrt(asymSig)


def create_upDNNcut_SigBkgDF(ix_test,ix_train,scoreCut):

    Df_Sig    = pd.concat( [ ix_test.loc[(ix_test.isSignal == 1) & (ix_test.DNN_Score > scoreCut)], ix_train.loc[(ix_train.isSignal == 1) & (ix_train.DNN_Score > scoreCut)] ] )
    DF_Bkg    = pd.concat( [ ix_test.loc[(ix_test.isSignal == 0) & (ix_test.DNN_Score > scoreCut)], ix_train.loc[(ix_train.isSignal == 0) & (ix_train.DNN_Score > scoreCut)] ] )

    return Df_Sig,DF_Bkg

def create_upDNNcut_SigBkgDF_SR(ix_test,ix_train,scoreCut):

    Df_Sig    = pd.concat( [ ix_test.loc[(ix_test.isSignal == 1) & (ix_test.DNN_Score > scoreCut) & (ix_test.isCR==0)], ix_train.loc[(ix_train.isSignal == 1) & (ix_train.DNN_Score > scoreCut) & (ix_train.isCR==0) ] ] )
    DF_Bkg    = pd.concat( [ ix_test.loc[(ix_test.isSignal == 0) & (ix_test.DNN_Score > scoreCut) & (ix_test.isCR==0)], ix_train.loc[(ix_train.isSignal == 0) & (ix_train.DNN_Score > scoreCut) & (ix_train.isCR==0) ] ] )

    return Df_Sig,DF_Bkg

def create_downDNNcut_SigBkgDF(ix_test,ix_train,scoreCut):

    Df_Sig    = pd.concat( [ ix_test.loc[(ix_test.isSignal == 1) & (ix_test.DNN_Score < scoreCut)], ix_train.loc[(ix_train.isSignal == 1) & (ix_train.DNN_Score < scoreCut)] ] )
    DF_Bkg    = pd.concat( [ ix_test.loc[(ix_test.isSignal == 0) & (ix_test.DNN_Score < scoreCut)], ix_train.loc[(ix_train.isSignal == 0) & (ix_train.DNN_Score < scoreCut)] ] )

    return Df_Sig,DF_Bkg



def drawParameterCorrelationMatrix():

    resultsPath = 'Test_MixPD_MergedggF_ggH1000/llqqDNN_128_2048_4_0.003_VarSet2/'
    ix_test = pd.read_pickle(resultsPath+'ResultsTestPD.pkl')
    ix_train = pd.read_pickle(resultsPath+'ResultsTrainPD.pkl')

    DF_Sig_Merged_ggF    = ix_test.loc[(ix_test.isSignal == 1)]
    DF_Bkg_Merged_ggF    = ix_test.loc[(ix_test.isSignal == 0)]
    # DF_Sig_Merged_ggF    = pd.concat( [ix_test.loc[(ix_test.isSignal == 1)],ix_train.loc[(ix_train.isSignal == 1)]] )
    # DF_Bkg_Merged_ggF    = pd.concat( [ix_test.loc[(ix_test.isSignal == 0)],ix_train.loc[(ix_train.isSignal == 0)]] )

    varList = ['l1_e', 'l1_pt', 'l1_eta', 'l1_phi', 'l2_e','l2_pt', 'l2_eta', 'l2_phi']
    # varList = ['l1_e', 'l1_pt', 'l1_eta', 'l1_phi', 'l2_e','l2_pt', 'l2_eta', 'l2_phi', 'll_m', 'll_pt','fat_jet_E', 'fat_jet_pt', 'fat_jet_eta', 'fat_jet_phi','NJETS']
    df_sig_final = DF_Sig_Merged_ggF[varList]
    df_bkg_final = DF_Bkg_Merged_ggF[varList]


    plt.figure(figsize=(12,8))
    cmap="YlGnBu"

    # df_SplusB = pd.concat([df_sig_final,df_bkg_final])
    #
    # corr = df_SplusB.corr()
    # ax = sns.heatmap(df_SplusB,xticklabels=corr.columns.values,yticklabels=corr.columns.values,annot=True,vmin=-1.1, vmax=1.1,linewidths=0.5,fmt='0.2f',cmap=cmap)
    # ax.set_xticklabels(ax.get_xticklabels(),rotation=40)
    # ax.set_yticklabels(ax.get_yticklabels(),rotation=0)
    # plt.title("Parameter Correlation Matrix")
    # plt.savefig(resultsPath+"InputsCorrelationMatrix_SpluB.png")
    # # plt.show()
    # plt.clf()


    corr = df_sig_final.corr()
    ax = sns.heatmap(df_sig_final,xticklabels=corr.columns.values,yticklabels=corr.columns.values,annot=True,vmin=-1.1, vmax=1.1,linewidths=0.5,fmt='0.2f',cmap=cmap)
    ax.set_xticklabels(ax.get_xticklabels(),rotation=40)
    ax.set_yticklabels(ax.get_yticklabels(),rotation=0)
    plt.title("Parameter Correlation Matrix")
    plt.savefig(resultsPath+"InputsCorrelationMatrix_Signal.png")
    # plt.show()
    plt.clf()


    corr = df_bkg_final.corr()
    ax = sns.heatmap(df_bkg_final,xticklabels=corr.columns.values,yticklabels=corr.columns.values,annot=True,vmin=-1.1, vmax=1.1,linewidths=0.5,fmt='0.2f',cmap=cmap)
    ax.set_xticklabels(ax.get_xticklabels(),rotation=40)
    ax.set_yticklabels(ax.get_yticklabels(),rotation=0)
    plt.title("Parameter Correlation Matrix")
    plt.savefig(resultsPath+"InputsCorrelationMatrix_Background.png")
    # plt.show()
    plt.clf()




def plotResults():
    # resultsPath = 'Test_MixPD_MergedggF_ggH1000/llqqDNN_128_2048_4_0.003_VarSet0/'
    resultsPath = 'Test_MixPD_MergedggF_ggH1000_HyperParamScan_MAXAUC/llqqDNN_128_1024_3_0.0003_VarSet0/'
    ix_test = pd.read_pickle(resultsPath+'ResultsTestPD.pkl')
    ix_train = pd.read_pickle(resultsPath+'ResultsTrainPD.pkl')
    sns.set(style="whitegrid")
    # Initial S/B
    # print('nRawEventsTest',  ix_test.shape[0])
    # print('nRawEventsTrain', ix_train.shape[0])
    # print('nWeightedEventsTest',ix_test['weight'].sum())
    # print('nWeightedEventsTrain',ix_train['weight'].sum())
    # print('')

    ## Create Initial Signal and Background samples
    DF_Sig_Merged_ggF    = pd.concat( [ix_test.loc[(ix_test.isSignal == 1)],ix_train.loc[(ix_train.isSignal == 1)]] )
    DF_Bkg_Merged_ggF    = pd.concat( [ix_test.loc[(ix_test.isSignal == 0)],ix_train.loc[(ix_train.isSignal == 0)]] )
    initSig = DF_Sig_Merged_ggF['weight'].sum()
    initBkg = DF_Bkg_Merged_ggF['weight'].sum()
    print('initial SigYield', initSig)
    print('initial BkgYield', initBkg)
    initSoB = initSig/math.sqrt(initSig+initBkg)
    print('initial S/sqrt(S+B) =',initSoB)
    # plot S and B ZV mass
    bins=np.linspace(0,3000, 30)
    hbkg, b2,p2 = plt.hist(DF_Bkg_Merged_ggF.reco_zv_mass_llJ,  bins=bins, histtype='stepfilled', lw=2, alpha=0.5,  label=[r'Background'], weights=[ DF_Bkg_Merged_ggF.weight] )
    hsig, b1,p1 = plt.hist(DF_Sig_Merged_ggF.reco_zv_mass_llJ,  bins=bins, histtype='step',       lw=2, alpha=1.0,  label=[r'Signal'],weights=[ DF_Sig_Merged_ggF.weight] )
    plt.ylabel('Entries')
    plt.xlabel('llJ Reco Mass [GeV]')
    plt.yscale('log')
    plt.legend(loc="best")
    plt.savefig(resultsPath+"reco_zv_mass_llJ_default.png")
    # plt.show()
    plt.clf()
    initAsymSig = asymSignificance(hsig,hbkg)

    ### Scan the score
    scanRange = np.arange(0, 1, 0.05)
    dnnSsqrtB = []
    asymSig = []
    for score in scanRange:
        DF_Sig_Merged_ggF_dnn, DF_Bkg_Merged_ggF_dnn    = create_upDNNcut_SigBkgDF(ix_test,ix_train,score)
        dnnSigYield = DF_Sig_Merged_ggF_dnn['weight'].sum()
        dnnBkgYield = DF_Bkg_Merged_ggF_dnn['weight'].sum()
        dnnSsqrtB += [dnnSigYield/math.sqrt(dnnSigYield+dnnBkgYield)]

        hsig, b1,p1 = plt.hist(DF_Sig_Merged_ggF_dnn.reco_zv_mass_llJ,  bins=bins, histtype='step',       lw=2, alpha=1.0,  label=[r'Signal'],weights=[ DF_Sig_Merged_ggF_dnn.weight] )
        # print(DF_Bkg_Merged_ggF_dnn.reco_zv_mass_llJ)
        hbkg, b2,p2 = plt.hist(DF_Bkg_Merged_ggF_dnn.reco_zv_mass_llJ,  bins=bins, histtype='stepfilled', lw=2, alpha=0.5,  label=[r'Background'], weights=[ DF_Bkg_Merged_ggF_dnn.weight] )
        plt.clf()

        asymSig += [asymSignificance(hsig,hbkg)]

    a = np.full( (len(scanRange), 1), initAsymSig )
    b = np.full( (len(scanRange), 1), initSoB )

    plt.plot(scanRange,dnnSsqrtB,'bo', label='Default+DNN S/$\sqrt{S+B}$', markersize=3)
    plt.plot(scanRange, b, color='blue', lw=1, linestyle='--',label='Default S/$\sqrt{S+B}$')
    plt.plot(scanRange,asymSig,'rx', label='Default+DNN Asymptotic', markersize=3)
    plt.plot(scanRange, a, color='red', lw=1, linestyle='--',label='Default Asymptotic')
    plt.ylabel('Significance')
    plt.xlabel('DNN Score')
    plt.legend(loc="best",fontsize=9)
    plt.xlim([-0.05, 1.0])
    plt.savefig(resultsPath+"significance_comparisons.png")
    plt.show()
    plt.clf()

    # Apply the DNN_Score cut
    scoreCut = 0.85
    DF_Sig_Merged_ggF_dnn, DF_Bkg_Merged_ggF_dnn    = create_upDNNcut_SigBkgDF(ix_test,ix_train,scoreCut)
    dnnSig = DF_Sig_Merged_ggF_dnn['weight'].sum()
    dnnBkg = DF_Bkg_Merged_ggF_dnn['weight'].sum()
    print('dnn SigYield', dnnSig )
    print('dnn BkgYield', dnnBkg )
    print('dnn S/sqrt(S+B) =', dnnSig/math.sqrt(dnnSig+dnnBkg) )
    print('')
    print ('initial asymSignificance',initAsymSig)

    hsig, b1,p1 = plt.hist(DF_Sig_Merged_ggF_dnn.reco_zv_mass_llJ,  bins=bins, histtype='step',       lw=2, alpha=1.0,  label=[r'Signal DNN_Score>'+str(scoreCut)],weights=[ DF_Sig_Merged_ggF_dnn.weight ]  )
    hbkg, b2,p2 = plt.hist(DF_Bkg_Merged_ggF_dnn.reco_zv_mass_llJ,  bins=bins, histtype='stepfilled', lw=2, alpha=0.5,  label=[r'Background  DNN_Score>'+str(scoreCut)], weights=[ DF_Bkg_Merged_ggF_dnn.weight] )
    plt.ylabel('Entries')
    plt.xlabel('llJ Reco Mass [GeV]')
    plt.yscale('log')
    plt.legend(loc="best")
    plt.savefig(resultsPath+"reco_zv_mass_llJ_afterDNNCut.png")
    # plt.show()
    plt.clf()
    print ('dnn asymSignificance',asymSignificance(hsig,hbkg))
    #######################################################

    print('')
    print('---- Signal Region----')

    DF_Sig_Merged_ggF_SR    = pd.concat( [ix_test.loc[(ix_test.isSignal == 1) & (ix_test.isCR == 0) ], ix_train.loc[(ix_train.isSignal == 1) & (ix_train.isCR == 0) ]] )
    DF_Bkg_Merged_ggF_SR    = pd.concat( [ix_test.loc[(ix_test.isSignal == 0) & (ix_test.isCR == 0) ], ix_train.loc[(ix_train.isSignal == 0) & (ix_train.isCR == 0) ]] )
    print('initial SigYield in SR', DF_Sig_Merged_ggF_SR['weight'].sum())
    print('initial BkgYield in SR', DF_Bkg_Merged_ggF_SR['weight'].sum())
    initSoB_SR = DF_Sig_Merged_ggF_SR['weight'].sum()/math.sqrt(DF_Bkg_Merged_ggF_SR['weight'].sum())
    print('initial S/sqrt(B) in SR =',initSoB_SR)

    hsig, b1,p1 = plt.hist(DF_Sig_Merged_ggF_SR.reco_zv_mass_llJ,  bins=bins, histtype='step',       lw=2, alpha=1.0,  label=[r'Signal SR'],weights=[ DF_Sig_Merged_ggF_SR.weight ]  )
    hbkg, b2,p2 = plt.hist(DF_Bkg_Merged_ggF_SR.reco_zv_mass_llJ,  bins=bins, histtype='stepfilled', lw=2, alpha=0.5,  label=[r'Background SR'], weights=[ DF_Bkg_Merged_ggF_SR.weight] )
    plt.ylabel('Entries')
    plt.xlabel('llJ Reco Mass [GeV]')
    plt.yscale('log')
    plt.legend(loc="best")
    # plt.show()
    plt.clf()
    initAsymSig_SR = asymSignificance(hsig,hbkg)
    print ('initial asymSignificance in SR',)


    ### Scan the score in the SR region
    scanRange = np.arange(0, 1, 0.05)
    dnnSsqrtB = []
    asymSig = []
    for score in scanRange:
        DF_Sig_Merged_ggF_SR_dnn, DF_Bkg_Merged_ggF_SR_dnn    = create_upDNNcut_SigBkgDF_SR(ix_test,ix_train,score)
        dnnSigYield = DF_Sig_Merged_ggF_SR_dnn['weight'].sum()
        dnnBkgYield = DF_Bkg_Merged_ggF_SR_dnn['weight'].sum()
        dnnSsqrtB += [dnnSigYield/math.sqrt(dnnSigYield+dnnBkgYield)]

        hsig, b1,p1 = plt.hist(DF_Sig_Merged_ggF_SR_dnn.reco_zv_mass_llJ,  bins=bins, histtype='step',       lw=2, alpha=1.0,  label=[r'Signal in SR'],weights=[ DF_Sig_Merged_ggF_SR_dnn.weight] )
        hbkg, b2,p2 = plt.hist(DF_Bkg_Merged_ggF_SR_dnn.reco_zv_mass_llJ,  bins=bins, histtype='stepfilled', lw=2, alpha=0.5,  label=[r'Background in SR'], weights=[ DF_Bkg_Merged_ggF_SR_dnn.weight] )
        plt.clf()

        asymSig += [asymSignificance(hsig,hbkg)]

    a = np.full( (len(scanRange), 1), initAsymSig_SR )
    b = np.full( (len(scanRange), 1), initSoB_SR )

    plt.plot(scanRange,dnnSsqrtB,'bo', label='Default+DNN S/$\sqrt{S+B}$', markersize=3)
    plt.plot(scanRange, b, color='blue', lw=1, linestyle='--',label='Default S/$\sqrt{S+B}$')
    plt.plot(scanRange,asymSig,'rx', label='Default+DNN Asymptotic', markersize=3)
    plt.plot(scanRange, a, color='red', lw=1, linestyle='--',label='Default Asymptotic')
    plt.ylabel('Significance SR')
    plt.xlabel('DNN Score')
    plt.legend(loc="best",fontsize=9)
    plt.xlim([-0.05, 1.0])
    plt.savefig(resultsPath+"significance_comparisons_SR.png")
    plt.show()
    plt.clf()


    DF_Sig_Merged_ggF_SR_dnn = DF_Sig_Merged_ggF_SR.loc[ DF_Sig_Merged_ggF_SR.DNN_Score > scoreCut ]
    DF_Bkg_Merged_ggF_SR_dnn = DF_Bkg_Merged_ggF_SR.loc[ DF_Bkg_Merged_ggF_SR.DNN_Score > scoreCut ]
    print('SigYield in SR after DNN', DF_Sig_Merged_ggF_SR_dnn['weight'].sum())
    print('BkgYield in SR after DNN', DF_Bkg_Merged_ggF_SR_dnn['weight'].sum())
    initAsymSig_SR = DF_Sig_Merged_ggF_SR_dnn['weight'].sum()/math.sqrt(DF_Bkg_Merged_ggF_SR_dnn['weight'].sum())
    print('S/sqrt(B) in SR  after DNN =',initAsymSig_SR)

    hsig, b1,p1 = plt.hist(DF_Sig_Merged_ggF_SR_dnn.reco_zv_mass_llJ,  bins=bins, histtype='step',       lw=2, alpha=1.0,  label=[r'Signal SR  DNN_Score>'+str(scoreCut)],weights=[ DF_Sig_Merged_ggF_SR_dnn.weight ]  )
    hbkg, b2,p2 = plt.hist(DF_Bkg_Merged_ggF_SR_dnn.reco_zv_mass_llJ,  bins=bins, histtype='stepfilled', lw=2, alpha=0.5,  label=[r'Background SR  DNN_Score>'+str(scoreCut)], weights=[ DF_Bkg_Merged_ggF_SR_dnn.weight] )
    plt.ylabel('Entries')
    plt.xlabel('llJ Reco Mass [GeV]')
    plt.yscale('log')
    plt.legend(loc="best")
    # plt.show()
    plt.clf()
    print ('SR dnn asymSignificance',asymSignificance(hsig,hbkg))



    ### Look at the fat jet mass before and after the Dnn cut
    bins1 =np.linspace(0,800, 40)
    lw=1
    plt.hist(DF_Sig_Merged_ggF.fat_jet_M,  bins=bins1, histtype='step', lw=lw, color='blue',  label=[r'Signal'],density=True)#,weights=[ DF_Sig_Merged_ggF.weight ]  )
    plt.hist(DF_Bkg_Merged_ggF.fat_jet_M,  bins=bins1, histtype='step', lw=lw, color='red', label=[r'Background'],density=True)#, weights=[ DF_Bkg_Merged_ggF.weight] )
    plt.hist(DF_Sig_Merged_ggF_dnn.fat_jet_M,  bins=bins1, histtype='step', lw=lw,linestyle='--',color='blue',  label=[r'Signal DNN>'+str(scoreCut)],density=True)# ,weights=[ DF_Sig_Merged_ggF_dnn.weight ]  )
    plt.hist(DF_Bkg_Merged_ggF_dnn.fat_jet_M,  bins=bins1, histtype='step', lw=lw, linestyle='--',color='red', label=[r'Background DNN>'+str(scoreCut)],density=True)#, weights=[ DF_Bkg_Merged_ggF_dnn.weight] )
    plt.ylabel('Norm. Entries')
    plt.xlabel('FatJet Mass [GeV]')
    plt.yscale('log')
    plt.legend(loc="best")
    plt.savefig(resultsPath+"fat_jet_m_default_dnn.png")
    plt.show()
    plt.clf()






def plotROCs():
    modelName = 'llqqDNN_100_64_2_0'

    roc_compare = [
        ['Model_All_TestOn_1600','DNN trained at all masses, evaluated at $M_{x}=1600$'],
        # ['Train1000','DNN trained at mass=1000 only'],
        ['Model_Not1600_TestOn_1600', 'DNN (w/o mass=1600), evaluated at $M_{x}=1600$'],
        # ['TrainAll_Test1000','DNN trained at all masses'],
        # ['TrainNot1000_Test1000', 'NN (w/o mass=1000)'],
    ]
    # bins=np.linspace(0, 1, 100)
    fig = plt.figure()
    ax = fig.gca()
    ax.text(0.16, 0.17, r'$X_{spin\ 0} \rightarrow ZV \rightarrow \ell\ell qq$  -  Merged Analysis', fontsize=10)
    # for roc in roc_compare:
    #     tpr = np.load(os.path.join(roc[0],modelName,"tpr_AtMx1600.npy"))
    #     fpr = np.load(os.path.join(roc[0],modelName,"fpr_AtMx1600.npy"))
    #     plt.plot(fpr,tpr,'--',lw=1, label=roc[1])
    tpr = np.load(os.path.join(roc_compare[0][0],modelName,"tpr_AtMx1600.npy"))
    fpr = np.load(os.path.join(roc_compare[0][0],modelName,"fpr_AtMx1600.npy"))
    plt.plot(fpr,tpr,'--',lw=2, label=roc_compare[0][1])
    tpr2 = np.load(os.path.join(roc_compare[1][0],modelName,"tpr_AtMx1600.npy"))
    fpr2 = np.load(os.path.join(roc_compare[1][0],modelName,"fpr_AtMx1600.npy"))
    plt.plot(fpr2,tpr2,':',lw=2, label=roc_compare[1][1])


    plt.legend(loc='best',frameon=False)
    # plt.xlim([-0.01, 1.0])
    plt.ylim([-0.02, 1.03])
    plt.xlabel("Background Efficiency")
    # plt.yscale('log')
    # plt.xscale('log')
    plt.ylabel("Signal Efficiency")
    # plt.show()
    plt.savefig("Compare_ROCs.pdf")
    plt.clf()


def plotAUCs():
    modelName = 'llqqDNN_100_60_2_0'
    massPoints = [700,1000,2000,3000]
    roc_auc_afterDilepton = []
    roc_auc_afterggFMerged = []

    for mass in massPoints:
        fpr_w    = np.load(os.path.join('Out_AfterDilepton_TrainggF'+str(mass)+'_FullStat_1FatJet',modelName,"fpr_w.npy"))
        tpr_w    = np.load(os.path.join('Out_AfterDilepton_TrainggF'+str(mass)+'_FullStat_1FatJet',modelName,"tpr_w.npy"))
        roc_auc  = auc(fpr_w, tpr_w,reorder=True)
        roc_auc_afterDilepton += [roc_auc]

        if mass!=3000:
            plt.plot(fpr_w, tpr_w, lw=2, label='Mass point '+str(mass) )

    plt.legend(loc='best',frameon=False)
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.title('ROC curves for Signal vs Background')
    plt.legend(loc="lower right")
    plt.savefig("Compare_ROCs_AfterDilepton.pdf")
    plt.clf()

    for mass in massPoints:
        fpr_w    = np.load(os.path.join('Out_AfterggFMerged_TrainggF'+str(mass)+'_FullStat_1FatJet',modelName,"fpr_w.npy"))
        tpr_w    = np.load(os.path.join('Out_AfterggFMerged_TrainggF'+str(mass)+'_FullStat_1FatJet',modelName,"tpr_w.npy"))
        roc_auc  = auc(fpr_w, tpr_w,reorder=True)
        roc_auc_afterggFMerged += [roc_auc]
        if mass!=3000:
            plt.plot(fpr_w, tpr_w, lw=2, label='Mass point '+str(mass) )

    plt.legend(loc='best',frameon=False)
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.title('ROC curves for Signal vs Background')
    plt.legend(loc="lower right")
    plt.savefig("Compare_ROCs_AfterggF.pdf")
    plt.clf()

    plt.plot(massPoints, roc_auc_afterDilepton, 'ro-', label='After Dilepton Selection')
    plt.plot(massPoints, roc_auc_afterggFMerged, 'bx--',label='After ggF Merged Selection')
    plt.legend(loc='best',frameon=False)
    plt.xlabel("Mass point [GeV]")
    plt.ylabel("AUC")
    plt.savefig("Compare_AUCs.pdf")
    plt.clf()



def plotScores():
    isBlindAnalysis = True
    modelName = 'llqqDNN_100_60_2_0'
    outDirAfterDilep = ['Out_AfterDilepton_TrainggF1000_FullStat_1FatJet',
    'Out_AfterDilepton_TrainggF2000_FullStat_1FatJet',
    'Out_AfterDilepton_TrainggF3000_FullStat_1FatJet',
    'Out_AfterDilepton_TrainggF700_FullStat_1FatJet']

    outDirAfterggF = ['Out_AfterggFMerged_TrainggF1000_FullStat_1FatJet',
    'Out_AfterggFMerged_TrainggF2000_FullStat_1FatJet',
    'Out_AfterggFMerged_TrainggF3000_FullStat_1FatJet',
    'Out_AfterggFMerged_TrainggF700_FullStat_1FatJet']


    for idir in outDirAfterDilep:
    # for idir in outDirAfterggF:
        if isBlindAnalysis==False:
            yhat_data         = np.load(os.path.join(idir,modelName,"yhat_data.npy"))

        yhat_train_signal     = np.load(os.path.join(idir,modelName,"yhat_train_signal.npy"))
        yhat_train_background = np.load(os.path.join(idir,modelName,"yhat_train_background.npy"))

        yhat_test_signal      = np.load(os.path.join(idir,modelName,"yhat_test_signal.npy"))
        yhat_test_background  = np.load(os.path.join(idir,modelName,"yhat_test_background.npy"))

        bins=np.linspace(0,1, 50)
        plt.hist(yhat_train_signal,     bins=bins, histtype='step',       lw=2, alpha=0.5, color='deepskyblue', label='TrainSignal',    normed=True)
        plt.hist(yhat_test_signal,      bins=bins, histtype='stepfilled', lw=2, alpha=0.5, color='turquoise',   label='TestSignal',     normed=True)
        plt.hist(yhat_train_background, bins=bins, histtype='step',       lw=2, alpha=0.5, color='deeppink',    label='TrainBackground',normed=True)
        plt.hist(yhat_test_background,  bins=bins, histtype='stepfilled', lw=2, alpha=0.5, color='plum',        label='TestBackground', normed=True)
        if isBlindAnalysis==False:
            skh_plt.hist(yhat_data,  bins=bins, errorbars=True, histtype='marker',label='Data', color='black',normed=True)
        plt.legend(loc="upper center")
        plt.ylabel('Norm. Entries')
        plt.xlabel('DNN score')
        plt.yscale('log')
        plt.savefig(idir+'/'+modelName+"/MC_TrainTest_Score.pdf")
        # plt.show()
        plt.clf()



def plotMultiAUC(mass):
    topDir = 'Test_MixPD_MergedggF_ggH1000_HyperParamScan'
    # topDir = 'Train_S'+mass+'_Test_S'+mass
    listFiles = os.listdir(topDir)

    plt.clf()
    fig, ax = plt.subplots()

    aucsList = []
    nameList = []

    for i,combo in enumerate(listFiles):
        if not os.path.isfile(topDir+'/'+combo+'/AUC_w.npy'):
            continue
        aucs_w = np.load(topDir+'/'+combo+'/AUC_w.npy')
        aucsList.append(aucs_w.item(0))
        cname = combo.split('_',1)[1]
        nameList += [cname]
        plt.plot(cname,aucs_w,'bo', label='auc', markersize=3)

    # print(aucsList)

    aucsNewArray = np.asarray(aucsList)
    print('Combination with max AUC',nameList[np.argmax(aucsNewArray)],' AUC=',np.amax(aucsNewArray) )
    print(np.argmax(aucsNewArray))
    print(np.amax(aucsNewArray))


    plt.ylabel('AUC')
    plt.xticks(rotation=90,fontsize=6)
    fig.tight_layout()
    someX, someY = np.argmax(aucsNewArray), np.amax(aucsNewArray)
    ax.add_patch(Rectangle((someX-0.5, someY-0.001), 1, 0.0015,clip_on=False, alpha=0.3, facecolor='r',edgecolor='r'))
    plt.savefig('MultiAUC_comparison.png')
    plt.show()


def plotMultiROC(mass):
    topDir = 'Train_S'+mass+'_Test_S'+mass
    listFiles = os.listdir(topDir)

    plt.clf()
    for combo in listFiles:
        if '.png' in combo:
            continue

        splitCombo = combo.split('_')
        width = splitCombo[2]
        batchsize = splitCombo[3]
        varSet = splitCombo[4]
        depth = splitCombo[5]

        if varSet!='1':
            continue

        tpr = np.load(os.path.join(topDir,combo,"tpr_w.npy"))
        fpr = np.load(os.path.join(topDir,combo,"fpr_w.npy"))

        if depth=='2':
            plt.plot(fpr,tpr,'--',lw=1, label=combo)
        elif depth=='3':
            plt.plot(fpr,tpr,'-',lw=1, label=combo)
        elif depth=='4':
            plt.plot(fpr,tpr,':',lw=1, label=combo)

    plt.title('ggF '+mass+' GeV')
    plt.ylabel('Signal Efficiency')
    plt.xlabel('Background Efficiency')
    plt.legend(loc='best',ncol=2,fontsize=7)
    plt.savefig(topDir+"/ROC_varset2_"+mass+".png")




def plotFeatureSetImpact(mass):
    topDir = 'Train_S'+mass+'_VarSetScan_Test_S'+mass
    listFiles = os.listdir(topDir)

    auc = []
    name= []

    for combo in listFiles:
        if '.png' in combo:
            continue
        perfDF  = pd.read_csv(topDir+'/'+combo+'/Performance.csv')
        splitCombo = combo.split('_')
        width = splitCombo[2]
        batchsize = splitCombo[3]
        varSet = splitCombo[4]
        depth = splitCombo[5]
        perfDF['Combo'] = combo


        if varSet=='0':
            name +=['Njets']
        elif varSet=='1':
            name +=['+l1 E,Pt']
        elif varSet=='2':
            name +=['+l1 eta,phi']
        elif varSet=='3':
            name +=['+l2 E,Pt']
        elif varSet=='4':
            name +=['+l2 eta,phi']
        elif varSet=='5':
            name +=['+ll M,Pt']
        elif varSet=='6':
            name +=['+FJet E,Pt']
        elif varSet=='7':
            name +=['+FJet eta,phi']

        auc += [perfDF['ROC_AUC_Weighted']]


    plt.clf()
    # fig, ax = plt.subplots()
    # plt.plot(range(0,8),auc,'b-', label='Variable Set Scan', linewidth=2)
    plt.bar(range(0,8),auc,color='orange')
    plt.legend(loc="best")
    plt.ylabel('AUC')
    plt.xticks(range(0,8),name, rotation=30,fontsize=8)
    plt.title('Input features impact on AUC')
    plt.ylim([0.4, 1.05])
    # fig.tight_layout()
    # plt.show()
    plt.savefig(topDir+"/VarSetImpact_"+mass+".png")
    # plt.yscale('log')





if __name__ == '__main__':
    MassPoints = ['1000']
    # MassPoints = ['700','1000','2000']
    # plotROCs()
    # plotAUCs()
    # plotScores()
    plotResults()
    # drawParameterCorrelationMatrix()

    # for mass in MassPoints:
        # plotMultiAUC(mass)
        # plotMultiROC(mass)
        # plotFeatureSetImpact(mass)

    # plotMultiAUC('2000') ## combo 22 llqqDNN_200_64_2048_1_3
    # plotMultiAUC('1000') ## combo 19 llqqDNN_200_64_2048_1_2
    # plotMultiAUC('700') ## combo 20 llqqDNN_200_128_2048_1_2
