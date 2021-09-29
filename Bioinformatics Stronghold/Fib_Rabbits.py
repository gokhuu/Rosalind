#given pos int n <= 40
#      pos int k <= 5

#return the total num of rabbit pairs after n months,
#if we begin with 1 pair every generation, 
#every pair produces k rabbits

n = 33
k = 5

def find_total(n,k):
    f1 = 1
    f2 = 1

    if n <= 1:
        return 1
    elif n <= 2:
        return 1
    else:
        return k*find_total(n-2,k) + find_total(n-1,k)

print(find_total(n,k))