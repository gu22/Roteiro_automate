# -*- coding: utf-8 -*-

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
filex= (easygui.fileopenbox())
filex = open(filex,'r',encoding='utf8')
# Path_name = user_dir
# Path_file = os.listdir(Path_name)
# Files = os.path.join(Path_name,Path_file)

# with open(filex,"r") as html:
#     pass
    

#file = open(filex,encoding='utf8')

# file2 = open("D:\gusan\Documents\PROGRAMAÇÃO\GitHub\beautifulsoup_testes\parse_html.html","r")


soup = BeautifulSoup(filex,'html.parser')

# print(soup.prettify())
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
print(list(soup.children))
print("\n yyyyyyyy")
print([type(item) for item in list(soup.children)])

html = list(soup.children)

loc = soup.find_all('span',class_="alkDirectionCol")

#loc1 = soup.find_all('a',class_="reference external")
# loc2 = soup.find_all('b')

text =[]
# text2 =[]
c = 0
for i in loc:
    text.append(str(loc[c].string))
    # text2.append(str(loc[c]))
    c+=1
# #loc = soup.find('a')

# table = [["%s"%text[0],"%s"%text[1]],["%s"%text2[0],"%s"%text2[1]]]


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
