# -*- coding: UTF-8 -*-
from __future__ import division
import re
import xlsxwriter
from math import sqrt


def standard_deviation(lst, population=False):
    """Calculates the standard deviation for a list of numbers."""
    num_items = len(lst)
    mean = sum(lst) / num_items
    print mean
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)

    # Note: it would be better to return a value and then print it outside
    # the function, but this is just a quick way to print out the values along
    # the way.
    if population is True:
        print('This is POPULATION standard deviation.')
        variance = ssd / num_items
    else:
        print('This is SAMPLE standard deviation.')
        variance = ssd / (num_items - 1)
    sd = sqrt(variance)
    return sd
    # You could `return sd` here.
size=32
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
aV=0
aPREP=0
aPART=0
aDET=0
aNOUN=0
aNSUFF=0
aADJ=0
aPRON=0
aNUM=0
aCONJ=0
awords=0
sentence=""
row = 3
col = 2

allwords=0
j=0
workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/POSssZ.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(4, 1 , "Verbs")
worksheet.write(5, 1 , "PREP")
worksheet.write(6, 1 , "PART")
worksheet.write(7, 1  ,  "DET")
worksheet.write(8, 1 , "NOUN")
worksheet.write(9, 1 , "NSUFF")
worksheet.write(10, 1 ,"PRON")
worksheet.write(11, 1 ,"NUM")
worksheet.write(12, 1 ,"CONJ")
worksheet.write(13, 1 , "ADJ")
worksheet.write(14, 1 , "words")
pos =[]

o = open("/Users/diasaleh/Desktop/GP/POS1000s.txt","w")
for i in range(0,32):
    f = open("/Users/diasaleh/Desktop/GP/1000/TN"+str(i)+".txt", "r")
    print "/Users/diasaleh/Desktop/GP/100/TN"+str(i)+".txt"
    sentence += f.read()
    sentence = unicode(sentence, "utf-8")
    x = sentence.split()

    words[i] += len(x)
    with open("/Users/diasaleh/Desktop/GP/pos1000/newPOSresult_1_1000_"+str(i)+".txt", "r") as f:
        for line in f:
            x = line.split("&")
            if len(x) > 2:
                if x[1] == "V":
                    V[i]+=  1
                if x[1] == "PREP":
                    PREP[i] = PREP[i] + 1
                if x[1] == "PART":
                    PART[i] = PART[i] + 1
                if x[1] == "DET":
                    DET[i] = DET[i] + 1
                if x[1] == "NOUN":
                    NOUN[i] = NOUN[i] + 1
                if x[1] == "NSUFF":
                    NSUFF[i] = NSUFF[i] + 1
                if x[1] == "PRON":
                    PRON[i] = PRON[i] + 1
                if x[1] == "NUM":
                    NUM[i] = NUM[i] + 1
                if x[1] == "CONJ":
                    CONJ[i] = CONJ[i] + 1
                if x[1] == "ADJ":
                    ADJ[i] = ADJ[i] + 1
    o.write("100H Book"+str(i)+"\n")
    o.write(str(V[i])+"\n")
    o.write(str(PREP[i])+"\n")
    o.write(str(PART[i])+"\n")
    o.write(str(DET[i])+"\n")
    o.write(str(NOUN[i])+"\n")
    o.write(str(NSUFF[i])+"\n")
    o.write(str(PRON[i])+"\n")
    o.write(str(NUM[i])+"\n")
    o.write(str(CONJ[i])+"\n")
    o.write(str(ADJ[i])+"\n")
    o.write(str(words[i])+"\n")
    o.write("=========================================\n")
    pos.append(i)
    pos.append(V[i])
    pos.append(PREP[i])
    pos.append(PART[i])
    pos.append(DET[i])
    pos.append(NOUN[i])
    pos.append(NSUFF[i])
    pos.append(PRON[i])
    pos.append(NUM[i])
    pos.append(CONJ[i])
    pos.append(ADJ[i])
    pos.append(words[i])


    # Iterate over the data and write it out row by row.

    k=0
    format = workbook.add_format()
    format.set_bold()
    format.set_font_color('white')
    format.set_bg_color('green')
    format.set_font_size(20)

    for item in (pos):
        worksheet.write(row, col, item)
        if(k>0):
            worksheet.write(row, col+1, (100*item)/words[i],format)
        k+=1
        row += 1
    pos=[]
    col = col + 2
    print col

    aV += V[i]
    aPREP += PREP[i]
    aPART +=PART[i]
    aDET +=DET[i]
    aNOUN += NOUN[i]
    aNSUFF += NSUFF[i]
    aADJ +=ADJ[i]
    aPRON += PRON[i]
    aNUM += NUM[i]
    aCONJ += CONJ[i]

    avgV[i] = (V[i]*100)/words[i]

    allwords = words[i]+allwords
    sentence=""
    row=3
o.write("allwords = "+ str(allwords)+"\n")
o.close()

worksheet.write(18, 4 , (100*aV) / allwords)
worksheet.write(19, 4 , (100*aPREP )/ allwords)
worksheet.write(20, 4 , (100*aPART )/ allwords)
worksheet.write(21, 4 , (100*aDET )/ allwords)
worksheet.write(22, 4 , (100*aNOUN )/ allwords)
worksheet.write(23, 4 , (100*aNSUFF )/ allwords)
worksheet.write(24, 4 , (100*aPRON )/ allwords)
worksheet.write(25, 4 ,(100* aNUM )/ allwords)
worksheet.write(26, 4 , (100*aCONJ) / allwords)
worksheet.write(27, 4 , (100*aADJ) / allwords)
worksheet.write(28, 4 ,  allwords)

o = 18
for x in avgV:
    worksheet.write(o, 7, x)
    o+=1
V.remove(0)
avgV.remove(0)
print V
print avgV
print len(avgV)
print standard_deviation(avgV)
workbook.close()
