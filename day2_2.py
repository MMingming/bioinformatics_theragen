string = raw_input('Enter a string: ')

#print 'The string length is %d' % (len(string))

import re
p = re.compile('\w')
lis = p.findall(string)

print len(lis)
