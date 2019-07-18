#-*- coding: utf-8 -*-


fr = open('sequence.nucleotide.gb' , 'r')


import re
p = re.compile("TITLE+")     #단어자체를 비교하고 싶으면 따움표로 묶거나 변수 사용
                             #title = "TITLE"
p1 = re.compile("JOURNAL+")

lines = fr.xreadlines()
count = 0
lis = []
for line in lines:
    if p.findall(line):
        lis.append(line)
        count += 1
    elif p1.findall(line):
        count = 0
    elif count == 1:
        lis.append(line)
fr.close()

count = 0
title = ""
for i in lis:
    if count==1 and p.findall(i):
        i = i.replace("TITLE", "     ")
        title +='\n' +i.rstrip()
    elif p.findall(i):
        title += i.rstrip()
        count += 1
    else:
        title += " "+i.strip()




print title
