if doScore3:
    yhat_test  = model.predict(X_test,verbose = True,batch_size=setupClient.Params['BatchSize'])
    yhat_train = model.predict(X_train,verbose = True,batch_size=setupClient.Params['BatchSize'])
    rounded_test  = np.array([round(x[0]) for x in yhat_test])
    rounded_train = np.array([round(x[0]) for x in yhat_train])

    df_full = pd.read_pickle(setupClient.PDPath+setupClient.pklDataFileTag+'.pkl')
    predicted_background_1 = df_full.iloc[np.array(ix_test)[rounded_test == 0]]
    predicted_signal_1     = df_full.iloc[np.array(ix_test)[rounded_test == 1]]
    predicted_background_2 = df_full.iloc[np.array(ix_train)[rounded_train == 0]]
    predicted_signal_2     = df_full.iloc[np.array(ix_train)[rounded_train == 1]]

    predicted_background = pd.concat([predicted_background_1,predicted_background_2])
    predicted_signal     = pd.concat([predicted_signal_1,predicted_signal_2])

    # intersections = predicted_signal_1.index.intersection(predicted_signal_2.index)
    # print intersections
    bins=np.linspace(0, 1000., 100)

    plt.hist(predicted_background['Zll_pt']/1000., histtype='stepfilled', normed=False, bins=bins, weights=36.1*predicted_background['LumiNorm'], label=r'background', linewidth=1)
    plt.hist(predicted_signal['Zll_pt']/1000., histtype='step', normed=False, bins=bins, weights=36.1*predicted_signal['LumiNorm'], label=r'ggH1000', linewidth=1, color='red', linestyle='dashed')

    data_full = pd.read_pickle(setupClient.PDPath+'Data_PD.pkl')
    data_full_matrix = data_full[setupClient.SelectedFields[setupClient.VarSet]].as_matrix()

    yhat_data = model.predict(data_full_matrix,verbose = True,batch_size=setupClient.Params['BatchSize'])
    rounded_data = np.array([round(x[0]) for x in yhat_data])
    predicted_data    = data_full.iloc[np.array(data_full.index)[rounded_data == 0]]

    _ = skh_plt.hist(predicted_data['Zll_pt']/1000., bins=bins, errorbars=True, histtype='marker',label='Data', color='black')

    plt.legend(loc='best',prop={'size': 10})

    # plt.xlabel(var,fontsize=14)
    plt.savefig(setupClient.ModelSavePath+"/dataMCFinal.pdf")
    plt.show()



    #############
    for myvar in setupClient.VariablesToPlot:
        plt.figure(figsize=(12,8))
        x = ix_test[myvar].as_matrix()
        sns.regplot(x=x, y=yhat_test, x_bins=10, fit_reg=None)
        plt.savefig(setupClient.ModelSavePath+"/Score_VS_"+myvar+".pdf")
        plt.clf()


def preparePandasMulti(setupClient):
    print ("-----------------------------")
    print (" Preparing multi-class data  ")
    print ("-----------------------------")

    df_All = []

    print 'Number of signal files',len(setupClient.InputFilesSB['Signal'])
    print 'Number of backgr files',len(setupClient.InputFilesSB['Background'])

    classID = 0;

    #Get Files
    for ifile in setupClient.InputFilesSB['Signal']:
        df_s = ht.getDFEvents(setupClient.PDPath,ifile)
        df_s['ChannelClass'] = classID
        df_All += [ df_s ]

    classID +=1

    for ifile in setupClient.InputFilesSB['Background']:
        df_b = ht.getDFEvents(setupClient.PDPath,ifile)
        df_b['ChannelClass'] = classID
        df_All += [ df_b ]
        classID +=1

    print "\nShuffling and Saving Pandas Sample"
    Mix_All = Randomizing(pd.concat(df_All,ignore_index=True))
    Mix_All.to_pickle(setupClient.PDPath+'MixAll_PD.pkl')

    # --------------------
    # data = np.genfromtxt('/afs/le.infn.it/user/k/kbachas/MyDNNKit/XSections_13TeV.txt', comments='#',usecols = (0, 1, 2,3),dtype=[('dsid','i8'),('xsec','f8'),('Kf','f8'),('filter','f8')])
    # xsecdf = pd.DataFrame(data)
    # xsecdf = xsecdf.set_index('dsid')

    # df_list = [signalDF,zjetsDF,dibosonDF,topDF]
    # for idf in df_list:
    #     idf['Xsec'] = [getNorm(dsid,xsecdf) for dsid in idf['RunNumber']]
    #     idf['Norm']= idf['Xsec']*idf['FullEventWeight']
    #     print idf.head()

    # topDF['Xsec'] = [getNorm(dsid,xsecdf) for dsid in topDF['RunNumber']]
    # topDF['Norm']= topDF['Xsec']*topDF['FullEventWeight']
    # colors = plt.cool(np.linspace(0, 1, 7))


#n, bins, _ = plt.hist(data, bins=np.arange(0,20,0.5),normed=1)
# mid = 0.5*(bins[1:] + bins[:-1])
# plt.errorbar(mid, n, yerr=0.01, fmt='none')
