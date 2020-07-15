# Open File and save lines as variable data
file = open('rosalind_degree.txt', 'r')
data = file.readlines()

# split first line into 2 variables for num verticies and num edges
v, e = data[0].split()
v = int(v)  # num verticies
e = int(e)  # num edges

# initialize list of counted vertexs
count = [0] * (v + 1)

# iterate through the data and count the number of times a vertex appears
for i in range(1, e + 1):
    v1, v2 = data[i].split()
    count[int(v1)] += 1
    count[int(v2)] += 1

# remove the first element of the list count
count = count[1:]

# formatting
ans = ' '.join(str(item)for item in count)
print(ans)
