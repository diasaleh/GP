# -*- coding: UTF-8 -*-
from __future__ import division

def wordAvgLength( str ):
    #
    # sentence=""

    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print average
    return average


sentence=""
avg=0
for x in range(1, 11):
    f = open("/Users/diasaleh/Desktop/100/t" + str(x) + ".txt", "r")
    sentence = f.read()
    sentence = unicode(sentence, "utf-8")
    avg+=wordAvgLength(sentence)
print "avg"
print avg/10