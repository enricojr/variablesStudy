from keras.models import Sequential,Model
from keras.layers.core import Dense, Activation
from keras.layers import BatchNormalization, Dropout, GRU, concatenate, SimpleRNN, Masking, RNN, LSTM,Input
import numpy as np

def BuildDNN(setupClient,N_input,width,depth):
    model = Sequential()
    model.add(Dense(units=width, input_dim=N_input))
    model.add(Activation('relu'))
    if setupClient.Dropout >0 :
        model.add(Dropout(setupClient.Dropout))

    for i in range(0, depth):
        model.add(Dense(width))
        model.add(Activation('relu'))
        if setupClient.Dropout >0 :
            model.add(Dropout(setupClient.Dropout))

    model.add(Dense(1, activation='sigmoid'))

    return model


def BuildDNNMulti(setupClient,Nclass,N_input,width,depth):
    model = Sequential()
    model.add(Dense(units=width, input_dim=N_input))
    model.add(Activation('relu'))
    if setupClient.Dropout >0 :
        model.add(Dropout(setupClient.Dropout))

    for i in range(0, depth):
        model.add(Dense(width))
        model.add(Activation('relu'))
        if setupClient.Dropout >0 :
            model.add(Dropout(setupClient.Dropout))

    model.add(Dense(Nclass, activation='softmax'))

    return model


def BuildTestRNN(setupClient,Xjet_train):
    print ('Building Simple RNN model')
    # JET_SHAPE = N_input
    JET_SHAPE = Xjet_train.shape[1:]

    jet_input  = Input(JET_SHAPE)
    jet_channel = Masking(mask_value=setupClient.MaskValue, name='jet_masking')(jet_input)


    #jet_channel = GRU(25, name='jet_gru')(jet_channel)
    #jet_channel = Dropout(0.3, name='jet_dropout')(jet_channel)

    jet_channel = LSTM(input_dim=24, output_dim=25, name='jet_lstm1', return_sequences=True)(jet_channel)
    jet_channel = Dropout(0.3, name='jet_dropout0')(jet_channel)
    jet_channel = LSTM(25, name='jet_lstm2', return_sequences=False)(jet_channel)

    jet_channel = Dropout(0.3, name='jet_dropout')(jet_channel)

    #jet_channel = Dense(64, activation = 'relu')(jet_channel)
    #jet_channel = Dropout(0.3)(jet_channel)
    #jet_channel = Dense(64, activation = 'relu')(jet_channel)
    #jet_channel = Dropout(0.3)(jet_channel)
    #jet_channel = Dense(64, activation = 'relu')(jet_channel)
    #jet_channel = Dropout(0.3)(jet_channel)
    #jet_channel_outputs = Dense(1, activation='sigmoid')(jet_channel)

    jet_channel = Dense(output_dim=1)(jet_channel)
    jet_channel_outputs = Activation('sigmoid')(jet_channel)

    combined_rnn = Model(inputs=[jet_input], outputs=jet_channel_outputs)
    combined_rnn.summary()

    return combined_rnn


def BuildSimpleRNN(setupClient, N_input):
    print ('Building Simple RNN model')

    #batch_size = 1000
    batch_size = setupClient.Params['BatchSize']

    model = Sequential()

    print ('Mask value', setupClient.MaskValue)
    #model.add(Masking(mask_value=setupClient.MaskValue, input_shape=(N_input, 1) ) )
    #model.add(Masking(mask_value=-999., input_shape=(N_input, 1) ) )
    model.add(Masking(mask_value=setupClient.MaskValue, input_shape=(6, 4) ) )

    #layers = [1, N_input+1, 100, 1]
    layers = [N_input, N_input+1, N_input+1, 1]
    model.add(LSTM(input_dim=layers[0], output_dim=layers[1], return_sequences=True ))
    model.add(Dropout(0.2))

    model.add(LSTM(layers[2], return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(output_dim=layers[3]))
    #model.add(Activation("linear"))
    model.add(Activation("sigmoid"))




    #model.add(SimpleRNN(N_input, activation='relu', batch_input_shape=(batch_size, N_input, 1)))
    #model.add(SimpleRNN(N_input, activation='relu', input_shape=(N_input, 1)))
    #model.add(LSTM(N_input, kernel_initializer="one", input_shape=(N_input, 1)) )
    #model.add(LSTM(output_dim=1, kernel_initializer="one", input_shape=(N_input, 1)) )

    #model.add(Activation('relu'))
    #model.add(Dense(1,activation='linear'))

    #if setupClient.Dropout >0 :
        #model.add(Dropout(setupClient.Dropout))

    #model.add(Dense(1, activation='sigmoid'))
    model.summary()

    print ('Done')
    return model


### antonio ### CNN ###
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
#from keras import backend as K
#K.set_image_dim_ordering('th')

def BuildCNN(setupClient, N_input):
    print ('Building CNN model')

    model = Sequential()

    model.add(Conv2D(64, kernel_size=2, activation='relu', input_shape=(6, 4, 1) ) )
    model.add(Conv2D(32, kernel_size=2, activation='relu'))
    model.add(Flatten())
    #model.add(Dense(1, activation='softmax'))
    model.add(Dense(1, activation='sigmoid'))

    model.summary()

    print ('Done')
    return model


### antonio ### SVM ###
from sklearn.svm import SVC

def BuildSVM(setupClient, N_input):
    print ('Building SVM model')

    #svm = SVC(kernel='linear', C=1.0, random_state=0)
    svm = SVC(kernel='rbf', random_state=0, gamma=0.1, C=10.0)

    print ('Done')
    return svm
