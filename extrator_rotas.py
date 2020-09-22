# -*- coding: utf-8 -*-
"""
TIRA AS ROTAS DO TXT

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



index= easygui.fileopenbox()
index2= easygui.fileopenbox()
# user_dir = easygui.diropenbox()

# Path_name = user_dir
# Path_file = os.listdir(Path_name)

indexo = open(index,'r',encoding='utf8')
indexo2 = open(index2,'r',encoding='utf8')

indexofix=[]
for i in indexo:
    indexofix.append(i) 
    
indexofix2=[]
for i in indexo2:
    indexofix2.append(i) 

indexr = []


c=0
a=0
veriq = (" ").join(re.findall("[A-Za-z]\w+",indexofix[c]))
for idx in indexofix2:
    if veriq in idx:
        indexr.append(idx)
        break
    else:
        indexr.append(idx)
        a+=1
    # if indexofix2[a] in indexr:
    #     break
        
    # else:
    #     a+=1
co =0
rota = []

cidade=veriq+".txt"

for i in indexr:
    check1 = re.findall("[BR\s]+[0-9]{5}",indexr[co])
    check2 = re.findall("([A-Z]{2})+[0-9]{3}",indexr[co])
    if not check1:
        if check2:
            rota.append(check2)
            with open(cidade,"a",encoding="utf-8") as escritor:
                escritor.write()
            
                
# print(a)
# ex = len(indexofix2)-a
# a+=1
# for i in range (ex):
  
#TIP re.findall("[BR\s]+[0-9]{5}",indexofix2[1])
#TIP >>> desconsiderar >> re.findall("[BR]+[0-9]{3}",indexofix2[9])
#TIP re.findall("([A-Z]{2})+[0-9]{3}",indexofix2[9])
    
  
    
# for item in Path_file:
#     file = os.path.join(Path_name,item)
#     rota = open(file,'r',encoding='utf8')