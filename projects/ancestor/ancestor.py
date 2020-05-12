from util import Queue

def earliest_ancestor(ancestors, starting_node):

    ancestorCache = {}
    for i in ancestors: # Child as key, parents as values in list
        if i[1] not in ancestorCache:
            ancestorCache[i[1]] = [i[0]]
        else:
            ancestorCache[i[1]].append(i[0])
    
    if starting_node not in ancestorCache:
        return -1

    distanceCache = {}
    distanceCache[starting_node] = 0
    
    searchQ = Queue()
    searchQ.enqueue(starting_node)

    while searchQ.size() > 0:
        # How do I uniquely identify and store paths within distances? 
        cr_node = searchQ.dequeue()

        if cr_node in ancestorCache:

            ancestors = ancestorCache[cr_node]
            for a in ancestors:
                distanceCache[a] = distanceCache[cr_node] + 1
                searchQ.enqueue(a)

    mostDistant = -1
    distance = 0

    for i, n in distanceCache.items():

        if mostDistant < 0:
            mostDistant = i
            distance = n

        else:
            if n > distance:
                mostDistant = i
                distance = n

    return mostDistant