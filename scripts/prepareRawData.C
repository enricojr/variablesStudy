#include "../includes/prepareRawData.hpp"

int prepareRawData(){

  if(mergeDATA()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge data" << endl;
    return 1;
  }

  if(mergeDIBOSON()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge diboson" << endl;
    return 1;
  }

  if(mergeDYHVT()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge DYHVT" << endl;
    return 1;
  }

  if(mergeGGFH()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge GGFH" << endl;
    return 1;
  }

  if(mergeGGFR()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge GGFR" << endl;
    return 1;
  }

  if(mergeGGFRSG()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge GGFRSG" << endl;
    return 1;
  }

  if(mergeTOP()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge top" << endl;
    return 1;
  }

  if(mergeVBFH()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge VBFH" << endl;
    return 1;
  }

  if(mergeVBFHVT()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge VBFHVT" << endl;
    return 1;
  }

  if(mergeVBFR()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge VBFR" << endl;
    return 1;
  }

  if(mergeVBFRSG()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge VBFRSG" << endl;
    return 1;
  }

  if(mergeWJETS()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge Wjets" << endl;
    return 1;
  }

  if(mergeZJETS()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot merge Zjets" << endl;
    return 1;
  }

  return 0;
}
