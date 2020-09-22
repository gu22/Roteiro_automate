# -*- coding: utf-8 -*-
import datetime
import easygui
import os, glob
import os.path
import sys
import glob


from easygui import *

import openpyxl
from openpyxl import load_workbook
import pandas as pd

import shutil
from shutil import copyfile

data= (easygui.fileopenbox())

arq = pd.read_excel(data,1)

cidade=[]
dtx=[]



#escritor = open('cch_dt.txt','a',encoding="utf-8")

material= "ROUNDUP ORIGINAL DI L"
for i in range(1871):
    try:
        if material in arq.loc[i][6]:
            if not arq.loc[i][22] in cidade:
               cidade.append( arq.loc[i][22])
               if not  arq.loc[i][9] in dtx:
                   dtx.append(arq.loc[i][9])
                   print("<<< Entrou {} {} >>>>\n".format((arq.loc[i][22]),(arq.loc[i][9])))
                   #escritor.write("{} : {} ,{} \n".format(i,(arq.loc[i][22]),(arq.loc[i][9])))
                   with open("cch_dt.txt", "a",encoding="utf-8") as escritor:
                        escritor.write("{} : {} \t{} \n".format(i,(arq.loc[i][22]),(arq.loc[i][9])))
                   #     #print("{} : {} ,{} \n".format(i,(arq.loc[i][22]),(arq.loc[i][9])))
                   #     escritor.write("Teste")
               else:
                   ab = i+1
                   dtx.append(arq.loc[ab][9])
                   print("<<< Entrou {} {} >>>>\n".format((arq.loc[i][22]),(arq.loc[ab][9])))
                   #escritor.write("{} : {} ,{} \n".format(i,(arq.loc[i][22]),(arq.loc[ab][9])))
       
                   with open("cch_dt.txt","a",encoding="utf-8") as escritor:
                        escritor.write("{} : {} \t{} \n".format(i,(arq.loc[i][22]),(arq.loc[ab][9])))
        else:
            print("Passou {}".format(arq.loc[i][22]))
    except:
        print(arq.loc[i][22])
        
#escritor.close()
        