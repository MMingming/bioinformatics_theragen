Code = {'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
        'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
        'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*',
        'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W',
        'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
        'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
        'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
        'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
        'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
        'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
        'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
        'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
        'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
        'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
        'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
        'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
        }
Base = {"A":"T","T":"A","G":"C","C":"G"}


fr = open("sequence.nucleotide.fasta", "r")

lines = fr.xreadlines()
seq_f = ''
count = 0
for line in lines:
    if count == 1:
        seq_f += line.strip()
        continue
    count += 1
fr.close()

seq_r = ''
for i in seq_f:
   seq_r += Base[i]
#seq_foward
count = 0
x, xx, xxx = 0, 1, 2
y, yy, yyy = 3, 4, 5
f_1 = []
f_2 = []
f_3 = []
for i in seq_f:
    count += 1
    if count%3 == 0:
        f_1.append(Code[seq_f[x:y]])
        x += 3
        y += 3
    if count%3 == 1:
        if yy < len(seq_f):
            f_2.append(Code[seq_f[xx:yy]])
        xx += 3
        yy += 3
    if count%3 == 2:
        if yyy < len(seq_f):
            f_3.append(Code[seq_f[xxx:yyy]])
        xxx += 3
        yyy += 3

#seq_reverse
count = 0
x, xx, xxx = -3, -4, -5
y, yy, yyy = 0, -1, -2
r_1 = []
r_2 = []
r_3 = []
for i in seq_r:
    count += 1
    if y == 0:
        r_1.append(Code[seq_r[x:]])
        x -= 3
        y -= 3
    if y != 0 and count%3 == 0:
        if x >= -len(seq_r):
            r_1.append(Code[seq_r[x:y]])
        x -= 3
        y -= 3
    if count%3 == 1:
        if xx > -len(seq_r):
            r_2.append(Code[seq_r[xx:yy]])
        xx -= 3
        yy -= 3
    if count%3 == 2:
        if xxx > -len(seq_r):
            r_3.append(Code[seq_r[xxx:yyy]])
        xxx -= 3
        yyy -= 3


print '  '.join(f_1)+'\n'+' '+'  '.join(f_2)+'\n'+'  '+'  '.join(f_3)+'\n'+seq_f+'\n'+seq_r+'\n'+'  '.join(r_1)+'\n'+' '+'  '.join(r_2)+'\n'+'  '+'  '.join(r_3)
