#Rosalind Double Degree Array

#Given A simple graph with N<= 10^3 verticies in the edge list format
#Return An array D where D[i] is the sum of the degrees of i's neighbors

from typing import Counter
class Node:
    def __init__(self, data1 = None, data2 = None):
        self.start = data1
        self.end = data2
        self.next = None

class EdgeList:
    
    def __init__(self):
        self.head = None

    def print_list(self):
        printval = self.head
        while printval is not None:
            print(printval.start, printval.end)
            printval = printval.next

    def add_back(self,Node):
        if self.head is None:
            self.head = Node
            return 
        tail = self.head
        while(tail.next):
            tail = tail.next
        tail.next = Node
    
    def get_count(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count

#split given
def split_given(given):
    total_vert_edge = given[0]
    edge_list = given[1:]

    return total_vert_edge[0], total_vert_edge[1], edge_list



#fill linked list
def fill_lst(lst, linked_list):
    
    linked_list.head = Node(edge_list[0][0], edge_list[0][1])

    for i in range(1,len(lst)):
        newNode = Node(edge_list[i][0],edge_list[i][1])

        linked_list.add_back(newNode)

    return linked_list

def get_sum_vert(num_vert, linkedlist):
    lst = []
    for i in range(1,num_vert+1):
        count = 0
        current = linkedlist.head
        while current is not None:
            if current.start == i or current.end == i:
                count += 1
            current = current.next
        lst.append(count)
    return lst

def dic_of_edge_sum(lst):
    dict = {}
    for i in range(len(lst)):
        dict[i+1] = lst[i]
    return dict

def get_neighbors(num_vert,linkedlist):
    lst = []
    for i in range(1, num_vert+1):
        vert = []
        current = el.head
        while current is not None:
            if current.start == i:
                vert.append(current.end)
            if current.end == i:
                vert.append(current.start)
            current = current.next
        lst.append(vert)
    return lst

def get_neighbors_dict(lst):
    dict = {}

    for i in range(len(lst)):
        if lst[i]:
            dict[i+1] = lst[i]
        else:
            dict[i+1] = 0
    
    return dict

def get_sum_neighbors(num_vert,sum_dict,n_dict):
    sum_lst = []
    for i in range(1,num_vert+1):
        temp = n_dict[i]
        lst = []
        if temp == 0:
            sum_lst.append(0)
        else:
            for j in temp:
                lst.append(sum_dict[j])
            sum_lst.append(sum(lst))

    return sum_lst
##################################################################################
f = open('Rosalind\DDEG_Input.txt','r')
given = []
for line in f:
    temp = line.split()
    temp = list(map(int,temp))
    given.append(temp)

num_vert, num_edges, edge_list = split_given(given)
temp = EdgeList()
el = fill_lst(edge_list,temp)
#el.print_list()

#testing
target = 2
x = el.get_count()

lst = get_sum_vert(num_vert, el)

dict_sum_neighbors = dic_of_edge_sum(lst)
#print(dict_sum_neighbors)

neighbors_lst = get_neighbors(num_vert,el)

neighbors_dict = get_neighbors_dict(neighbors_lst)
#print(neighbors_dict)

to_string = get_sum_neighbors(num_vert,dict_sum_neighbors,neighbors_dict)
ans = list(map(str, to_string))
print(" ".join(ans))
