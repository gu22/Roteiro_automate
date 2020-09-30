# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:41:06 2020

@author: glpyz
"""

from unidecode import unidecode
a = input()

trad=[]
for i in a:
    trad.append(unidecode(a))
    