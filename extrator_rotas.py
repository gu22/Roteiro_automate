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


# cidade dt
index= easygui.fileopenbox()

# rotas para extrair
index2= easygui.fileopenbox()


# user_dir = easygui.diropenbox()
# Path_name = user_dir
# Path_file = os.listdir(Path_name)

index_cdt = open(index,'r',encoding='utf8')
index_ex = open(index2,'r',encoding='utf8')

index_busca=[]
for i in index_cdt:
    index_busca.append(i) 
    
index_acha=[]
for i in index_ex:
    index_acha.append(i) 

indexr = []


c=0
a=0

# Pega o nome da cicade 
veriq = (" ").join(re.findall("[A-Za-z]\w+",index_busca[c]))

# extraido os textos
for idx in index_acha:
    if veriq in idx:
        indexr.append(idx)
        break
    else:
        indexr.append(idx)
        a+=1
    # if index_acha[a] in indexr:
    #     break
        
    # else:
    #     a+=1
co =0
rota = []
adeq =[]

#nome arquivo
cidade= veriq
arq_city = cidade +".txt"

# extaindo as rotas
for i in indexr:
    check1 = re.findall("[BR\s]+[0-9]{5}",i)
    check2 = re.findall("(([A-Z]{2})+[0-9]{3})",i)
    if not check1:
        if check2:
            rota.append(check2)
            adeq.append(check2[0][0])
            print (check2)
            with open(cidade,"a",encoding="utf-8") as escritor:
                escritor.write(check2[0][0])
                escritor.write("\n")
            co+=1
    else:
        rota.append(check1)
        print (check1)
        with open(cidade,"a",encoding="utf-8") as escritor:
            escritor.write(check1[0])
            escritor.write("\n")
        co+=1
            
print(rota)

rotas =[]

# organizando as rotas
for item in adeq:
    text = item[0:2]+"-"+item[2:5]
    rotas.append(text)

with open("ROTAS_ok.txt","a",encoding="utf-8") as escritor:
    escritor.write((cidade+";"))
    escritor.write(",".join(rotas))
    escritor.write("\n")

index_cdt.close()
index_ex.close()

            
                
# print(a)
# ex = len(index_acha)-a
# a+=1
# for i in range (ex):
  
#TIP re.findall("[BR\s]+[0-9]{5}",index_acha[1])
#TIP >>> desconsiderar >> re.findall("[BR]+[0-9]{3}",index_acha[9])
#TIP re.findall("([A-Z]{2})+[0-9]{3}",index_acha[9])
    
  
    
# for item in Path_file:
#     file = os.path.join(Path_name,item)
#     rota = open(file,'r',encoding='utf8')