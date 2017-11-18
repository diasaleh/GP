# -*- coding: UTF-8 -*-
from __future__ import division
import xlsxwriter
import collections

row = 3
col = 1
size=31
words=[0]* (size+1)
PREP=[0]* (size+1)
allPREP=[0]* (size+1)
inn=[0]* (size+1)
ala=[0]* (size+1)
mn=[0]* (size+1)
ela=[0]* (size+1)
an=[0]* (size+1)
b=[0]* (size+1)
l=[0]* (size+1)
ff=[0]* (size+1)
until=[0]* (size+1)
k=[0]* (size+1)
mth=[0]* (size+1)
mnth=[0]* (size+1)
workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/1000PrepFrqByWords.xlsx')
worksheet = workbook.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)

for i in range(1,size+1):
    sentence = ""

    f = open("/Users/diasaleh/Desktop/GP/1000/TN" + str(i) + ".txt", "r")
    print "/Users/diasaleh/Desktop/GP/1000/TN" + str(i) + ".txt"
    sentence += f.read()
    sentence = unicode(sentence, "utf-8")
    x = sentence.split()
    words[i] += len(x)

    with open("/Users/diasaleh/Desktop/GP/pos1000/newPOSresult_1_1000_" + str(i) + ".txt", "r") as f:
        for line in f:
            x = line.split("&")
            if len(x) > 2:
                if x[1] == "PREP":
                    allPREP[i] = allPREP[i] + 1
                    if x[0] == "ب+":
                        b[i] = b[i] + 1
                        PREP[i] = PREP[i] + 1
                    elif x[0] == "ل+":
                        l[i] = l[i] + 1
                        PREP[i] = PREP[i] + 1
                    elif x[0]=="في":
                        inn[i]=inn[i]+1
                        PREP[i] = PREP[i] + 1
                    elif x[0]=="من":
                        mn[i]=mn[i]+1
                        PREP[i] = PREP[i] + 1
                    elif x[0]=="على" or x[0]=="علي":
                        ala[i]=ala[i]+1
                        PREP[i] = PREP[i] + 1
                    elif x[0] == "الى"or x[0]=="إلى" or x[0]=="إلي" or x[0]=="الي":
                        ela[i]=ela[i]+1
                        PREP[i] = PREP[i] + 1
                    elif x[0]=="عن":
                        an[i]=an[i]+1
                        PREP[i] = PREP[i] + 1
                    elif x[0] == "حتى":
                        until[i] = until[i] + 1
                        PREP[i] = PREP[i] + 1
                    elif x[0] == "ك+":
                        k[i] = k[i] + 1
                        PREP[i] = PREP[i] + 1
                    elif x[0] == "مذ":
                        mth[i] = mth[i] + 1
                        PREP[i] = PREP[i] + 1
                    elif x[0] == "منذ":
                        mnth[i] = mnth[i] + 1
                        PREP[i] = PREP[i] + 1
                    else:
                        print x[0]

    print allPREP[i]
    print PREP[i]
    print inn[i]
    PREP = [x / 100 for x in PREP]
    words = [x / 100 for x in words]
    inn[0] += inn[i]/words[i]
    b[0] += b[i]/words[i]
    l[0] += l[i]/words[i]
    k[0] += k[i]/words[i]
    mnth[0] += mnth[i]/words[i]
    mth[0] += mth[i]/words[i]
    until[0] += until[i]/words[i]
    an[0] += an[i]/words[i]
    ela[0] += ela[i]/words[i]
    ala[0] += ala[i]/words[i]
    mn[0] += mn[i]/words[i]

    worksheet.write(row, col, unicode("في", "utf-8"),format)
    col+=3
    worksheet.write(row, col, unicode("من", "utf-8"), format)
    col+=3
    worksheet.write(row, col, unicode("على", "utf-8"), format)
    col+=3
    worksheet.write(row, col, unicode("الى", "utf-8"), format)
    col+=3
    worksheet.write(row, col, unicode("عن", "utf-8"), format)
    col+=3
    worksheet.write(row, col, unicode("ب", "utf-8"), format)
    col+=3
    worksheet.write(row, col, unicode("ل", "utf-8"), format)
    col+=3
    worksheet.write(row, col, unicode("ك", "utf-8"), format)
    col+=3
    worksheet.write(row, col, unicode("حتى", "utf-8"), format)
    col+=3
    worksheet.write(row, col, unicode("منذ", "utf-8"), format)
    col+=3
    worksheet.write(row, col, unicode("مذ", "utf-8"), format)



    col=1
    worksheet.write(row+i, col, inn[i],format)
    worksheet.write(row+i, col+1, inn[i]/words[i],format)
    col+=3
    worksheet.write(row+i, col, mn[i], format)
    worksheet.write(row+i, col+1, mn[i] / words[i], format)
    col+=3
    worksheet.write(row+i, col, ala[i], format)
    worksheet.write(row+i, col+1, ala[i] / words[i], format)
    col+=3
    worksheet.write(row+i, col, ela[i], format)
    worksheet.write(row+i, col+1, ela[i] / words[i], format)
    col+=3
    worksheet.write(row+i, col, an[i], format)
    worksheet.write(row+i, col+1, an[i] / words[i], format)
    col+=3
    worksheet.write(row+i, col, b[i], format)
    worksheet.write(row+i, col+1, b[i] / words[i], format)
    col+=3
    worksheet.write(row+i, col, l[i], format)
    worksheet.write(row+i, col+1, l[i] / words[i], format)
    col+=3
    worksheet.write(row+i, col, k[i], format)
    worksheet.write(row+i, col+1, k[i] / words[i], format)
    col+=3
    worksheet.write(row+i, col, until[i], format)
    worksheet.write(row+i, col+1, until[i] / words[i], format)
    col+=3
    worksheet.write(row+i, col, mnth[i], format)
    worksheet.write(row+i, col+1, mnth[i] / words[i], format)
    col+=3
    worksheet.write(row+i, col, mth[i], format)
    worksheet.write(row+i, col+1, mth[i] / words[i], format)
    col =1

col=3
for i in range(1,size+1):
    worksheet.write(row+i, col, (inn[0]/size), format)
    col+=3
    worksheet.write(row + i, col, (mn[0] / size) , format)
    col += 3
    worksheet.write(row + i, col, (ala[0] / size) , format)
    col += 3
    worksheet.write(row + i, col, (ela[0] / size) , format)
    col += 3
    worksheet.write(row + i, col, (an[0] / size) , format)
    col += 3
    worksheet.write(row + i, col, (b[0] / size) , format)
    col += 3
    worksheet.write(row + i, col, (l[0] / size) , format)
    col += 3
    worksheet.write(row + i, col, (k[0] / size) , format)
    col += 3
    worksheet.write(row + i, col, (until[0] / size) , format)
    col += 3
    worksheet.write(row + i, col, (mnth[0] / size) , format)
    col += 3
    worksheet.write(row + i, col, (mth[0] / size) , format)
    col += 3

    col=3



workbook.close()
