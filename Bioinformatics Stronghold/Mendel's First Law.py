from scipy.special import comb


def mendel(k, m, n):
    total = 4 * comb(k + m + n, 2)

    total_rec = 4 * comb(n, 2) + 2 * n * m + comb(m, 2)

    return 1 - total_rec / total


k = 26
m = 20
n = 23

print(str(mendel(k, m, n)))
