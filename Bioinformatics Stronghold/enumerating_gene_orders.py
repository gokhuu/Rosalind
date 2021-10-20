#given length of permuatations
#return the number of possible permuatations and their orders
import random
p = 3
lst = list(range(1,p+1))
all = []

while lst not in all:
    all.append(lst)
    lst = random.sample(lst,p)

print(all)
