# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:48:36 2020

@author: glpyz
"""


import easygui
import time



import openpyxl
from openpyxl import load_workbook
import pandas as pd
from unidecode import unidecode

## lendo dados

data = easygui.fileopenbox("Escolha o arquivo de orientacao, xmlx",default="*.xlsx")

tabela = pd.read_excel(data,1)

index = len(tabela.index)

arq = []

for i in range(index):
    z = tabela.iloc[i][0]
    arq.append(unidecode(z))
    
with open(".arquivos.txt","a",encoding=("utf-8")) as wr:
    for i in arq:
        wr.write(i)
        wr.write('\n')
        
        
    