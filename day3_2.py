fr = open('title.txt', 'r')
lines = fr.xreadlines()
for i in lines:
    i = i.rstrip()
    print 'The first line is: ' + i


