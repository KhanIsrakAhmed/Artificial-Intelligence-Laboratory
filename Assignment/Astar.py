'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    17-02-2024     *************************  '''


class Node:
    def __init__(self, name, p, g, h):
        self.name = name
        self.p = p
        self.g = g
        self.h = h
        self.f = g + h
        
'''
p = parent................................................................
g = actual value..........................................................
h = heuristic value.......................................................

'''

adjacency_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('D', 2), ('G', 3)],
    'D': [('G', 2), ('A', 2)],
    'G': [('C', 4)],
}


H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 1,
    'G': 0,
}

pqueue = []
nobj = Node('S', None, 0, H['S']) 
pqueue.append(nobj)
g_node = None

while pqueue:
    pqueue.sort(key=lambda x: x.f) #Sort the pqueue base on f copied from google
    nobj = pqueue.pop(0)

    if nobj.name == 'G':
        g_node = nobj
        break
    
    

    for nbr_name, edge_cost in adjacency_list[nobj.name]:
        nbr_node = Node(nbr_name, nobj, nobj.g + edge_cost, H[nbr_name])
        pqueue.append(nbr_node)



if g_node:
    path = []
    cost = g_node.g
    
    while g_node is not None:
        path.append(g_node.name)
        g_node = g_node.p
        
        
    path.reverse()
    print("Path:", path)
    print("Total Cost:", cost)
    
      
else:
    print("Can not reach out the goal")
