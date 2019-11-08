#include "../includes/makeReport.hpp"

int makeReports_2variables(){

  if(makeReport("merged", "ggF", 2)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make report for merged ggF" << endl;
    return 1;
  }
  
  if(makeReport("resolved", "ggF", 2)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make report for resolved ggF" << endl;
    return 1;
  }
  
  if(makeReport("merged", "VBF", 2)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make report for merged VBF" << endl;
    return 1;
  }
  
  if(makeReport("resolved", "VBF", 2)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make report for resolved VBF" << endl;
    return 1;
  }

  if(makeCompilationScript(2)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make compilation script" << endl;
    return 1;
  }
  
  return 0;
}
