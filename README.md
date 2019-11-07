++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++ scripts/prepareRawData.C
run as

root -b -q prepareRawData.C

This one takes the raw data from Napoli and merges the different MC productions into single ntuples. The output is saved in /nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++ scripts/convertFromRootToPanda.sh
run as

source convertFromRootToPanda.sh

It takes the merged raw data, selects merged/resolved ggf/vbf events and creates pandas dataframes, after splitting the data into test and training samples

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++ scripts/createTrainAndTestSamples.sh
run as

source createTrainAndTestSamples.sh

It takes the pickle files for the 1TeV Higgs signal and background, and creates the mixed and shuffled set split in test and train samples

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
To prepare for the next steps, one must edit the MyDNNKit/Configuration.py file by enabling the useful variables.
Set the variables list in InputDNNVariables
The run

python RunML.py -d

to look at all the permutations. Take the number of permutations and loop over the -y parameter in the shell scripts (see below).

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++ scripts/trainMerged.sh
run as

source trainMerged.sh

It builds the DNN and trains the merged data.

WARNING!!!
Before running, edit MyDNNKit/Configuration.py to enable the corresponding variables

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++ scripts/trainResolved.sh
run as

source trainResolved.sh

It builds the DNN and trains the resolved data.

WARNING!!!
Before running, edit MyDNNKit/Configuration.py to enable the corresponding variables

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++ scripts/testMerged.sh
run as

source testMerged.sh

It builds the DNN and tests the merged data.

WARNING!!!
Before running, edit MyDNNKit/Configuration.py to enable the corresponding variables

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++ scripts/testResolved.sh
run as

source testResolved.sh

It builds the DNN and tests the resolved data.

WARNING!!!
Before running, edit MyDNNKit/Configuration.py to enable the corresponding variables

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++ scripts/getDFsize.py
run as

python getDFsize.py

Prints the size of all the pickle files (file names hardcoded in the script)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++ scripts/makeReports.C
run as

root -b -q makeReports.C

Copies the images to the report folder and creates the tex files of the report beamers