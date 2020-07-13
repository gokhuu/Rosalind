def binary_search(lst, item):
    start_point = 0
    end_point = len(lst) - 1

    while start_point <= end_point:
        midpoint = (end_point - start_point) // 2
        midpoint_val = lst[midpoint]
        if item == midpoint_val:
            return midpoint
        elif item < midpoint_val:
            end_point = midpoint - 1
        else:
            start_point = midpoint + 1

    return -1


file = open('rosalind_bins.txt', 'r')
n = file.readline()
m = file.readline()

A_n = file.readline()
A_m = file.readline()

ans = []

for i in A_m:
    ans.append(binary_search(A_n, i))

print(*ans)
