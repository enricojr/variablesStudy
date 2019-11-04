import root_pandas as rp
from root_numpy import root2array, list_branches, array2root
from ROOT import *
from array import array

def NNTreeMakerForTestTrain( VT_name, name_sample, DF_test, DF_train ):
    f = TFile( VT_name )
    t = f.Get('Nominal')
    nentries = t.GetEntries()
    print(nentries)

    new_file = TFile('NNVT_' + name_sample + '.root', 'recreate')
    new_file.cd()

    new_tree = t.CloneTree(0)
    new_tree.CopyEntries(t)

    NNScore          = array("f", [0])
    isTestEvent      = array("i", [0])
    VTEventID        = array("i", [0])
    hasOSEtaJetsPair = array("i", [0])

    b_NNScore          = new_tree.Branch("NNScore", NNScore, "NNScore/f")
    b_isTestEvent      = new_tree.Branch("isTestEvent", isTestEvent, "isTestEvent/i")
    b_VTEventID        = new_tree.Branch("VTEventID", VTEventID, "VTEventID/i")
    b_hasOSEtaJetsPair = new_tree.Branch("hasOSEtaJetsPair", hasOSEtaJetsPair, "hasOSEtaJetsPair/i")

    #nentries = 1000
    for i in range(0, nentries):
        print i

        NNScore[0]          = -3.
        isTestEvent[0]      = -3
        VTEventID[0]        = -3
        hasOSEtaJetsPair[0] = -3
        
        if not DF_test[ DF_test['VTEventID']==i ].empty:
            row = DF_test.loc[ DF_test['VTEventID']==i ]

            #print(i, row.iloc[0]['VTEventID'], NNScore[0])
            NNScore[0]          = row.iloc[0]['DNN_Score']
            isTestEvent[0]      = 1
            VTEventID[0]        = row.iloc[0]['VTEventID']
            hasOSEtaJetsPair[0] = row.iloc[0]['hasOSEtaJetsPair']

        if not DF_train[ DF_train['VTEventID']==i ].empty:
            row = DF_train.loc[ DF_train['VTEventID']==i ]

            NNScore[0]          = row.iloc[0]['DNN_Score']
            isTestEvent[0]      = 0
            VTEventID[0]        = row.iloc[0]['VTEventID']
            hasOSEtaJetsPair[0] = row.iloc[0]['hasOSEtaJetsPair']
            
        b_NNScore.Fill()
        b_isTestEvent.Fill()
        b_VTEventID.Fill()
        b_hasOSEtaJetsPair.Fill()

    new_tree.Write()
    new_file.Close()


def NNTreeMakerForBkg( VT_name, name_sample, DF_test ):
    f = TFile( VT_name )
    t = f.Get('Nominal')
    nentries = t.GetEntries()
    print(nentries)

    new_file = TFile('NNVT_' + name_sample + '.root', 'recreate')
    new_file.cd()

    new_tree = t.CloneTree(0)
    new_tree.CopyEntries(t)

    NNScore          = array("f", [0])
    isTestEvent      = array("i", [0])
    VTEventID        = array("i", [0])
    hasOSEtaJetsPair = array("i", [0])

    b_NNScore          = new_tree.Branch("NNScore", NNScore, "NNScore/f")
    b_isTestEvent      = new_tree.Branch("isTestEvent", isTestEvent, "isTestEvent/i")
    b_VTEventID        = new_tree.Branch("VTEventID", VTEventID, "VTEventID/i")
    b_hasOSEtaJetsPair = new_tree.Branch("hasOSEtaJetsPair", hasOSEtaJetsPair, "hasOSEtaJetsPair/i")

    #nentries = 1000
    for i in range(0, nentries):
        print i

        NNScore[0]          = -3.
        isTestEvent[0]      = -3
        VTEventID[0]        = -3
        hasOSEtaJetsPair[0] = -3
        
        NNScore[0]          = DF_test.iloc[i]['DNN_Score']
        isTestEvent[0]      = 1
        VTEventID[0]        = DF_test.iloc[i]['VTEventID']
        hasOSEtaJetsPair[0] = DF_test.iloc[i]['hasOSEtaJetsPair']

        b_NNScore.Fill()
        b_isTestEvent.Fill()
        b_VTEventID.Fill()
        b_hasOSEtaJetsPair.Fill()

    new_tree.Write()
    new_file.Close()







"""
def NNTreeMaker( DF_VT, name_sample, DF_test, DF_train ):
    DF_VT['NNScore']=-3.
    DF_VT['VTEventID']=-3.
    DF_VT['hasOSEtaJetsPair']=-3.
    DF_VT['isTestEvent']=0

    DF_VT = AddDF( DF_VT, name_sample, DF_test , 1)
    DF_VT = AddDF( DF_VT, name_sample, DF_train, 0)
    #rp.to_root( DF_VT, 'NNVT_' + name_sample + '.root', key='Nominal' )
    
    array = DF_VT.values
    print('olaaa', DF_VT.values)
    #print(DF_VT.values.dtype)
    array.dtype.fields = (DF_VT.columns.values)
    array2root( array, filename='NNVT_' + name_sample + '.root', treename='Nominal', mode='recreate', branches=DF_VT.columns.values )

def AddDF( DF_VT, name_sample, DF_NN, isTestDF ):
    nEvents = DF_VT.shape[0]
    nEvents = 10
    for i in range(0, nEvents):
        print i
        #print i, DF_NN[ DF_NN['VTEventID']==i ]['NNScore']
        #print i, DF_NN[ DF_NN['VTEventID']==i ]['VTEventID']

        if not DF_NN[ DF_NN['VTEventID']==i ].empty:
            row = DF_NN.loc[ DF_NN['VTEventID']==i ]
            #print row, type(row)
            #print row.iloc[0]['VTEventID']
            #print row.iloc[0]['NNScore']
        
            DF_VT['isTestEvent'][i]      = isTestDF
            DF_VT['NNScore'][i]          = row.iloc[0]['DNN_Score']
            DF_VT['VTEventID'][i]        = row.iloc[0]['VTEventID']
            DF_VT['hasOSEtaJetsPair'][i] = row.iloc[0]['hasOSEtaJetsPair']
            
    print DF_VT['NNScore']
    return DF_VT

def NNTreeMakerForBkg( DF_VT, name_sample, DF ):
    print( DF_VT.shape, DF.shape )

    #DF_VT['NNScore']=-3.
    #DF_VT['VTEventID']=-3.
    #DF_VT['hasOSEtaJetsPair']=-3.
    #DF_VT['isTestEvent']=1

    DF_VT['NNScore'] = DF['DNN_Score'].values
    #DF_VT[ DF_VT['hasOSEtaJetsPair']==0 ]['NNScore'] = -3
    #DF_VT['VTEventID'] = DF['VTEventID']
    #DF_VT['hasOSEtaJetsPair'] = DF['hasOSEtaJetsPair']

    print(DF_VT['NNScore'])
    rp.to_root( DF_VT, 'NNVT_' + name_sample + '.root', key='Nominal' )

    #print( DF_VT['VTEventID'], DF['VEEventID'] )


"""
"""
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
