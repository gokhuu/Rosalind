'''
given: dna string and collection of substrings
		in FASTA format

return: the protein string resulting from 
		trascribing/translating the exons
'''
file = open("rna_splicing.txt",'r')
list_of_fasta = [line.split() for line in file]
seqs = [list_of_fasta[index] for index in range(1, len(list_of_fasta), 2)]
main_seq = seqs[0][0]
substrings = seqs[1:]


for i in substrings:
	main_seq.replace(i[0], '')

main_seq = main_seq.replace('T', 'U')

print(main_seq)



'''
def match_substring(dna, introns):
	for i in range((len(dna)-len(introns)+1)):
		if dna[i:i+len(introns)] == introns:
			return(1)

print(len(substrings))

count = 0
for i in substrings:
	count += (match_substring(main_seq, i[0]))

print(count)
'''