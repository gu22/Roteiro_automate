# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:44:32 2020

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

dnit = easygui.fileopenbox("Arquivo do DNIT")
remessas = easygui.fileopenbox("Arquivo Remessas")


e1 = 'MT'
e2 = 'GO'
e3 = 'RO'

cidades = []

with open(remessas,"r",encoding=('utf-8')) as wr:
    for i in wr:
        # sl = i.split(":")[0]
        # cidades.append(unidecode(sl))
        cidades.append(unidecode(i))

dnit_ex = []
with open(dnit,"r",encoding=('utf-8')) as wr:
    for i in wr:
        #if (e1 or e2 or e3) in i:
           
            dnit_ex.append(unidecode(i))

cidade_ex = []
for i in cidades:
    valor = (((" ").join(re.findall("[A-Za-z]\w+",i))))
    cidade_ex.append(valor)


cod_dnit = []    
for i in cidade_ex:
    
    for x in dnit_ex:
        if i in x:
        # y = x.split(" ")
        # y = (" ").join(i[2:(len(y)+1)])
        # y = re.findall("[A-Za-z]\w+",y)
        # if i == y:    
            cod = x.split(":")[0]
            # cod = x
            cod_dnit.append("{}:{}".format(i,cod))

print(cod_dnit)

with open(".Codigos_DNIT_CUI.txt","a",encoding=('utf-8')) as wr:
    for i in cod_dnit:
        wr.write(i)
        wr.write('\n')
        
