a = 4480
b = 9144
total = 0

for i in range(a, b + 1):
    if i % 2 != 0:
        total += i

print(total)
