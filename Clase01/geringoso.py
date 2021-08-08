# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 01:35:57 2021

@author: maru8
"""


cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    if c =='a' :
        capadepenapa = capadepenapa + c + 'pa'
    elif c =='e' :
        capadepenapa = capadepenapa + c + 'pe'
    elif c =='i' :
        capadepenapa = capadepenapa + c + 'pi'
    elif c =='o' :
        capadepenapa = capadepenapa + c + 'po'
    elif c =='u' :
        capadepenapa = capadepenapa + c + 'pu'
    else:
        capadepenapa = capadepenapa + c
print(capadepenapa)
# capadepenapa
#Geperipingoposopo