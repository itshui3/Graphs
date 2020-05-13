"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):

        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        self.vertices[v1].add(v2)
    
    def get_nodes(self):
        return self.vertices

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # If I begin by enqueue'ing starting_vertex and write a while loop that doesn't end until all queued elements have become resolved, I can procedurally modify visited vertexes(printed vertexes) to be unvisitable
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        searchQ = Queue()
        QCache = {} # Used to delineate between values that can  still be added to queue and those that have already been added

        searchQ.enqueue(starting_vertex)
        QCache[starting_vertex] = 1

        while searchQ.size() > 0:

            # I need to add neighbors to Q
            # Print the current vertex as well as dequeue it
            removedVert = searchQ.dequeue()
            print(removedVert)

            neighbors = self.get_neighbors(removedVert)
            if len(neighbors) > 0:
                for vert in neighbors:
                    if vert not in QCache:
                        searchQ.enqueue(vert)
                        QCache[vert] = 1

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        S = Stack()
        SQache = {}

        S.push(starting_vertex)
        SQache[starting_vertex] = 1

        while S.size() > 0:
            removedVert = S.pop()
            print(removedVert)

            neighbors = self.get_neighbors(removedVert)
            if len(neighbors) > 0:
                for vert in neighbors:
                    if vert not in SQache:
                        S.push(vert)
                        SQache[vert] = 1

    def dft_recursive(self, starting_vertex, cache={}):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        cache[starting_vertex] = 1

        neighbors = self.get_neighbors(starting_vertex)

        if len(neighbors) > 0:
            for vert in neighbors:
                if vert not in cache:
                    self.dft_recursive(vert, cache)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        dirCache = {}

        dirCache[starting_vertex] = []
        dirCache[starting_vertex].append(starting_vertex)

        q = Queue()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            cur_vert = q.dequeue()

            neighbors = self.get_neighbors(cur_vert)

            for n in neighbors:
                if n not in dirCache:
                    dirCache[n] = dirCache[cur_vert] + [n] # might not concat like so
                    if destination_vertex in dirCache:
                        return dirCache[destination_vertex]
                    q.enqueue(n)
                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        dirCache = {}
        dirCache[starting_vertex] = []
        dirCache[starting_vertex].append(starting_vertex)

        s = Stack()
        s.push(starting_vertex)

        while s.size() > 0:
            cur_vert = s.pop()
            neighbors = self.get_neighbors(cur_vert)

            for n in neighbors:
                if n not in dirCache:
                    s.push(n)
                    dirCache[n] = dirCache[cur_vert] + [n]
                    if destination_vertex in dirCache:
                        return dirCache[destination_vertex]

    def dfs_recursive(self, starting_vertex, destination_vertex, dirCache={}):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex not in dirCache:
            dirCache[starting_vertex] = [starting_vertex]

        neighbors = self.get_neighbors(starting_vertex)
        if len(neighbors) > 0:
            for n in neighbors:
                if n not in dirCache:
                    dirCache[n] = dirCache[starting_vertex] + [n]

                    if n == destination_vertex:
                        return dirCache[n]
                    else:
                        chain = self.dfs_recursive(n, destination_vertex, dirCache)
                        if chain is not None:
                            return chain

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
