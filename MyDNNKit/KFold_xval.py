from keras.models import Model,load_model
from keras.callbacks import EarlyStopping,ModelCheckpoint

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_curve, auc, roc_auc_score, classification_report

from HelperTools import *
import ModelBuilder

from keras import backend as K
from  collections  import Counter
from matplotlib import pyplot as plt


def doKFold(setupClient):
    print (Fore.BLUE+"--------------------------")
    print (Back.BLUE+" K-Fold Cross Validation  ")
    print (Fore.BLUE+"--------------------------")

    pdtoLoad_Train = setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Train.pkl'
    pdtoLoad_Test = setupClient.PDPath+setupClient.MixPD_TrainTestTag+'_Test.pkl'

    print ('{:<45}{:<25}'.format("Train sample",Fore.GREEN+pdtoLoad_Train) )
    print ('{:<45}{:<25}'.format("Test sample", Fore.GREEN+pdtoLoad_Test) )
    if not os.path.isfile(pdtoLoad_Train):
        print ("PD file",pdtoLoad_Train," not found!")
        quit()
    if not os.path.isfile(pdtoLoad_Test):
        print ("PD file",pdtoLoad_Test," not found!")
        quit()

    df_Train = pd.read_pickle(pdtoLoad_Train)
    df_Test = pd.read_pickle(pdtoLoad_Test)

    ## Add them together:
    df_tot = pd.concat([df_Train,df_Test],ignore_index=True)

    VariablesSet =  setupClient.InputDNNVariables[setupClient.VarSet]
    print('{:<45}{:<25}'.format("Variable set",Fore.GREEN+str(setupClient.VarSet)+' '+str(VariablesSet)) )

    X=df_tot[VariablesSet].as_matrix()
    scaler = StandardScaler()
    le = LabelEncoder()
    Y= le.fit_transform(df_tot['isSignal'])
    kfold = StratifiedKFold(n_splits=5, shuffle=False, random_state=None)
    cvscores = []
    ii = 0
    tprs = []
    aucs = []
    mean_fpr = np.linspace(0, 1, 100)

    for train, test in kfold.split(X, Y):
        print('Doing Fold',ii)
        cls_ytrain_count = Counter(Y[train])
        print (Fore.GREEN+'Number of events per class in Train Sample:')
        print ('{:<15}{:<15}'.format('Background', cls_ytrain_count[0] ) )
        print ('{:<15}{:<15}'.format('Signal', cls_ytrain_count[1] ) )

        X[train] = scaler.fit_transform(X[train])
        X[test] = scaler.fit_transform(X[test])

        n_dim=X[train].shape[1]

        lossFunc = 'binary_crossentropy'
        model=ModelBuilder.BuildDNN(setupClient,n_dim,setupClient.Params['Width'],setupClient.Params['Depth'])
        if setupClient.runMode=='multi':
            lossFunc = 'sparse_categorical_crossentropy'
            model=ModelBuilder.BuildDNNMulti(setupClient,Nclass,n_dim,setupClient.Params['Width'],setupClient.Params['Depth'])

        model.compile(loss=lossFunc,optimizer=setupClient.Params['Optimizer'],metrics=['accuracy'])
        K.set_value(model.optimizer.lr, setupClient.Params['LearningRate'] )

        callbacks = [
            EarlyStopping(verbose=True, patience=5, monitor='val_loss'),
            ModelCheckpoint(setupClient.ModelSavePath+'/model_kfold'+str(ii)+'.h5', monitor='val_loss', verbose=True, save_best_only=True)
        ]

        wbkg = (cls_ytrain_count[1] / cls_ytrain_count[0])
        wsig = 1.0
        print(Fore.GREEN+'Weights to apply:')
        print('{:<15}{:<15}'.format('Background',round(wbkg,3)))
        print('{:<15}{:<15}'.format('Signal',wsig))


        kf_history = model.fit(
            X[train],
            Y[train],
            class_weight={
            0 : wbkg,
            1 : wsig},
            epochs=setupClient.Params['Epochs'],
            batch_size=setupClient.Params['BatchSize'],
            validation_split=0.2,
            callbacks=callbacks,
            verbose=1
        )

        kf_scores = model.evaluate(X[test], Y[test], verbose=1)
        print("%s: %.3f%%" % (model.metrics_names[1], kf_scores[1]*100))
        cvscores.append(kf_scores[1] * 100)

        kf_yhat_test = model.predict(X[test])

        # Get 'Receiver operating characteristic' (ROC)
        fpr, tpr, thresholds = roc_curve(Y[test], kf_yhat_test)
        tprs.append(np.interp(mean_fpr, fpr, tpr))
        tprs[-1][0] = 0.0
        roc_auc = auc(fpr, tpr)
        aucs.append(roc_auc)
        plt.plot(fpr, tpr, lw=1, alpha=0.3,label='ROC fold %d (AUC = %0.3f)' % (ii, roc_auc))

        np.save( os.path.join(setupClient.ModelSavePath,'cv_metrics_fold'+str(ii)+'.npy') , kf_scores)
        np.save( os.path.join(setupClient.ModelSavePath,'cv_thresholds_fold'+str(ii)+'.npy') , thresholds)
        np.save( os.path.join(setupClient.ModelSavePath,'cv_tpr_fold'+str(ii)+'.npy') , tpr)
        np.save( os.path.join(setupClient.ModelSavePath,'cv_fpr_fold'+str(ii)+'.npy') , fpr)
        ii += 1

    plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',label='Luck', alpha=.8)
    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    std_auc = np.std(aucs)
    plt.plot(mean_fpr, mean_tpr, color='b',label=r'Mean ROC (AUC = %0.3f $\pm$ %0.3f)' % (mean_auc, std_auc),lw=1, alpha=.7)

    std_tpr = np.std(tprs, axis=0)
    tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
    tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
    plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.2, label=r'$\pm$ 1 std. dev.')

    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    # plt.title('Receiver operating characteristic example')
    plt.xticks(np.arange(0.0, 1.1, 0.1))
    plt.yticks(np.arange(0.0, 1.1, 0.1))
    plt.title('ROC curves for Signal vs Background')
    plt.legend(loc="lower right",fontsize='x-small')
    plt.savefig(setupClient.ModelSavePath+"/KFold_ROC.png")
    plt.clf()
