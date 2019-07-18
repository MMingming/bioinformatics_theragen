def fq(in_file):
    fr = open(in_file, 'r')
    lines = fr.readlines()
    title = lines[0].rstrip()
    seq = ''
    for line in lines[1:]:
        line = line.rstrip()
        seq += line
    fr.close()
    return title, seq
    ###############################################
def gb(in_file):
    fr = open(in_file, 'r')
    lines = fr.xreadlines()

    count = 0
    seq = ''
    for line in lines:
        if count == 0:
            title = line.rstrip()
            count += 1
        elif line[0:6] == "ORIGIN":
            count += 1
        elif count >= 2:
            seq += line.lstrip()
    import re
    p = re.compile('[a-zA-Z]+')
    lis = p.finditer(seq)
    seq = ''
    for line in lis:
        seq += line.group()
    count = 0
    seq_1 = ''
    for i in seq:
        count += 1
        if count == 70:
            seq_1 += i+"\n"
            count = 0
        else:
            seq_1 += i
    fr.close()
    return title, seq_1
    ###############################################

in_file = raw_input('Enter input file: ')
out_file = raw_input('Enter output file: ')
option_1 = 'Read a FASTA format DNA sequence file and make a reverse sequence.'
option_2 = 'Read a FASTA format DNA sequence file and make a reverse complement sequence.'
option_3 = 'Convert GenBank format file to FASTA format file.'
print 'Option-1) '+option_1+'\n'+'Option-2) '+option_2+'\n'+'Option-3) '+option_3
option = raw_input('Select the option: ')

fw = open(out_file, 'w')

if option == 'Option-1':
    a,b = fq(in_file)
    print a+'\n'+b[::-1]
elif option == 'Option-2':
    a,b = fq(in_file)
    code = {"A":"T","T":"A","G":"C","C":"G"}
    seq = ''
    for i in b:
        i = code[i]
        seq += i
    print a+'\n'+seq
elif option == 'Option-3':
    a,b = gb(in_file)
    print a+'\n'+b

fw.close()
