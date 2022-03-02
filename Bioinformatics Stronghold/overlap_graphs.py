file = open("overlap_graphs.txt",'r')
list_of_fasta = [line.split() for line in file]

fasta = {list_of_fasta[i][0]:list_of_fasta[i+1][0] for i in range(0,len(list_of_fasta),2)}
seqs = []
for i in fasta:
	seqs.append(fasta[i])
print(seqs)