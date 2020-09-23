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
index= easygui.fileopenbox("Escolha o arquivo de orientacao",default="*.txt")

# rotas para extrair
#index2= easygui.fileopenbox(default="*.txt")


if 'SECO' in index:
    material = "SECO"
else:
    material = "LIQUIDO"
    
user_dir = easygui.diropenbox("escolha pasta com os txt de rotas")

Path_name = user_dir
Path_file = os.listdir(Path_name)
# user_dir = easygui.diropenbox()
# Path_name = user_dir
# Path_file = os.listdir(Path_name)
index_cdt = open(index,'r',encoding='utf8')

index_busca=[]
for i in index_cdt:
    index_busca.append(i)
    
   
    
c=0
a=0   
for data in Path_file:
    file = os.path.join(Path_name,data)
    index_ex = open(file,'r',encoding='utf8')
    
    
    
     
        
    index_acha=[]
    for i in index_ex:
        index_acha.append(i) 
    
    indexr = []
    
    
   
    
    # Pega o nome da cicade 
    veriq = (" ").join(re.findall("[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]\w+",index_busca[c]))
    
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
    c+=1
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
                with open(arq_city,"a",encoding="utf-8") as escritor:
                    escritor.write(check2[0][0])
                    escritor.write("\n")
                
        else:
            rota.append(check1)
            print (check1)
            with open(arq_city,"a",encoding="utf-8") as escritor:
                escritor.write(check1[0])
                escritor.write("\n")
            
                
    print(rota)
    
    rotas =[]
    
    # organizando as rotas
    for item in adeq:
        text = item[0:2]+"-"+item[2:5]
        rotas.append(text)
    
    with open((".ROTAS_{}.txt".format(material)),"a",encoding="utf-8") as escritor:
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