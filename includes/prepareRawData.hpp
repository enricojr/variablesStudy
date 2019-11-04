#ifndef PREPARERAWDATA_HPP
#define PREPARERAWDATA_HPP

#include "parameters.hpp"

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int merge(const vector<string> fileNameIn,
	  const string fileNameOut){

  // loading trees
  vector<TFile *> file;
  vector<TTree *> tree;
  for(unsigned int i=0; i<fileNameIn.size(); i++){
    cout << __PRETTY_FUNCTION__ << ": loading tree from " << fileNameIn[i] << endl;
    TFile *newFile = TFile::Open(fileNameIn[i].c_str());
    if(newFile == nullptr){
      cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot open file " << fileNameIn[i] << endl;
      return 1;
    }
    TTree *newTree = (TTree *) newFile -> Get("nominal");
    if(newTree == nullptr){
      cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot load tree from file " << fileNameIn[i] << endl;
      return 1;
    }
    tree.push_back(newTree);
    file.push_back(newFile);
  }

  // merging trees
  TList *list = new TList();
  for(unsigned int i=0; i<fileNameIn.size(); i++){
    cout << __PRETTY_FUNCTION__ << ": adding tree from " << fileNameIn[i] << endl;
    list -> Add(tree[i]);
  }
  TFile *fileOut = TFile::Open(fileNameOut.c_str(), "RECREATE");
  if(fileOut == nullptr){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot open file " << fileNameOut << endl;
    return 1;
  }
  cout << __PRETTY_FUNCTION__ << ": merging trees" << endl;
  TTree *newTree = TTree::MergeTrees(list);
  newTree -> SetName("nominal");
  cout << __PRETTY_FUNCTION__ << ": writing tree to " << fileNameOut << endl;
  newTree -> Write();

  // cleaning memory
  delete newTree;
  delete list;
  fileOut -> Close();
  delete fileOut;
  for(unsigned int i=0; i<fileNameIn.size(); i++){
    delete tree[i];
    file[i] -> Close();
    delete file[i];
  }
  tree.clear();
  file.clear();

  return 0;
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeDATA(){

  vector<string> fileNameIn;
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_Data15_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_Data16_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_Data17_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_Data18_spin0.root");

  const string fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/data.root";

  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }

  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeDIBOSON(){

  vector<string> fileNameIn;
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_Diboson_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_Diboson_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_Diboson_spin0.root");

  const string fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/diboson.root";

  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }

  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeDYHVT(){

  string fileNameOut = "";
  vector<string> fileNameIn;

  // 1000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT1000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1200 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1200_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1200_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1200_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT1200.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1400_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT1400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT1600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1800 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1800_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1800_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT1800_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT1800.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT2000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT2000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT2000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT2000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 250 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT250__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT250__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT250__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT250.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT2600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT2600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT2600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT2600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT3000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT3000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT3000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT3000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3500 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT3500_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT3500_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT3500_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT3500.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 4000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT4000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT4000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT4000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT4000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 4500 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT4500_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT4500_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT4500_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT4500.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 450 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT450__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT450__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT450__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT450.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 5000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT5000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT5000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT5000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT5000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 500 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT500__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT500__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT500__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT500.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 700 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT700_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT700_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_DYHVT700_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/DYHVT700.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeGGFH(){

  vector<string> fileNameIn;
  string fileNameOut = "";  

  // 1000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH1000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH1000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1200 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH1200_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH1200.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH1400_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH1400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH1600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH1600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1800 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH1800_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH1800.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH2000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH2000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 200 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH200__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH200.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH2400_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH2400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH2600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH2600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH3000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH3000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 300 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH300__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH300.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH400_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 700 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH700_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH700.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 800 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFH800_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFH800.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeGGFR(){

  vector<string> fileNameIn;
  string fileNameOut = "";  

  // 1000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFR1000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFR1000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFR2000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFR2000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFR3000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFR3000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 300 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFR300__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFR300.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 4000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFR4000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFR4000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 5000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFR5000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFR5000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 6000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFR6000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFR6000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 700 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFR700_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFR700.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  return 0;
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeGGFRSG(){

  vector<string> fileNameIn;
  string fileNameOut = "";  

  // 1000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG1000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG1000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1200 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG1200_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG1200.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1500 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG1500_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG1500.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1800 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG1800_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG1800.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG2000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG2000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 200 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG200__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG200.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG2400_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG2400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG2600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG2600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG3000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG3000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 300 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG300__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG300.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3500 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG3500_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG3500.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 4000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG4000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG4000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG400__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 4500 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG4500_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG4500.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 5000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG5000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG5000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 700 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG700_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG700.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 800 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ggFRSG800_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/ggFRSG800.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  return 0;
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeTOP(){

  vector<string> fileNameIn;
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_SingleTop_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_ttBar_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_SingleTop_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_ttBar_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_SingleTop_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_ttBar_spin0.root");

  const string fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/top.root";

  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }

  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeVBFH(){

  vector<string> fileNameIn;
  string fileNameOut = "";

  // 1000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH1000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1200 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1200_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1200_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1200_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH1200.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1400_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH1400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH1600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1800 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1800_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1800_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH1800_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH1800.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH2000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH2000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH2000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH2000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 200 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH200__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH200__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH200__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH200.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH2400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH2400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH2400_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH2400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH2600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH2600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH2600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH2600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH3000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH3000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH3000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH3000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 300 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH300__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH300__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH300__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH300.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH400_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 700 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH700_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH700_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH700_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH700.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 800 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH800_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH800_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFH800_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFH800.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeVBFHVT(){

  vector<string> fileNameIn;
  string fileNameOut = "";

  // 1000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT1000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1200 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1200_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1200_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1200_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT1200.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1500 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1500_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1500_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1500_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT1500.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 1800 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1800_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1800_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT1800_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT1800.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT2000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT2000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT2000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT2000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT2400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT2400_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT2400_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT2400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 250 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT250_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT250_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT250_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT250.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT2600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT2600_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT2600_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT2600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT3000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT3000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT3000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT3000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 300 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT300__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT300__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT300__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT300.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3500 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT3500_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT3500_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT3500_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT3500.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 4000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT4000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT4000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT4000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT4000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 400 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT400__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT400__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT400__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT400.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 5000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT5000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT5000_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT5000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT5000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 600 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT600__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT600__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT600__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT600.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 700 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT700__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT700__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT700__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT700.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 800 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT800__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT800__spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFHVT800__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFHVT800.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeVBFR(){

  vector<string> fileNameIn;
  string fileNameOut = "";

  // 1000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFR1000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFR1000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFR2000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFR2000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFR3000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFR3000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 300 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFR300__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFR300.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 4000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFR4000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFR4000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 5000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFR5000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFR5000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 6000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFR6000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFR6000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 700 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFR700_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFR700.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeVBFRSG(){

  vector<string> fileNameIn;
  string fileNameOut = "";

  // 1000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFRSG1000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFRSG1000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 2000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFRSG2000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFRSG2000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 3000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFRSG3000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFRSG3000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 300 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFRSG300__spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFRSG300.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 4000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFRSG4000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFRSG4000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 5000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFRSG5000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFRSG5000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 6000 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFRSG6000_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFRSG6000.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  // 700 GeV
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_VBFRSG700_spin0.root");
  fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/VBFRSG700.root";
  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }
  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeWJETS(){

  vector<string> fileNameIn;
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_Wjets_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_Wjets_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_Wjets_spin0.root");

  const string fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/Wjets.root";

  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }

  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

int mergeZJETS(){

  vector<string> fileNameIn;
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16a_RNNCut0p8_pDNN_SelSpin0/FlatTree_Zjets_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16d_RNNCut0p8_pDNN_SelSpin0/FlatTree_Zjets_spin0.root");
  fileNameIn.push_back("/nfs/kloe/einstein2/enricojr/data/2019-11-04/mc16e_RNNCut0p8_pDNN_SelSpin0/FlatTree_Zjets_spin0.root");

  const string fileNameOut = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/merged/Zjets.root";

  if(merge(fileNameIn, fileNameOut)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge files" << endl;
    return 1;
  }

  fileNameIn.clear();

  return 0; 
}

/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/
/***********//***********//***********//***********//***********//***********//***********//***********//***********//***********/

#endif
