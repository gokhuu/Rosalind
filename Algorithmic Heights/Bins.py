def binary_search(A, item, start=None, stop=None):
    start = 0 if start is None else start
    stop = len(A) - 1 if stop is None else stop

    if stop < start:
        return -1

    else:
        mid = (start + stop) // 2
        if A[mid] > item:
            return binary_search(A, item, start, mid - 1)
        elif A[mid] < item:
            return binary_search(A, item, mid, stop)
        else:
            return mid


'''
file = open('rosalind_bins.txt', 'r')
n = file.readline()
m = file.readline()

A = file.readline().strip().split()
k = file.readline().strip().split()
'''

A = [10, 20, 30, 40, 50]
k = [40, 10, 35, 15, 40, 20]
ind = []
for i in k:
    ind.append(binary_search(A, i))

print(*ind)
