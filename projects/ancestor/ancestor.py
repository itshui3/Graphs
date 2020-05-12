from util import Queue
from graph import Graph

# def earliest_ancestor(ancestors, starting_node):

#     ancestorCache = {}
#     for i in ancestors: # Child as key, parents as values in list
#         if i[1] not in ancestorCache:
#             ancestorCache[i[1]] = [i[0]]
#         else:
#             ancestorCache[i[1]].append(i[0])
    
#     if starting_node not in ancestorCache:
#         return -1

#     distanceCache = {}
#     distanceCache[starting_node] = 0
    
#     searchQ = Queue()
#     searchQ.enqueue(starting_node)

#     while searchQ.size() > 0:
#         # How do I uniquely identify and store paths within distances? 
#         cr_node = searchQ.dequeue()

#         if cr_node in ancestorCache:

#             ancestors = ancestorCache[cr_node]
#             for a in ancestors:
#                 distanceCache[a] = distanceCache[cr_node] + 1
#                 searchQ.enqueue(a)

#     mostDistant = -1
#     distance = 0

#     for i, n in distanceCache.items():

#         if mostDistant < 0:
#             mostDistant = i
#             distance = n

#         else:
#             if n > distance:
#                 mostDistant = i
#                 distance = n
#     print(mostDistant, 'most distant')
#     return mostDistant

def earliest_ancestor(ancestors, starting_node):

    ancestorGraph = Graph()

    for anc in ancestors:
        parent = anc[0]
        child = anc[1]

        nodes = ancestorGraph.get_nodes()
        if parent not in nodes:
            ancestorGraph.add_vertex(parent)
        if child not in nodes:
            ancestorGraph.add_vertex(child)
    
    for anc in ancestors:
        ancestorGraph.add_edge(anc[1], anc[0])

    if len(ancestorGraph.get_neighbors(starting_node)) < 1:
        return -1

    Q = Queue()
    Q.enqueue(starting_node)
    visited = set()

    bastard = None

    while Q.size() > 0:

        adoptee = Q.dequeue()
        visited.add(adoptee)

        parents = ancestorGraph.get_neighbors(adoptee)

        if len(parents) < 1:
            bastard = adoptee

        for p in parents:
            if p not in visited:
                Q.enqueue(p)
    
    return bastard

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1), (3, 10)]
print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 3))
print(earliest_ancestor(test_ancestors, 4))
print(earliest_ancestor(test_ancestors, 5))
earliest_ancestor(test_ancestors, 6)
earliest_ancestor(test_ancestors, 7)
earliest_ancestor(test_ancestors, 8)
earliest_ancestor(test_ancestors, 9)
earliest_ancestor(test_ancestors, 10)
earliest_ancestor(test_ancestors, 11)