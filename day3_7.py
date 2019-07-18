fr = open('sequence.protein.2.fasta', 'r')
lines = fr.readlines()

seq = ''
for line in lines[1:]:
    line = line.rstrip()
    seq += line
fr.close()
print seq
# code = open('codonTable', 'r')
# code_dic = code.read()

while True:
    num = raw_input('Position: ')
    if num == 'XXX':
        break
    else:
        try:
            num = int(num)
        except:
            print 'plz enter a number'
            continue
    print seq[num-1:num+2]

