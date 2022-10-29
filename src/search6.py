#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:48:04 2022

@author: anselmo

DEIXE O USUÁRIO ESOLHER O NOME DO ARQUIVO

Consultando strigns que conté, '@uct.ac.za' (Universidade de Cape town na 
                                             África do SUl)

"""
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count+1
print(f"There were {count} sinject lines in {fname}")



