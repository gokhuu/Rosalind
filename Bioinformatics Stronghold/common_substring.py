'''
given: a collection of strings at most 1kb with FASTA format
return : the longest common substring of the collection
'''

from read_fasta import fastaread

fasta = fastaread('common_substring_input.txt')

seqs = []
for i in fasta:
	seqs.append(fasta[i])


from difflib import SequenceMatcher

string2 = seqs[0]
for i in range(1,len(seqs)):
	string1 = string2
	string2 = seqs[i]
	match = SequenceMatcher(None, string1, string2).find_longest_match(0,len(string1),0,len(string2))
print(string1[match.a: match.a + match.size])