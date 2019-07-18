fr = open('sequence.protein.fasta', 'r')
lines = fr.readlines()

seq = ''
for line in lines:
    seq += line.rstrip()
fr.close()

import re

while True:
    aa = raw_input('Searching for: ')
    if aa == 'XXX':
        break
    else:
        p = re.compile(aa, re.I)
        Iter = p.finditer(seq)
        buff = []
        i_start = [i.start() for i in Iter]
        buff = map(str, i_start)
        print ", ".join(buff)
