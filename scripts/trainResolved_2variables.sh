### WARNING:
#   remember to edit Configuration.py and enable the corresponding set of variables

cd ../MyDNNKit/

python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ -y 0 --MixPD_TrainTestTag mixPD_resolved_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ -y 1 --MixPD_TrainTestTag mixPD_resolved_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ -y 2 --MixPD_TrainTestTag mixPD_resolved_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ -y 3 --MixPD_TrainTestTag mixPD_resolved_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ -y 4 --MixPD_TrainTestTag mixPD_resolved_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ -y 5 --MixPD_TrainTestTag mixPD_resolved_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/ -y 6 --MixPD_TrainTestTag mixPD_resolved_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_ggF/train_2variables -m binary

python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/ -y 0 --MixPD_TrainTestTag mixPD_resolved_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/ -y 1 --MixPD_TrainTestTag mixPD_resolved_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/ -y 2 --MixPD_TrainTestTag mixPD_resolved_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/ -y 3 --MixPD_TrainTestTag mixPD_resolved_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/ -y 4 --MixPD_TrainTestTag mixPD_resolved_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/ -y 5 --MixPD_TrainTestTag mixPD_resolved_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/ -y 6 --MixPD_TrainTestTag mixPD_resolved_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_resolved_VBF/train_2variables -m binary

cd -
