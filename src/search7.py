#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:48:04 2022

@author: anselmo

DEIXE O USUÁRIO ESOLHER O NOME DO ARQUIVO

Usando try / except

"""

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("file connot be opened")
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count += 1
print(f"There were {count} subjects lines in {fname}")



