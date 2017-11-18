# -*- coding: UTF-8 -*-
from __future__ import division
import re
import xlsxwriter
row = 3
col = 1

workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/Patin100notin1000.xlsx')
worksheet = workbook.add_worksheet()
i=0
worksheet.write(2, col, i)
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)
format2 = workbook.add_format()
format2.set_bold()
format2.set_font_color('white')
format2.set_bg_color('blue')
format2.set_font_size(16)
with open("/Users/diasaleh/Desktop/GP/Patin100notin1000.txt","r") as f:
    for line in f:
        x = line.strip().split(":")
        if x[0] == "@@@":
            print "new file"
            i+=1
            worksheet.write(2, col , i)
            col+=2
            row = 3
        else:
            print x[0]
            if len(x)==3:
                if x[0].strip() != '#':
                    sentence = unicode(x[0], "utf-8")
                    worksheet.write(row, col,sentence )
                    worksheet.write(row, col+1, float(x[1]),format)
                    worksheet.write(row, col+2, float(x[2]),format2)
                    row += 1
workbook.close()
