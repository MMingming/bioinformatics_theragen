fr = open('sequence.protein.2.fasta', 'r')
lines = fr.readlines()

title = lines[0].rstrip()
print 'title: '+title

seq = ''
for line in lines[1:]:
    line = line.rstrip()
    seq += line
print 'seq: '+seq
fr.close()

