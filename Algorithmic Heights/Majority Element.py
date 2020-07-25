import os

def major(lst, n):
    count = 0
    for i in (lst):
        if i == n:
            count += 1

    return count


def majorityElementy(lst):
    count_dict = {}

    num = len(lst) / 2

    for i in lst:
        count_dict[i] = major(lst, i)

    max_num = 0
    mode = 0

    for key, value in count_dict.items():
        if value > max_num:
            max_num = value
            mode = key

    if max_num > num:
        return int(mode)
    else:
        return -1

'''
w = ["5", "5", "5", "5", "5", "5", "5", "5"]
x = ["8", "7", "7", "1", "7", "3", "7"]
y = ["7", "1", '6', '5', '10', '100', '1000', '1']
z = ["5", "1", "6", '7', '1', '1', '10', '1']

a = [w, x, y, z]
ans = []

for b in a:
    ans.append(majorityElementy(b))

print(*ans)
'''

with open(os.path.join('rosalind_mj.txt')) as dataset:
    n1 =(dataset.readline().strip().split(" "))
    n,m = int(n1[0]),int(n1[1])

    A = []
    ans = []
    for a in dataset:
        A.append(majorityElementy(a.strip().split(' ')))

    print(*A)