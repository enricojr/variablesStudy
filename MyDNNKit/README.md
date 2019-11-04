# Installation Instructions on lxplus with Miniconda2
`bash Miniconda2-latest-Linux-x86_64.sh`

use /afs/cern.ch/work/k/kbachas/miniconda2 due to space limitations

answer no to the question on prepending to PATH

`echo ". /afs/cern.ch/work/k/kbachas/miniconda2/etc/profile.d/conda.sh" >> ~/.bash_profile`

logout and back in, now conda should work

`conda create -n AIenv`

`conda update conda`

`conda activate AIenv`

`conda install keras scikit-learn pandas numpy theano matplotlib seaborn pydot`

`conda install python=2`

`conda install -c nlesc root_numpy`

`pip install scikit-hep`

everytime you need to run you have to do:

`export LD_PRELOAD=/afs/cern.ch/work/k/kbachas/miniconda2/envs/AIenv/lib/libstdc++.so.6.0.24`

# Installation Instructions for setup with Python 3 and without ROOT dependencies
`bash Miniconda3-latest-Linux-x86_64.sh`

logout and back in, now conda should work

`conda create -n AIenv`

`conda update conda`

`conda activate AIenv`

`conda install keras scikit-learn pandas numpy theano matplotlib seaborn pydot colorama`

`pip install scikit-hep`

`pip install uproot`



# RunML.py
Contains the 'main' and is therefore the driving python file. The parsing of the arguments from the command line is done here.
The types of jobs that can be run are:
- '--ConvertRootToPD' Takes flat ROOT Ntuples as input and outputs Panda Dataframes. The separation in train and test samples is already done here. Also, not all branches are kept from the initial ML ntuples but only the ones that are defined in Configuration.py
- '--CreateTrainTestPD' Mixing and shuffling of Panda Dataframes to create one Panda DataFrame with both Signal and Background.
- '--Train' Train a DNN model. The mode of running(binary, multiclassification, parametrized, simpleRNN etc) needs to be defined here. The output will be the model in h5 format and a pickle file containing the configuration of the model and job. This pickle file will be then read when running on the test samples.
- '--LoadTrainedModel' Will load an existing trained model and run predictions on the test samples. Need to define the trained model path.
- '--ValidPlotsFromTrainTestDF' plot input variables as Signal and Background
- '--ValidPlotsDataMC' plot input variable as Data/MC
- '--printParamSet' Dump the available HyperParameter sets
- '--printSetup' Dump the setup

Inportant paramteres are:
- '--InputMLNtuplePath' Defines the path where the input ROOT ntuples are
- '--PDPath' Defines the path where the Panda Dataframes will be stored
- '--VarPlotPath'  Defines the path where the control plots will be stored when the VariablesToPlot is not empty and --ValidPlotsDataMC is used

# Configuration.py
Define the following setup parameters:
rootBranchSubSample
VariablesToPlot
InputDNNVariables
ScanParams
Params
Dropout

# ConfigClass.py  
Holds the python class that is handling all the job configuration

# ModelBuilder.py
Holds the basic DNN/RNN/CNN building method with dropout by default to 20%
def BuildDNN(N_input,width,depth):
N_input: Number of input variables
width: Number of NN nodes
depth: Number of hidden layers to use

# PrepareData.py
Holds method to:
- Create Panda DFs files from the flat Ntuples(=can be the output of CxAODReader). Train/Test separation is already done here at 70:30 ratio. Applies preselection on input ntuples if requested with the  "--PreselectionCommand " command as simple text  E.g: ``--PreselectionCommand "inPanda[(inPanda.isMerged == 1 ) & (inPanda.isVBFevent == 0)]"``
- Create 1 single DF file containing the mixure of signal and background events you want specified with --inSignalFiles, --inBackgrFiles flags.
  - Note that if you need to do additional filtering you can do it at this point writing the command as simple text with the --PreselectionCommand as above
- This is where Y,X arrays are defined. CAUTION: Y array takes the 'isSignal' input variable to tag and event as signal or background. In case multi-classification is run then this is 'Class' variable which is added to the train/test DFs when the MixDF is created. The 'Class' variable follows the scheme of the 'channelDic' dictionary found in HelperTools.py:

# Permutator.py
Provides the actual permutations from parameter values in the Configuration.py

# TrainDNN.py
Calls ModelBuilder and handles the construction and training of the Network

# LoadDNN.py
Loads the model from path 'modelpath + '/model.h5'' and the setup from 'modelpath + '/DNN_Setup''

# HelperTools
Holds small routines to ease the job execution
