'''
input: given 2 dna strings in FASTA
output: the index of the beginning of the seq
'''

file = open("splice_motif.txt",'r')
list_of_fasta = [line.split() for line in file]
seqs = [list_of_fasta[index] for index in range(1, len(list_of_fasta), 2)]
DNA = seqs[0][0]
motifs = [str(i[0]) for i in seqs[1:]]

lst = []

for i in motifs:
	for j in range(len(DNA)-len(i)+1):
		if DNA[j:j+len(i)] == i:
			lst.append(j+1)


print(lst)