#ifndef MAKEREPORT_HPP
#define MAKEREPORT_HPP

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

string getFileName(const string selectionType, // merged or resolved
		   const string processType){  // ggF or VBF
  return "/nfs/kloe/einstein2/enricojr/data/2019-11-04/reports/" + selectionType + "_" + processType + "/main.tex";
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

string getTitle(const string selectionType, // merged or resolved
		const string processType){  // ggF or VBF
  return "DNN studies, " + selectionType + " " + processType;
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

string getShortTitle(const string selectionType, // merged or resolved
		     const string processType){  // ggF or VBF
  return selectionType + " " + processType;
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

string getDataFolder(const string selectionType, // merged or resolved
		     const string processType){  // ggF or VBF
  return "/nfs/kloe/einstein2/enricojr/data/2019-11-04/pandas_" + selectionType + "_" + processType + "/";
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

string getPlotsFolder(const string selectionType, // merged or resolved
		      const string processType){  // ggF or VBF
  return "/nfs/kloe/einstein2/enricojr/data/2019-11-04/reports/" + selectionType + "_" + processType + "/";
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

vector<string> getVarSet(const string selectionType){
  vector<string> varSet;
  if(selectionType == "merged"){
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET");
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET,l1\\_pt");
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET,l1\\_e");
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET,l2\\_pt");
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET,l2\\_e");
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET,fat\\_jet\\_D2");
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET,fat\\_jet\\_C2");
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET,ratio\\_merged");
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET,ratio\\_resolved");
    varSet.push_back("NJETS,l1\\_eta,l2\\_eta,l2\\_phi,l1\\_phi,ll\\_pt,\\\\fat\\_jet\\_eta,fat\\_jet\\_phi,fat\\_jet\\_pt,fat\\_jet\\_E,MET,fat\\_jet\\_ntrack");
  }
  else if(selectionType == "resolved"){
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j2pt");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j1M");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j1pt");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,l1\\_pt");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,l2\\_pt");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,l2\\_e");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,ratio\\_resolved");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,l1\\_e");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j2NTracks");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j1NTracks");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j2M");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,ratio\\_merged");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,detajj");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j1eta");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j2eta");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j2phi");
    varSet.push_back("NJETS,l2\\_eta,l1\\_eta,l1\\_phi,l2\\_phi,ll\\_pt,\\\\jj\\_eta,jj\\_phi,jj\\_pt,MET,jj\\_j1phi");
  }
  else{
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - unknown selection type = " << selectionType << endl;
  }
  return varSet;
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

void writeHeader(ofstream &file,
		 const string title,
		 const string shortTitle){

  file << "\\documentclass{beamer}" << endl;
  file << "\\mode<presentation> {" << endl;
  file << "\\usetheme{PaloAlto}" << endl;
  file << "\\setbeamertemplate{footline}[page number]" << endl;
  file << "\\setbeamertemplate{navigation symbols}{}" << endl;
  file << "}" << endl;
  file << "\\usepackage{graphicx}" << endl;
  file << "\\usepackage{booktabs}" << endl;
  file << "\\usepackage{tkz-graph}" << endl;
  file << "\\GraphInit[vstyle = Shade]" << endl;
  file << "\\tikzset{" << endl;
  file << "  LabelStyle/.style = { rectangle, rounded corners, draw," << endl;
  file << "                        minimum width = 2em, fill = yellow!50," << endl;
  file << "                        text = red, font = \\bfseries }," << endl;
  file << "  VertexStyle/.append style = { inner sep=5pt," << endl;
  file << "                                font = \\normalsize\\bfseries}," << endl;
  file << "  EdgeStyle/.append style = {->, bend left} }" << endl;
  file << "\\usetikzlibrary {positioning}" << endl;
  file << "\\definecolor {processblue}{cmyk}{0.96,0,0,0}" << endl;
  file << "\\title[" << shortTitle << "]{" << title << "}" << endl;
  file << "\\author{E.J. Schioppa}" << endl;
  file << "\\institute[Unisalento]" << endl;
  file << "{" << endl;
  file << "Unisalento\\\\" << endl;
  file << "\\medskip" << endl;
  file << "}" << endl;
  file << "\\date{\\today}" << endl;
  file << "\\begin{document}" << endl;
  file << "\\begin{frame}" << endl;
  file << "\\titlepage" << endl;
  file << "\\end{frame}" << endl;

  return ;
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

int copyPlotsToLocal(const string dataFolder,
		     const vector<string> varSet,
		     const string plotsFolder){
  for(unsigned int i=0; i<varSet.size(); i++){
    stringstream ii_ss;
    ii_ss << i;
    const string trainFolder = dataFolder + "train/" + "llqqDNN_64_1024_4_0.0003_VarSet" + ii_ss.str();
    const string testFolder = dataFolder + "test/" + "llqqDNN_64_1024_4_0.0003_VarSet" + ii_ss.str();
    string commandTrain = "cp " + trainFolder + "/Loss.png " + plotsFolder + "Loss" + ii_ss.str() + ".png";
    if(system(commandTrain.c_str())){
      cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot copy train plots" << endl;
      return 1;
    }
    commandTrain = "cp " + trainFolder + "/Accuracy.png " + plotsFolder + "Accuracy" + ii_ss.str() + ".png";
    if(system(commandTrain.c_str())){
      cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot copy train plots" << endl;
      return 1;
    }
    string commandTest = "cp " + testFolder + "/ROC.png " + plotsFolder + "ROC" + ii_ss.str() + ".png";
    if(system(commandTest.c_str())){
      cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot copy test plots" << endl;
      return 1;
    }
    commandTest = "cp " + testFolder + "/ConfusionMatrix.png " + plotsFolder + "ConfusionMatrix" + ii_ss.str() + ".png";
    if(system(commandTest.c_str())){
      cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot copy test plots" << endl;
      return 1;
    }
    commandTest = "cp " + testFolder + "/MC_Data_TrainTest_Score_log.png " + plotsFolder + "Score" + ii_ss.str() + ".png";
    if(system(commandTest.c_str())){
      cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot copy test plots" << endl;
      return 1;
    }
  }
  return 0;
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

void writeCore(ofstream &file,
	       const string selectionType, // merged or resolved
	       const string processType){  // ggF or VBF

  const string dataFolder = getDataFolder(selectionType, processType);
  vector<string> varSet = getVarSet(selectionType);
  const string plotsFolder = getPlotsFolder(selectionType, processType);
  if(copyPlotsToLocal(dataFolder, varSet, plotsFolder)){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot copy plots for " << selectionType << " " << processType << endl;
    return 1;
  }
  for(unsigned int i=0; i<varSet.size(); i++){
    stringstream i_ss;
    i_ss << i;
    file << "\\begin{frame}{Training}" << endl;
    file << varSet[i] << endl;
    file << "\\begin{figure}[H]" << endl;
    file << "  \\centering" << endl;
    file << "  \\includegraphics[width=0.45\\textwidth]{Loss" << i_ss.str() << ".png}" << endl;
    file << "  \\includegraphics[width=0.45\\textwidth]{Accuracy" << i_ss.str() << ".png}" << endl;
    file << "\\end{figure}" << endl;
    file << "\\end{frame}" << endl;    
    file << "\\begin{frame}{Test}" << endl;
    file << varSet[i] << endl;
    file << "\\begin{figure}[H]" << endl;
    file << "  \\centering" << endl;
    file << "  \\includegraphics[width=0.45\\textwidth]{ROC" << i_ss.str() << ".png}" << endl;
    file << "  \\includegraphics[width=0.45\\textwidth]{ConfusionMatrix" << i_ss.str() << ".png}" << endl;
    file << "  \\includegraphics[width=0.45\\textwidth]{Score" << i_ss.str() << ".png}" << endl;
    file << "\\end{figure}" << endl;
    file << "\\end{frame}" << endl;    
  }
  varSet.clear();
  return ;
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

void writeFooter(ofstream &file){
  file << "\\end{document}" << endl;
  return ;
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

int makeReport(const string selectionType, // merged or resolved
	       const string processType){  // ggF or VBF

  const string fileName = getFileName(selectionType, processType);
  cout << __PRETTY_FUNCTION__ << ": (over)writing file " << fileName << endl;

  ofstream file(fileName.c_str());
  if(!file){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot open file " << fileName << endl;
    return 1;
  }

  writeHeader(file, getTitle(selectionType, processType), getShortTitle(selectionType, processType));
  writeCore(file, selectionType, processType);
  writeFooter(file);
  
  file.close();
  
  return 0;
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

int makeCompilationScript(){

  const string fileName = "/nfs/kloe/einstein2/enricojr/data/2019-11-04/reports/compile.sh";
  cout << __PRETTY_FUNCTION__ << ": (over)writing file " << fileName << endl;
  
  ofstream file(fileName.c_str());
  if(!file){
    cout << __PRETTY_FUNCTION__ << ": ERROR!!! - cannot open file " << fileName << endl;
    return 1;
  }

  file << "cd merged_ggF" << endl;
  file << "pdflatex main.tex" << endl;
  file << "pdflatex main.tex" << endl;
  file << "rm -rf *aux" << endl;
  file << "rm -rf *log" << endl;
  file << "rm -rf *nav" << endl;
  file << "rm -rf *out" << endl;
  file << "rm -rf *snm" << endl;
  file << "rm -rf *toc" << endl;
  file << "cd -" << endl;
  
  file << "cd resolved_ggF" << endl;
  file << "pdflatex main.tex" << endl;
  file << "pdflatex main.tex" << endl;
  file << "rm -rf *aux" << endl;
  file << "rm -rf *log" << endl;
  file << "rm -rf *nav" << endl;
  file << "rm -rf *out" << endl;
  file << "rm -rf *snm" << endl;
  file << "rm -rf *toc" << endl;
  file << "cd -" << endl;
  
  file << "cd merged_VBF" << endl;
  file << "pdflatex main.tex" << endl;
  file << "pdflatex main.tex" << endl;
  file << "rm -rf *aux" << endl;
  file << "rm -rf *log" << endl;
  file << "rm -rf *nav" << endl;
  file << "rm -rf *out" << endl;
  file << "rm -rf *snm" << endl;
  file << "rm -rf *toc" << endl;
  file << "cd -" << endl;
  
  file << "cd resolved_VBF" << endl;
  file << "pdflatex main.tex" << endl;
  file << "pdflatex main.tex" << endl;
  file << "rm -rf *aux" << endl;
  file << "rm -rf *log" << endl;
  file << "rm -rf *nav" << endl;
  file << "rm -rf *out" << endl;
  file << "rm -rf *snm" << endl;
  file << "rm -rf *toc" << endl;
  file << "cd -" << endl;
  
  file.close();
  
  return 0;
}

/*********//*********//*********//*********//*********//*********//*********//*********//*********/
/*********//*********//*********//*********//*********//*********//*********//*********//*********/

#endif
