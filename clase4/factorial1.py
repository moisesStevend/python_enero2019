#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:04:14 2019

@author: stevend
"""

#el factorial de un numero cualquiera
n=int(input('ingresa numero: '))
f=range(1,n+1)  # 6,5,4,3,2,1 

aux=1
for i in f:
    aux=aux*i

print('''
      el factorial de {} es {}
'''.format(n,aux))



