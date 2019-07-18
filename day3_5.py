fr =open('sequence.protein.2.fasta', 'r')
line = fr.readlines()
print 'The second line is: '+line[1]
fr.close()
