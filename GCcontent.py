#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hanabillings
"""
"""
Calculates GC content of FASTA formatted sequence data.
Returns the ID of the sequence and its GC content
"""

import re

def getGCcontent():
    # /Users/hanabillings/Desktop/rosalind.txt on my computer lol
    fileLocation = input("please input your data file location")
    data = open(fileLocation)
    text = data.read()
    text = text.replace('\n','')
    txtRegex= re.compile(r'(Rosalind[_]\d+)')
    data = txtRegex.findall(text)
    GCRegex = re.compile(r'Rosalind[_]\d+(\w+)')
    GCdata = GCRegex.findall(text)
    
    GCcontentDict = {}
    i = 0
    for sequence in GCdata:
        C_amt = 0
        G_amt = 0
        for NU in sequence:
            if NU == "C":
                C_amt +=1
            elif NU =="G":
                G_amt +=1
        GCcontent = ((C_amt + G_amt)/len(sequence))*100
        GCcontentDict[data[i]] = GCcontent
    maxGC = max(GCcontentDict, key=GCcontentDict.get)
    print(maxGC, "%.6f" % GCcontentDict[maxGC], "%")

getGCcontent()

