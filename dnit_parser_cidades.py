# -*- coding: utf-8 -*-
"""
TRANFORMA HTML EM TEXTO
"""
import easygui
from bs4 import BeautifulSoup
import tabulate
from tabulate import tabulate

import os.path
import easygui
import sys
import glob
import shutil
import os

from shutil import copyfile


#user_dir = easygui.diropenbox()
# filex= (easygui.fileopenbox())
fileo = easygui.fileopenbox()

# Path_name = user_dir
# Path_file = os.listdir(Path_name)

# contador = len(Path_file)

# for item in user_dir:
#     file = os.path.join(Path_name,item)
#     filex = open(file,'r',encoding='utf8')
# Path_name = user_dir
# Path_file = os.listdir(Path_name)
# Files = os.path.join(Path_name,Path_file)

# with open(filex,"r") as html:
#     pass
    

#file = open(filex,encoding='utf8')

# file2 = open("D:\gusan\Documents\PROGRAMAÇÃO\GitHub\beautifulsoup_testes\parse_html.html","r")

file =  open(fileo,"r",encoding='utf-8')

soup = BeautifulSoup(file,'html.parser')

# # print(soup.prettify())
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
list(soup.children)
# print("\n yyyyyyyy")
# print([type(item) for item in list(soup.children)])

# html = list(soup.children)

html = soup.find_all('li',class_="active-result")

#loc1 = soup.find_all('a',class_="reference external")
# loc2 = soup.find_all('b')
    # dt = item
    # dt = dt.split(".")[0]
text =[]
# text2 =[]
c = 0
# filedt= ((os.path.join(Path_name,dt)+'.txt'))
for i in html:
    text.append(str(html[c].string))
# text2.append(str(loc[c]))

    with open('CIDADES_DESTINO_DNIT_OK.txt', "a", encoding="utf-8") as escritor:
        try:
            escritor.write("{}:{}".format((c+1),text[c]))
            escritor.write("\n")
        except:
            pass
    c+=1
    
print (text)
# #loc = soup.find('a')
file.close()  
# table = [["%s"%text[0],"%s"%text[1]],["%s"%text2[0],"%s"%text2[1]]]
# "{}.txt".format(dt)

# print(text)
# print(text2)
# print('/n')
# print(tabulate(table))
# # print(loc)
# # print(loc2)

# with open("Geral.txt","a") as geral:
#     geral.write(";".join(text))
#     geral.write('\n')
#     geral.write((tabulate(table)))
    
    
# with open("log.txt","w") as log:
#     log.write(str(text))
#     log.write("\n")
#     log.write(str(text2))
#     log.write("\n")
    
# 'oi, {} {}'.format(x[0][0],x)
# Out[112]: "oi, a [['a', 11], ['b', 22]]"

# xxx = '{} tentaremos uma tentativa'

# xxx
# Out[114]: '{} tentaremos uma tentativa'

# xxx.format("Viva! ")
# Out[115]: 'Viva!  tentaremos uma tentativa'

# xxx.format("Viva!")
# Out[116]: 'Viva! tentaremos uma tentativa'
