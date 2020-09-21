# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:53:02 2020

@author: glpyz
"""

import datetime
import easygui
import os, glob
import os.path
import sys
import glob
from os import *

import os.path
import easygui
import sys
import glob
import shutil
import os
from os import *
from shutil import copyfile

user_dir = easygui.diropenbox()

Path_name = user_dir
Path_file = os.listdir(Path_name)

dt_id = easygui.enterbox(msg='Enter something.', title=' ', default='', strip=True)

dt_id = dt_id.split(',0')


print (Path_file)
print(("\n {} \n").format((len(Path_file))))

files =[]
dt = []

# for i in Path_file:
#     files.append(os.path.join(Path_name,i))

for x in Path_file:
    
    dt.append(x.split(".")[0])

checkok=[]
c = 0
for z in dt_id:
    if z in dt[c]:
        print("{}".format(z))
        checkok.append(z)
        c+=1
    else:
        print("\n{} no".format(z))
        c+=1
        
for z in dt_id:
    try:
        if str(z) in dt:
            arq = z+".html"
            arq = os.path.join(Path_name,arq)
            shutil.move(arq,os.path.join(Path_name,"un"))
    except:
        print("error")
        pass
        