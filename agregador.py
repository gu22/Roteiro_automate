# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:30:27 2020

@author: glpyz

AGREGAR AS ROTAS 

"""
import datetime
import easygui
import os, glob
import os.path
import sys
import glob
import csv
import re
from easygui import *

import openpyxl
from openpyxl import load_workbook
import pandas as pd

import shutil
from shutil import copyfile


data = easygui.fileopenbox("Escolha o arquivo de orientacao, xmlx",default="*.xlsx")
data2 = easygui.fileopenbox("Escolha de verificação, txt",default="*.txt")


arq = pd.read_excel(data,0)

cat = []
with open(data2,"r",encoding=("utf-8")) as txt:
    
    for i in txt:
        cat.append(i)
 
    
verificador = []
for i in cat:
    add = (" ").join(re.findall("[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]+[^A-Z0-9]{2}\w+",i))
    verificador.append(add)    
# for i in range(len(arq.index)):
#     for g in cat:
#         if arq.loc[i][0] in verificador

# arq = open(data,"r",encoding='utf-8')
# print(arq.read())
# print("\n")

#arq.loc[1][0]
# arq.close()