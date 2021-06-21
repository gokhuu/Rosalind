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


def sum2(n, lst):
    for i in range(n):
        for j in range(n):
            if int(lst[i]) == -int(lst[j]):
                return i, j
    return -1

def iterate_array(k, n, lst):

    return


filename = 'rosalind_2sum.txt'
file = import_file(filename)
k, n, new_file = adjust_file(file)
