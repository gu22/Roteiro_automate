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

from unidecode import unidecode

# data = easygui.fileopenbox("Escolha o arquivo de orientacao, xmlx",default="*.xlsx")
data = easygui.fileopenbox("Escolha o arquivo de orientacao, .arquivo",default="*.txt")
data2 = easygui.fileopenbox("Escolha de verificação, txt",default="*.txt")


# arq = pd.read_excel(data,0)
regiao = "MT"
regiao2 = "GO"
regiao3 = "RO"
cat = []
with open(data2,"r",encoding=("utf-8")) as txt:
    
    for i in txt:
        # if (regiao or regiao2 or regiao3) in i:
            
      cat.append(unidecode(i))

cidade = []
with open(data,"r",encoding=("utf-8")) as txt:
    
    for i in txt:
        i = ((" ").join(re.findall("[A-Za-z]\w+",i)))
        cidade.append(unidecode(i))
    

    
verificador = {}
# for i in cat:
#     i = unidecode(i)
#     add = (" ").join(re.findall("[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]+[^A-Z0-9]{2}\w+",i))
#     if ";BR" in add:
#         add = add.split(";BR")[0]
#         verificador.append(add)
#     else:
#         verificador.append(add)

for i in cat:
    i = unidecode(i)
    slt = re.findall(('[A-Z]{2}\s'), i)
    slt = str(slt[0])
    sl = i.split((":{}").format(slt))
    
    sl2 = (((" ").join(re.findall("[A-Za-z]\w+",sl[1]))))
    # add = (" ").join(re.findall("[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]+[^A-Z0-9]{2}\w+",i))
    # if ";BR" in add:
    #     add = add.split(";BR")[0]
    #     verificador.append(add)
    # else:
    #     verificador.append(add)
    key = sl2
    vl = sl[0]
    
    verificador.update({key:vl})

contador = 0  
final = []  
contador = 0
con = 0

# pandac = len(arq.index)

# for i in range(len(verificador)):
    
#     for x in range(pandac):
#         if unidecode(arq.loc[x][0]) == verificador[i]:
#             final.append(cat[i])
#             print(verificador[i])
print(verificador)
            
for i in verificador:
    # c=0
    for x in cidade:
        if x == i:
            ok = ("{}:{}").format((i),verificador[i])
            final.append(ok)
            print(i)
        
        # else:
        #     c+=0
            
        
    
    
    
    # #for g in verificador:
    #     # if arq.loc[i][0] == g:
    #         final.append(cat[contador])
            
    #         print("<<g: {} , cat: {} , contador: {} , arq: {}>>\n".format(g,(cat[contador]),contador,(arq.loc[i][0])))
        
    #     # else:
    #     #     try:
    #            print("<< g: {} , cat: {} , contador: {} , arq: {}>>\n".format(g,(cat[contador]),contador,(arq.loc[i][0])))
               
               
    #         # except: 
    #             final.append(cat[contador])
                
                # print("g: {} , cat: {} , contador: {} , arq: {}\n".format(g,(cat[contador]),contador,(arq.loc[i][0])))
    # contador+=1            
    # print("__panda {}, i {}__\n".format((arq.loc[i][0]),i))
                
            
with open("DNIT_cod_lon.txt","a",encoding=("utf-8")) as es:
    for i in final:
        es.write(i) 
        es.write("\n")           
            

# arq = open(data,"r",encoding='utf-8')
# print(arq.read())
# print("\n")

#arq.loc[1][0]
# arq.close()