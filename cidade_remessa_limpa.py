# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:32:58 2020

@author: glpyz
"""
import os.path
import easygui
import sys
import glob
import shutil
import os
import easygui
import re
from shutil import copyfile
from unidecode import unidecode

import openpyxl
from openpyxl import load_workbook
import pandas as pd
from unidecode import unidecode

file = easygui.fileopenbox("XLSX com cidades")
# file2 = easygui.fileopenbox("XLSX com remessas")

entrada = pd.read_excel(file,4)

# remessas = pd.read_excel(file2,0)

index = range(len(entrada.index))

tenho = []

for i in index:
    try:
        tem = (unidecode(entrada.loc[i][0]))
    except:
        break
    
    for x in range(len(entrada.index)):
        vouquerer =(unidecode(entrada.loc[x][1]))
        quero = (" ").join(( re.findall("[A-Za-z]\w+",vouquerer)))
        pego = ((entrada.loc[x][2]))
        
        if quero == tem:
            agora = "{}:{}".format(quero,pego)
            tenho.append(agora)
            
with open("AgoraSim.txt","a",encoding=("utf-8")) as wr:
        for o in tenho:
            wr.write(o)
            wr.write("\n")            
