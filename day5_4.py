fr = open("sequence.nucleotide.gb", "r")

import re
p = re.compile("CDS  ")
p1 = re.compile("STS")

lines = fr.xreadlines()
count = 0
cds = ''
for line in lines:
    if p.findall(line):count +=1
    elif count == 1 and p1.findall(line):
        break
    elif count == 1:
        cds += line.strip()

num = ((cds.index("translation"))+len("translation  "))

print cds[num:len(cds)-1]







