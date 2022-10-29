#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:48:04 2022

@author: anselmo

DEIXE O USUÁRIO ESOLHER O NOME DO ARQUIVO

Consultando strigns que conté, '@uct.ac.za' (Universidade de Cape town na 
                                             África do SUl)

"""

fhand = open('..//src/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1 :
        continue
    pontos = line.find(":")
    print(pontos)



