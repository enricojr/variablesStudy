#import Configuration

class ConfigClass(object):
    """docstring for ConfigClass."""

    def __init__(self,  **kwargs):
        super(ConfigClass, self).__init__()

        self.InputMLNtuplePath  = "/afs/le.infn.it/user/k/kbachas/ML/MyDNNKit/InputMLNtuples/"
        self.rootBranchSubSample = None
        self.PDPath = "/afs/le.infn.it/user/k/kbachas/MyDNNKit/PDFiles/"

        self.InputROOTFiles = []

        self.InputFilesSB  = {
            'Signal': [],
            'Background': [],
            'Data': []
        }

        self.InputDNNVariables =  [
            ['lep1_pt','lep1_eta','lep1_phi','lep1_E','lep2_pt','lep2_eta','lep2_phi','lep2_E','fatjet_pt','fatjet_eta','fatjet_phi','fatjet_E','fatjet_C2','fatjet_D2','Zll_mass','Zll_pt','MET' ]
        ]
        self.Params  = {
            "BatchSize": 2048,
            "LearningRate": 0.005,
            "WeightInitialization": "'normal'"
        }
        self.ScanParams  = {
            "Width":[32,64,128]
            ,"Depth":[2,3,4]
            ,"Epochs": [200]
            ,"VarSet": [ i for i in range(0,len(self.InputDNNVariables))]
        }
        self.VariablesToPlot = [
            'lep1_pt','lep1_eta','lep2_pt','lep2_eta','Zll_mass','Zll_pt','truth_zv_mass'
        ]

        self.CreateTrainTestPD   = False
        self.HyperParamSet = -1
        self.PrintParamSet = False
        self.LoadTrainedModel = False
        self.TrainedModelPath = None
        self.Train         = False
        self.DoKFold       = False
        self.OutBaseDir    = "ModelOutput"
        self.ConvertRootToPD   = False
        self.ModelSavePath = ""
        self.VarSet        = -1
        self.Dropout       = -1
        self.ValidPlotsFromTrainTestDF     = False
        self.ValidPlotsDataMC    = False
        self.MixPD_TrainTestTag     = "MixData"
        self.modelTag      = "llqqDNN"
        self.VarPlotPath   = "/afs/le.infn.it/user/k/kbachas/MyDNNKit/VarPlots/"
        self.runMode       = 'binary'
        self.useEqualSizeSandB = False
        self.massPoint     = ''
        self.MaskValue     = -99.
        self.Scaler        = None
        self.PreselectionCuts = ''
        self.doConfusionMatrix = False
        self.doEfficiency      = False
        self.doScore           = False
        self.doROC             = False
        self.unblind           = False
        self.testModelOnFullSamples= False

        for key in kwargs:
            setattr(self, key, kwargs[key])


    def printSetupParameters(self):
        print ('---- START Configuration dump ----')
        attrs = vars(self)
        print ('\n'.join("%s: %s" % item for item in attrs.items()))
        print ('---- END Configuration dump ----')
