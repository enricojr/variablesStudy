#!/bin/python 
import os, re, pickle

import pandas as pd
import root_pandas as rp

#path = '/data3/agiannini/DBLCode_19nov19/MLTool/MyDNNKit/output_test_13feb19_bis/llqqDNN_32_512_2_0.0003_VarSet0/'
#path = '/data3/agiannini/DBLCode_19nov19/MLTool/MyDNNKit/PDFiles_Lecce/MixPD_VBFggF1000_Train.pkl'
path = '../testDinos/DFFiles/'

#ix_test = pd.read_pickle( path )

ix_test = pd.read_pickle( path + 'ResultsTestPD.pkl')
ix_train = pd.read_pickle( path + 'ResultsTrainPD.pkl')

rp.to_root(ix_test , 'NNTree_TestSample.root', key='NNTree' )
rp.to_root(ix_train, 'NNTree_TrainSample.root', key='NNTree' )

### split the signal/bkg samples ###
isVBFggFClassification = True
isSignalBkgClassification = False

if isVBFggFClassification:
    ix_test_VBF = ix_test[ ix_test['ggFVBF']==1 ]
    ix_test_ggF = ix_test[ ix_test['ggFVBF']==0 ]
    rp.to_root(ix_test_VBF , 'NNTree_TestSample_VBF.root', key='NNTree' )
    rp.to_root(ix_test_ggF , 'NNTree_TestSample_ggF.root', key='NNTree' )

    ix_train_VBF = ix_train[ ix_train['ggFVBF']==1 ]
    ix_train_ggF = ix_train[ ix_train['ggFVBF']==0 ]
    rp.to_root(ix_train_VBF , 'NNTree_TrainSample_VBF.root', key='NNTree' )
    rp.to_root(ix_train_ggF , 'NNTree_TrainSample_ggF.root', key='NNTree' )
    
#if isSignalBkgClassification:
#    print 'hello'


"""
from progressbar import ProgressBar
pbar = ProgressBar()

i = 0
csize = 100000
for df in pbar(rp.read_root(name_file, chunksize=csize)):
    a = i*csize
    b = (i+1)*csize - 1
    temp = Z_Zjets_df.ix[a:b, :]
    print i, a, b
    #print temp
    final_df = pd.concat( [temp, df], axis=1 )
    if i==0: rp.to_root(final_df, 'NNSmallTree_Zjets.root', key='NNSmallTree' )
    else:    rp.to_root(final_df, 'NNSmallTree_Zjets.root', key='NNSmallTree', mode='a' ) 
    i += 1
"""
