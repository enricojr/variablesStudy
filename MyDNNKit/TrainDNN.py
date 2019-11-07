from keras.models import Model
from keras.callbacks import ModelCheckpoint, EarlyStopping

from HelperTools import *
from PrepareData import LoadData,LoadDataRNN
import ModelBuilder
import PlotTools
import pickle

from keras import backend as K

def TrainRNN(setupClient):
    (X_train, y_train), (X_test, y_test), (w_train,w_test), (ix_train, ix_test) = LoadDataRNN(setupClient)

    modelpath = setupClient.ModelSavePath

    model=ModelBuilder.BuildTestRNN(setupClient,X_train)
    model.compile('adam', 'binary_crossentropy')
    print (Fore.BLUE+"--------------------------")
    print (Back.BLUE+"       TRAINING RNN       ")
    print (Fore.BLUE+"--------------------------")
    try:
        modelMetricsHistory =  model.fit([X_train], y_train, batch_size=16,
        #     class_weight={
        #         0 : 0.20 * (float(len(y)) / (y == 0).sum()),
        #         1 : 0.40 * (float(len(y)) / (y == 1).sum()),
        #         2 : 0.40 * (float(len(y)) / (y == 2).sum())
        # },
        callbacks = [
            EarlyStopping(verbose=True, patience=10, monitor='val_loss'),
            ModelCheckpoint(modelpath+'/model.h5', monitor='val_loss', verbose=True, save_best_only=True)
        ],
        epochs=30,
        validation_split = 0.2)

    except KeyboardInterrupt:
        print ('Training ended early.')

    #store the configuration of the training to disk
    outfile = open(modelpath+'/RNN_Setup','wb')
    pickle.dump(setupClient,outfile)
    outfile.close()

    return modelMetricsHistory


def TrainDNN(setupClient):
    (X_train, y_train), (X_test, y_test), (w_train,w_test), (ix_train, ix_test) = LoadData(setupClient)

    n_dim=X_train.shape[1]
    modelpath = setupClient.ModelSavePath

    Nsig = (y_train == 1).sum()
    Nbkg = (y_train != 1).sum()

    # TODO: Check this is working or still needed
    if (  Nsig!=Nbkg  ) and setupClient.useEqualSizeSandB==True:
        print ('You have selected to use equal portions of signal and background events but the numbers are not equal')
        print (Nsig,Nbkg)
        quit()


    print (Fore.BLUE+"--------------------------")
    print (Back.BLUE+"       TRAINING...!       ")
    print (Fore.BLUE+"--------------------------")
    print ("Number of input variables : ",X_train.shape[1])

    from  collections  import Counter
    cls_ytrain_count = Counter(y_train)
    Nclass = len(cls_ytrain_count)

    lossFunc = 'binary_crossentropy'
    if setupClient.runMode=='multi':
        print (Fore.GREEN+'Number of events per class in Train Sample:')
        for channel in channelDic:
            print ('{:<15}{:<15}'.format(channel, cls_ytrain_count[channelDic[channel]] ) )

        lossFunc = 'sparse_categorical_crossentropy'
        model=ModelBuilder.BuildDNNMulti(setupClient,Nclass,n_dim,setupClient.Params['Width'],setupClient.Params['Depth'])
    else:
        print (Fore.GREEN+'Number of events per class in Train Sample:')
        print ('{:<15}{:<15}'.format('Background', cls_ytrain_count[0] ) )
        print ('{:<15}{:<15}'.format('Signal', cls_ytrain_count[1] ) )
        model=ModelBuilder.BuildDNN(setupClient,n_dim,setupClient.Params['Width'],setupClient.Params['Depth'])

    model.compile(loss=lossFunc,optimizer=setupClient.Params['Optimizer'],metrics=['accuracy'])
    K.set_value(model.optimizer.lr, setupClient.Params['LearningRate'] )
    # model.summary()
    print(model.get_config())
    # print (model.optimizer.__class__.__name__)
    # print (K.get_value(model.optimizer.lr))

    callbacks = [
        # if we don't have a decrease of the loss for 4 epochs, terminate training.
        EarlyStopping(verbose=True, patience=5, monitor='val_loss'),
        # Always make sure that we're saving the model weights with the best val loss.
        ModelCheckpoint(modelpath+'/model.h5', monitor='val_loss', verbose=True, save_best_only=True)
    ]

    # TODO: make the number of classes be found and treated automatically by the flow
        #store the configuration of the training to disk
    outfile = open(modelpath+'/DNN_Setup','wb')
    pickle.dump(setupClient,outfile)
    outfile.close()

    if setupClient.runMode=='multi':
        Nsig     = float(cls_ytrain_count[1])
        NZjets   = float(cls_ytrain_count[0])
        NDiboson = float(cls_ytrain_count[2])
        NTop     = float(cls_ytrain_count[3])

        wZjets = round(Nsig / NZjets,3)
        wDiboson = round(Nsig / NDiboson,3)
        wTop = round(Nsig / NTop,3)
        wsig = round(1.0,2)

        print(Fore.GREEN+'Weights to apply:')
        print('{:<15}{:<15}'.format('Zjets',wZjets))
        print('{:<15}{:<15}'.format('Signal',wsig))
        print('{:<15}{:<15}'.format('Diboson',wDiboson))
        print('{:<15}{:<15}'.format('Top',wTop))

        modelMetricsHistory = model.fit(
            X_train,
            y_train,
            class_weight={
                0 : wZjets,
                1 : wsig, ## Signal
                2 : wDiboson,
                3 : wTop
            },
            epochs=setupClient.Params['Epochs'],
            batch_size=setupClient.Params['BatchSize'],
            validation_split=0.2,
            callbacks=callbacks,
            verbose=1)
    else:
        if setupClient.useEqualSizeSandB==True:
            modelMetricsHistory = model.fit(
                X_train,
                y_train,
                epochs=setupClient.Params['Epochs'],
                batch_size=setupClient.Params['BatchSize'],
                validation_split=0.2,
                callbacks=callbacks,
                verbose=0)

            print (modelMetricsHistory.history['val_loss'])
        else:
            print ('{:<25}'.format(Fore.BLUE+'Training with class_weights because of unbalance classes !!'))
            nsignal = cls_ytrain_count[1]
            nbackground = cls_ytrain_count[0]
            print ('Signal=',nsignal,'Background=',nbackground)

            wbkg = (nsignal / nbackground)
            wsig = 1.0

            if nsignal > nbackground:
                wbkg = 1.0
                wsig = (nbackground/nsignal)
            print(Fore.GREEN+'Weights to apply:')
            print('{:<15}{:<15}'.format('Background',round(wbkg,3)))
            print('{:<15}{:<15}'.format('Signal',wsig))

            modelMetricsHistory = model.fit(
                X_train,
                y_train,
                class_weight={
                0 : wbkg,
                1 : wsig},
                epochs=setupClient.Params['Epochs'],
                batch_size=setupClient.Params['BatchSize'],
                validation_split=0.2,
                callbacks=callbacks,
                verbose=1
            )



    return modelMetricsHistory
