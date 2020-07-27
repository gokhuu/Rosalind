import os


def majorityElementy(lst):
    count_dict = {}

    num = len(lst) / 2

    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

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


with open(os.path.join('rosalind_mj.txt')) as dataset:
    n1 = (dataset.readline().strip().split(" "))
    n, m = int(n1[0]), int(n1[1])

    A = []
    ans = []
    for a in dataset:
        A.append(majorityElementy(a.strip().split(' ')))

    print(*A)
