# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter
import re
import xlsxwriter
from math import sqrt
size=32
row = 3
er=1
col = 2
V=[0] * size
PREP=[0]* size
PART=[0]* size
DET=[0]* size
NOUN=[0]* size
NSUFF=[0]* size
ADJ=[0]* size
PRON=[0]* size
NUM=[0]* size
CONJ=[0]* size
words=[0]* size
avgV=[0]* size
mydict = {}
alldict = {}
workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/NegWords_1000.xlsx')
worksheet = workbook.add_worksheet()
k = 0
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(20)

for i in range(1,size):
    lineN=0
    print "/Users/diasaleh/Desktop/GP/wordFreq/negative words/1000/"+str(i)+".txt"
    with open("/Users/diasaleh/Desktop/GP/wordFreq/negative words/1000/"+str(i)+".txt", "r") as f:
        for line in f:
            lineN = lineN + 1
            if lineN == 1:
                wordsCount = line
            else:
                x = line.split(":")
                mydict[x[0].strip(),i] = [x[1],x[2]]
print mydict
print mydict["غير" ,1]
lineN = 0

with open("/Users/diasaleh/Desktop/GP/wordFreq/negative words/1000/1000.txt", "r") as f:
    for line in f:
        lineN = lineN + 1
        if lineN == 1:
            wordsCount = line
        else:
            x = line.split(":")
            alldict[x[0].strip(),1] = [x[1],x[2]]
print alldict
print alldict["غير" ,1]
for j in range(1,size):
    PART[j] =int(mydict["إلا",j][0])
    PREP[j] =float(mydict["إلا",j][1])

worksheet.write(row-1, col , "1000H L",format)

for j in range(1,size):
    worksheet.write(row, col, PART[j] )
    worksheet.write(row, col+1,PREP[j] ,format)
    row += 1
worksheet.write(row+1, col, int(alldict["إلا",er][0]))
worksheet.write(row+1, col+1, float(alldict["إلا",er][1]),format)
row = 3
col = col + 3
PREP=[0]* size
PART=[0]* size
for j in range(1, size):
    PART[j] =int(mydict["حاشا",j][0])+int(mydict["خلا",j][0])+int(mydict["عدا",j][0])
    PREP[j] =float(mydict["حاشا",j][1])+float(mydict["خلا",j][1])+float(mydict["عدا",j][1])

worksheet.write(row-1, col, "1000H V",format)

for j in range(1,size):
    worksheet.write(row, col, PART[j])
    worksheet.write(row, col + 1, PREP[j] , format)
    row += 1
worksheet.write(row+1, col, int(alldict["حاشا",er][0])+int(alldict["خلا",er][0])+int(alldict["عدا",er][0]))
worksheet.write(row+1, col+1, float(alldict["حاشا",er][1])+float(alldict["خلا",er][1])+float(alldict["عدا",er][1]),format)
row = 3
col = col + 3

for j in range(1, size):
    PART[j] =int(mydict["سوى",j][0])+int(mydict["سواء",j][0])+int(mydict["غير",j][0])
    print PART[j]
    PREP[j] =float(mydict["سوى",j][1])+float(mydict["سواء",j][1])+float(mydict["غير",j][1])

worksheet.write(row-1, col, "1000H N",format)

for j in range(1, size):
    worksheet.write(row, col, PART[j])
    worksheet.write(row, col + 1, PREP[j], format)
    row += 1
worksheet.write(row+1, col, int(alldict["سوى",er][0])+int(alldict["سواء",er][0])+int(alldict["غير",er][0]))
worksheet.write(row+1, col+1, float(alldict["سوى",er][1])+float(alldict["سواء",er][1])+float(alldict["غير",er][1]),format)
row = 3
col = col + 3
print col

workbook.close()
