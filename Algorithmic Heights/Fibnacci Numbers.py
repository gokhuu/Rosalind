# naive function
def fibnum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibnum(n - 1) + fibnum(n - 2)


# rosalind solution
def fib(n):
    a, b = 0, 1

    for i in range(0, n):
        a, b = b, a + b

    return a


print(fib(200))
