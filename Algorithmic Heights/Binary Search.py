def binary_search(lst, item):
    start_point = 0
    end_point = len(lst) - 1

    while start_point <= end_point:
        midpoint = start_point + (end_point - start_point) // 2
        midpoint_val = lst[midpoint]
        if item == midpoint_val:
            return midpoint + 1
        elif item < midpoint_val:
            end_point = midpoint - 1
        else:
            start_point = midpoint + 1

    return -1


file = open('rosalind_bin.txt', 'r')
n = file.readline()
m = file.readline()

A = file.readline().strip().split()
k = file.readline().strip().split()

print(*[binary_search(A, i) for i in k])
