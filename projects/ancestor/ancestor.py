
def earliest_ancestor(ancestors, starting_node):
    print('starting_node', starting_node)
    print('ancestors', ancestors)
    ancestorCache = {}
    for i in ancestors:
        if i[1] not in ancestorCache:
            ancestorCache[i[1]] = [i[0]]
        else:
            ancestorCache[i[1]].append(i[0])
    
    if starting_node not in ancestorCache:
        return -1
    
    searcher = starting_node

    while searcher in ancestorCache:
        searcher = ancestorCache[searcher][0]
    return searcher
    parents = ancestorCache[starting_node]
    print(ancestorCache[parents[0]])