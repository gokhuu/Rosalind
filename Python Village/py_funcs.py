#python functions
 
'''
Enumermate(iterable, index = 0)
iterate through a list more effectively
'''

#ex: base list
lst = [1,2,3]

index = 0
for value in lst:
	print(index, value)
	index += 1
'''
output:
0 1
1 2
2 3
'''

#using enumerate:
for count, value in enumerate(lst):
	print(count,value)
'''
output:
0 1
1 2
2 3
-----
The same output is achieved with one less line of code.
The extra variable of index is not needed as an iterator
'''

'''
Map(function, iterable)
returns a map function after applying the function to each object in the iterable
'''
def double(n):
	return n + n 
lst = [1,2,3,4]

map_result = map(double, lst)
print(map_result)
'''
must cast to list or tuble before printing
<map object at 0x0000024C1B073BB0>
is the output
'''
print(list(map_result))
'''
[2, 4, 6, 8]
'''
#often used in conjuction with lambda functions
map_result = map(lambda x:x+x, lst)
print(list(map_result))
'''
[2, 4, 6, 8]
'''

'''
filter(function, iterable)
returns a filter object fo elements from an iterable that is True for the function
'''

def check_even(x):
	if x%2 == 0:
		return True

even_num = filter(check_even, lst)
print(even_num)
print(list(even_num))
'''
must cast to list or tuble before printing
<filter object at 0x00000171B76E2FD0>
[2, 4]
if the function returns true, filter will return the iterable
'''

'''
zip(iterable, iterable)

parallel iteration
'''

lst = [1,2,3]
lst_par = ['a','b','c']

print(list(zip(lst,lst_par)))
'''
[(1, 'a'), (2, 'b'), (3, 'c')]
'''