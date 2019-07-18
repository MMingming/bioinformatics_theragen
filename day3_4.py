fr = open('sequence.protein.fasta', 'r')
fw = open('sequence.protein.2.fasta', 'w')

lines = fr.readlines()
for line in lines:
    fw.write(line)
fr.close()
fw.close()
