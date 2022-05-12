# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:17:51 2022

@author: ANDERSON
"""
lista2=[]
lista3=[]
lista=["R2",
       "R2",
       "R3",
       "S1",
       "S2",
       "S3",]

for item in lista:
    if "R" in item:
        lista2.append(item)
    else:
        lista3.append(item)
        