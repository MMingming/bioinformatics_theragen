fr = open('sequence.protein.gb', 'r')
lines = fr.xreadlines()

count = 0
seq = ''
for line in lines:
    if count == 0:
        title = line.rstrip()
        count += 1
    elif line[0:6] == "ORIGIN":
        count += 1
    elif count >= 2:
        seq += line.lstrip()
import re
p = re.compile('[a-zA-Z]+')
lis = p.finditer(seq)
seq_1 = ''
for line in lis:
    seq_1 += line.group()
print 'title: %s\nseq: %s' % (title, seq_1)

fr.close()
