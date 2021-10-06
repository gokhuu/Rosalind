#Given 10 DNA strings in Fasta Format
#Return the ID of the string with the highest GC content + the %

f = open('Rosalind_local_repo\Rosalind\Bioinformatics Stronghold\GC_input.txt','r')
def create_given_dict(f):
    lst = []
    for line in f:
        lst.append(line.split(' '))
    
    dict = {}
    for i in range(len(lst)):
        dict[lst[i][0]] = lst[i][1]
    
    return dict

fasta = create_given_dict(f)

'''
#get length of seq
temp = fasta['>Rosalind_6404']
seq_len = len(temp)

#get gc content
count = 0
for i in temp:
    if i == 'G':
        count += 1
    if i == 'C':
        count += 1

print(count)

#get percentage
print(count/seq_len*100)
'''

for i in fasta:
    temp = fasta[i]
    seq_len = len(temp)

    count = 0
    for j in temp:
        if j == 'G':
            count += 1
        if j == "C":
            count += 1
    print(i)
    print(count/seq_len*100)