import root_pandas as rp

import numpy as np
import pandas as pd

import glob
from root_numpy import root2array, list_branches, array2root

from NNTreeMakerHelper import *


### DF with Score from MLTool ###
#DF_path = '/data3/agiannini/DBLCode_19nov19/MLTool/MyDNNKit/output_RNN_ForVBFggF1000_19feb19_testingModel/llqqDNN_32_512_2_0.0003_VarSet0/'
DF_path = '/data3/agiannini/DBLCode_19nov19/MLTool/MyDNNKit_04mar19/MyDNNKit/output_RNN_ForVBFggF1000_testingModel_04mar19/llqqDNN_32_512_2_0.0003_VarSet0/'

#VT_path = '/data2/lavorgna/Samples/Tag32_06_mc16a/'
VT_path = '/data2/lavorgna/Samples/Tag32_06_mc16a_mergedTagg/'

runForVBFggF = False
runForBkg    = True
### end config ###################



name_fields = np.load( DF_path + 'rootBranchSubSample.npy' )

#print name_fields

#name_fields = np.append( name_fields, ['ggFVBF'] )
#name_fields = np.append( name_fields, ['NNScore'] )
#name_fields = np.append( name_fields, ['NNScore'] )

DF_test  = pd.DataFrame( np.load( DF_path + 'ResultsTestPD.npy' ) , columns=name_fields )
DF_train = pd.DataFrame( np.load( DF_path + 'ResultsTrainPD.npy' ), columns=name_fields )

#print DF_test
#print DF_test.shape
#print name_fields.shape

rp.to_root( DF_test, 'NNFlatTree_TestSample.root', key='NNFlatTree' )

DF_test_VBF = DF_test[ DF_test['ggFVBF']==1 ]
DF_test_ggF = DF_test[ DF_test['ggFVBF']==0 ]

DF_train_VBF = DF_train[ DF_train['ggFVBF']==1 ]
DF_train_ggF = DF_train[ DF_train['ggFVBF']==0 ]

rp.to_root( DF_test_VBF, 'NNFlatTree_VBF1000.root', key='NNFlatTree' )
rp.to_root( DF_test_ggF, 'NNFlatTree_ggF1000.root', key='NNFlatTree' )



### Vectorial Tree from Reader ###
if runForVBFggF:
    VT_name = VT_path + 'VBF_H1000.root'
    DF_VT_VBF1000 = pd.DataFrame( root2array(VT_name, 'Nominal', branches=list_branches(VT_name) ) )
    NNTreeMakerForTestTrain( VT_name, 'VBFH1000', DF_test_VBF, DF_train_VBF )
    
    VT_name = VT_path + 'ggF_H1000.root'
    DF_VT_ggF1000 = pd.DataFrame( root2array(VT_name, 'Nominal', branches=list_branches(VT_name) ) )
    NNTreeMakerForTestTrain( VT_name, 'ggFH1000', DF_test_ggF, DF_train_ggF )



### add NNScore to VT from Reader for bkg (only Test DF) ###
Samples = [
    #'ZeeB_Sh221', 'ZeeC_Sh221', 'ZeeL_Sh221', 'Zee_Sh221', 
    #'ZmumuB_Sh221', 'ZmumuC_Sh221', 'ZmumuL_Sh221', 'Zmumu_Sh221', 'WqqWlv_Sh221', 'WqqZll_Sh221', 'WlvZqq_Sh221', 'ZqqZll_Sh221', 
    #'stops_PwPy8', 'stopWt_PwPy8', 'ttbar_nonallhad_PwPy8', 
    #'ZtautauB_Sh221', 'ZtautauC_Sh221', 'ZtautauL_Sh221', #'Ztautau_Sh221', 
    #'data15', 'data16',
    #'VBF_H2000', 'ggF_H2000', 'VBF_H3000', 'ggF_H3000',
    #'VBF_HVT1000', 'ggF_HVT1000',
    #'VBF_RSG1000', 'ggF_RSG1000',
    'WmunuC_Sh221', 'WmunuB_Sh221', 'Wenu_Sh221', 'WenuL_Sh221', 'WenuC_Sh221', 'WenuB_Sh221', 'WtaunuL_Sh221', 'WtaunuC_Sh221', 'WtaunuB_Sh221', 'Wmunu_Sh221', 'WmunuL_Sh221'
    ]
SamplesNN = [
    #'ZjetsZeeB', 'ZjetsZeeC', 'ZjetsZeeL', 'ZjetsZeeHPT', 
    #'ZjetsZmumuB', 'ZjetsZmumuC', 'ZjetsZmumuL', 'ZjetsZmumuHPT',  'DibosonWqqWlv', 'DibosonWqqZll', 'DibosonWlvZqq', 'DibosonZqqZll', 
    #'Topstops', 'TopstopWt', 'Topttbar_nonallhad', 
    #'ZjetstautauB', 'ZjetstautauC', 'ZjetstautauL', #'ZjetstautauHPT', 
    #'Data15', 'Data16', 
    #'VBFH2000_spin0', 'ggFH2000_spin0', 'VBFH3000_spin0', 'ggFH3000_spin0',
    #'VBFHVT1000_spin0', 'DYHVT1000_spin0',
    #'VBFRSG1000_spin0', 'ggFRSG1000_spin0',
    'WjetsWmunuC', 'WjetsWmunuB', 'WjetsWenuHPT', 'WjetsWenuL', 'WjetsWenuC', 'WjetsWenuB', 'WjetsWtaunuL', 'WjetsWtaunuC', 'WjetsWtaunuB', 'WjetsWmunuHPT', 'WjetsWmunuL'
    ]
nSamples = len(Samples)


if runForBkg:
    for i in range(0, nSamples):
        name_sample_bkg = Samples[i]
        VT_name = VT_path + name_sample_bkg + '.root'
        DF_VT_bkg = pd.DataFrame( root2array(VT_name, 'Nominal', branches=list_branches(VT_name) ) )

        name_sample_bkg_NN = SamplesNN[i]
        name_fields = np.load( DF_path + 'rootBranchSubSampleForDataML_' + name_sample_bkg_NN + '.npy' )
        DF_bkg  = pd.DataFrame( np.load( DF_path + 'ResultsDataMLPD_' + name_sample_bkg_NN + '.npy' ) , columns=name_fields )

        print 'Making NN VT Tree for sample   ', name_sample_bkg
        NNTreeMakerForBkg( VT_name, name_sample_bkg, DF_bkg )
