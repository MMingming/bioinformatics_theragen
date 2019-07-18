while True:
    num = raw_input('which times table: ')

    try:
        num = int(num)
    except:
        print 'plz enter a number'
        continue
    
    if 0< num <10:
        for i in range(1, 10):
            print '%d * %d = %2d' % (num, i, num*i)
        break
    else:
        print 'What?'
