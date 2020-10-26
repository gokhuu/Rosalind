import os


def sum2(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if int(lst[i]) == -int(lst[j]):
                return i, j
    return -1


with open(os.path.join('rosalind_2sum.txt')) as data:
    n, m = data.readline().strip().split()
    a = data.readlines()
    for line in a:
        for i in line:
            int(i)
