### WARNING:
#   remember to edit Configuration.py and enable the corresponding set of variables

cd ../MyDNNKit/

python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ -y 0 --MixPD_TrainTestTag mixPD_merged_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ -y 1 --MixPD_TrainTestTag mixPD_merged_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/ -y 2 --MixPD_TrainTestTag mixPD_merged_ggF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_ggF/train_2variables -m binary

python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/ -y 0 --MixPD_TrainTestTag mixPD_merged_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/ -y 1 --MixPD_TrainTestTag mixPD_merged_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/train_2variables -m binary
python RunML.py --Train --PDPath /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/ -y 2 --MixPD_TrainTestTag mixPD_merged_VBF -o /nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_merged_VBF/train_2variables -m binary

cd -
