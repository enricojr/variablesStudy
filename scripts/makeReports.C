#include "../includes/makeReport.hpp"

int makeReports(){

  if(makeReport("merged", "ggF")){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make report for merged ggF" << endl;
    return 1;
  }
  
  if(makeReport("resolved", "ggF")){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make report for resolved ggF" << endl;
    return 1;
  }
  
  if(makeReport("merged", "VBF")){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make report for merged VBF" << endl;
    return 1;
  }
  
  if(makeReport("resolved", "VBF")){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make report for resolved VBF" << endl;
    return 1;
  }

  if(makeCompilationScript()){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! cannot make compilation script" << endl;
    return 1;
  }
  
  return 0;
}
