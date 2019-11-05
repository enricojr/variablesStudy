+++++++ scripts/prepareRawData.C
run as

root -b -q prepareRawData.C

This one takes the raw data from Napoli and merges the different MC productions into single ntuples. The output is saved in /nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/

+++++++ convertFromRootToPanda.sh
run as

source convertFromRootToPanda.sh

It takes the merged raw data, selects merged/resolved ggf/vbf events and creates pandas dataframes, after splitting the data into test and training samples