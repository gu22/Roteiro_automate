# -*- coding: utf-8 -*-
"""
SEPARA DT PARA EXTRAÇÃO


"""


import datetime
import easygui
import os, glob
import os.path
import sys
import glob

import re
from easygui import *

import openpyxl
from openpyxl import load_workbook
import pandas as pd

import shutil
from shutil import copyfile
from unidecode import unidecode


data= (easygui.fileopenbox())
dnit_arq = (easygui.fileopenbox())

arq = pd.read_excel(data,0)




# mat = []
# with open("option.txt","r",encoding="utf-8") as option:
#     for i in option:
#         mat.append(i)

#escritor = open('cch_dt.txt','a',encoding="utf-8")

# material= "ROUNDUP ORIGINAL DI L"
#escolha= easygui.indexbox(choices = ("Seco","Liquido"))
     
# material = mat[escolha]
# material= re.findall('[A-Z]+',material)
# material = " ".join(material)

#material = mat[escolha]

cd = easygui.enterbox("Qual o nome cd")    

#range é todas as linha da tabela 

# 22 = cidade; 9 = dt; 0 = remessa
dnit_final = []
      
index = range(len(arq))
           
verifiq = []
dnit=[]
dnit_ext = open(dnit_arq,"r",encoding=('utf-8'))

for a in dnit_ext:
    dnit.append(a)

for i in index:
    estado = arq.loc[i][23]
    
    
    dnit_cidade = []
    codigo = []
    # try:
        # if material in arq.loc[i][6]:
    for b in dnit:
        if estado in b:
            
            dnit_cidade.append(unidecode(b))
            
    cidade = unidecode(arq.loc[i][22])
    
    for z in dnit_cidade:
        wd = z.split(" ")[1:]
        wd = (' ').join(wd)
        wd = (" ").join(re.findall("[A-Za-z]\w+",wd))
        if  cidade == wd:
            if not cidade in dnit_final:
                cod = z.split(":")[0]
                
                dnit_final.append("{}:{}".format(cidade,cod))
                    
            
    # except:
    #     print('ERRO')
    #     pass

dnit_ext.close()    
with open("DNIT_{}.txt".format(cd),"a",encoding=("utf-8")) as wr:
    for item in dnit_final:
        wr.write(item)
        wr.write("\n")