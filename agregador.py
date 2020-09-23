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

import re
from easygui import *

import openpyxl
from openpyxl import load_workbook
import pandas as pd

import shutil
from shutil import copyfile


data = easygui.fileopenbox("Escolha o arquivo de orientacao",default="*.xlsx")
arq = pd.read_excel(data,0)

arq.loc[1][0]