#!/bin/python
from colorama import init, Fore, Back, Style
init(autoreset=True)
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
# print(Fore.RED + 'some red text')
# print(Back.YELLOW + 'some yellow background')
# print(Style.DIM + 'some dim text')

import numpy as np
np.random.seed(123)

import pandas as pd
import sklearn.utils
import os

channelDic = {'Zjets':0, 'Signal':1, 'Diboson':2, 'Top':3, 'VBF':5, 'ggF':6, 'Data':10}

def Randomizing(df,drop=True):
    df = sklearn.utils.shuffle(df,random_state=123) #'123' is the random seed
    df = df.reset_index(drop=drop)# drop=True does not allow the reset_index to insert a new column with the suffled index
    return df

def makeEqualSizeDFs(listofDFs):
    nEventsMap = []
    finalListofDfs=[]

    for idf in listofDFs:
        nEventsMap += [idf.shape[0]]

    minEvents = min(nEventsMap)

    print ("\tMaking all samples have equal number of events. Min is", minEvents)
    for idf in listofDFs:
        finalListofDfs += [idf[:minEvents]]

    totEvents = np.sum([final_df.shape[0] for final_df in finalListofDfs])

    return finalListofDfs, totEvents, minEvents

def getDFEvents(path,f,tag):
    listFiles = os.listdir(path) # returns list of files under path

    found = False
    for i in listFiles:
        # print ('look for ',f,' in',i,' under path',path)
        if (f in i) and (tag in i) and ('.pkl' in i) and (os.path.isfile(path+i)):
            found = True
            df = pd.read_pickle(path+i)
            print ('{:<46}{:<15}'.format("Events in "+i, Fore.GREEN+str(df.shape[0])))
            return df

    if found==False:
        print ("file",f ,"does not exist. Be sure you have already created it with the -c option")
        quit()



def checkCreateDir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)
        return Fore.RED+'...created'
    else:
        return Fore.RED+'...already there'
