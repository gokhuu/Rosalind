#given n <= 100 and m <= 20
#return total number of rabbits that will remain after
#        after the n-th month if all rabbits live for m months

n = 80
m = 19
bunnies = [1,1]
months = 2
count = []

while months < n:
    if months < m:
        bunnies.append(bunnies[-2] + bunnies[-1])
    elif months == m or count == m+1:
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)
    else:
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(m+1)])
    
    months +=1 

print(bunnies[-1])