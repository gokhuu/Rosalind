#given: a simple directed graph
#return: distance from v1 to v[i]

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

##################################################################################
f = open('Rosalind_local_repo\Rosalind\Algorithmic Heights\eadth_first_input.txt','r')
given = []
for line in f:
    temp = line.split()
    temp = list(map(int,temp))
    given.append(temp)

num_vert, num_edges, edge_list = split_given(given)
temp = EdgeList()
el = fill_lst(edge_list,temp)
el.print_list()