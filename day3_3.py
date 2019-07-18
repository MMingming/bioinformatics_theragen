fr = open('sequence.protein.fasta', 'r')
lines = fr.readlines()
for line in lines:
    print line
fr.close()
