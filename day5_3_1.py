# codon dictionary, base dictionary
Code = {'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
        'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
        'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*',
        'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W',
        'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
        'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
        'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
        'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
        'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
        'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
        'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
        'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
        'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
        'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
        'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
        'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
        }
Base = {"A":"T","T":"A","G":"C","C":"G"}

# foward sequence & reverse sequence
seq_f = ''
count = 0
with open("sequence.nucleotide.fasta", "r") as fr:
    for line in fr:
        if count == 1:
            seq_f += line.strip()
            continue
        count += 1

seq_r = ''
for i in seq_f: seq_r += Base[i]
seq_r = seq_r[::-1]

# all reading frame 
def Translation(seq):
    translation = []
    for a in range(len(seq)):
        if a+3 > len(seq): break
        else:
            codon = seq[a:a+3]
            translation.append(Code[codon])
            continue
    cnt = 0
    li_1 = []
    li_2 = []
    li_3 = []
    for aa in translation:
        if cnt == 0: li_1.append(aa) ; cnt += 1
        elif cnt == 1: li_2.append(aa) ; cnt += 1
        elif cnt == 2: li_3.append(aa) ; cnt = 0
    return li_1, li_2, li_3

Fli_1, Fli_2, Fli_3 = Translation(seq_f)
Rli_1, Rli_2, Rli_3 = Translation(seq_r)
print(""+"  ".join(Fli_1))
print(" "+"  ".join(Fli_2))
print(" i "+"  ".join(Fli_3))
print(seq_f)
print(seq_r[::-1])
print("  "+"  ".join(Rli_1[::-1]))
print("    "+"  ".join(Rli_2[::-1]))
print("   "+"  ".join(Rli_3[::-1]))

