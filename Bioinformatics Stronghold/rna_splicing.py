'''
given: dna string and collection of substrings
		in FASTA format

return: the protein string resulting from 
		trascribing/translating the exons
'''
trans_dict = {
    "UUU":'F',      'CUU':'L',      'AUU':'I',      'GUU':'V',
    "UUC":'F',      'CUC':'L',      'AUC':'I',      'GUC':'V',
    "UUA":'L',      'CUA':'L',      'AUA':'I',      'GUA':'V',
    "UUG":'L',      'CUG':'L',      'AUG':'M',      'GUG':'V',
    "UCU":'S',      'CCU':'P',      'ACU':'T',      'GCU':'A',
    "UCC":'S',      'CCC':'P',      'ACC':'T',      'GCC':'A',
    "UCA":'S',      'CCA':'P',      'ACA':'T',      'GCA':'A',
    "UCG":'S',      'CCG':'P',      'ACG':'T',      'GCG':'A',
    'UAU':'Y',      'CAU':'H',      'AAU':'N',      'GAU':'D',
    "UAC":'Y',      'CAC':'H',      'AAC':'N',      'GAC':'D',
    'UAA':'Stop',   'CAA':'Q',      'AAA':'K',      'GAA':'E',
    'UAG':'Stop',   'CAG':'Q',      'AAG':'K',      'GAG':'E',
    'UGU':'C',      'CGU':'R',      'AGU':'S',      'GGU':'G',
    'UGC':'C',      'CGC':'R',      'AGC':'S',      'GGC':'G',
    'UGA':'Stop',   'CGA':'R',      'AGA':'R',      'GGA':'G',
    'UGG':'W',      'CGG':'R',      'AGG':'R',      'GGG':'G' 
}

file = open("rna_splicing.txt",'r')
list_of_fasta = [line.split() for line in file]
seqs = [list_of_fasta[index] for index in range(1, len(list_of_fasta), 2)]
main_seq = seqs[0][0]
substrings = [str(i[0]) for i in seqs[1:]]

#remove introns from dna
for i in substrings:
	main_seq = main_seq.replace(i,'')

#convert to RNA
rna_seq = main_seq.replace('T', 'U')

#convert to protein seq
protein = ""
for i in range(0,len(rna_seq)-(3+len(rna_seq)%3),3):
    
    #if codon is s

#print answertop break loop
    if trans_dict[rna_seq[i:i+3]] == 'Stop':
        break
    
    #append protein string
    protein += trans_dict[rna_seq[i:i+3]]
print(protein)