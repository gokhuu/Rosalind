'''
given: k <= 20
n <= 10^4
k num of arrays size n
    with ints -10^5 to 10^5

output:
for each array
output two different indicies 1<=p<=q<=n 
such that A[p] = -A[q] otherwise print -1
'''
def import_file(filename):
    file = open(filename, 'r')

    lst = []

    for line in file:
        lst.append(line.strip())

    return lst

def adjust_file(file):
    k, n = file[0].split()
    k, n = int(k), int(n)

    lst = []
    file = file[1:]

    for line in file:
        lst.append(line.split())

    return k, n, lst

def sum2(n,lst):
    for p in range(len(lst)):
        for q in range(p,len(lst)):
            if q <= n:
                if int(lst[p]) == -int(lst[q]):
                    return p+1,q+1
    return -1

filename = 'rosalind_2sum.txt'
file = import_file(filename)
k, n, new_file = adjust_file(file)

for i in new_file:
    print(sum2(n,i))
    