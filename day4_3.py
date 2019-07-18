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
seq = ''
for line in lis:
    seq += line.group()

count = 0
seq_1 = ''
for i in seq:
    count += 1
    if count == 70:
        seq_1 += i+"\n"
        count = 0
    else:
        seq_1 += i
print seq_1

fr.close()
