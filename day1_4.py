a = raw_input('Enter a integer: ')
b = raw_input('Enter another: ')

a = int(a)
b = int(b)

if a > b:
    print '%d is greater than %d' % (a, b)
elif a < b:
    print '%d is less than %d' % (a, b)
else:
    print '%d is equal to %d' % (a, b)
