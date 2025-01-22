 

class Graph:
    def __init__(self, n, edges, directed=False):
 
        self.edges = [set() for _ in range(n)]
        for u, v in edges:
            self.edges[u].add(v)
            if not directed:
                self.edges[v].add(u)


    def is_edge(self, u, v):
        """
        :return: Returns whether node (u, v) is present
        """
        return v in self.edges[u]


    def neighbors(self, u):
        """
        :return: A set of u's neighbors
        """
        return self.edges[u].copy()


    def size(self):
        """
        :return: The number of vertices
        """
        return len(self.edges)


from collections import deque

"""
BFS on graph using a queue. Returns dictionaries of parents and
distance from source for each node in BFS tree
"""
def bfs(graph: Graph, source: int):
    parent = {source: source}
    dist = {source: 0}
    queue = deque([source])

    while len(queue) != 0:
        u = queue.popleft()
        for v in graph.neighbors(u):
            if v not in dist:
                parent[v] = u
                dist[v] = dist[u] + 1
                queue.append(v)

    return parent, dist


"""
Recursive DFS: returns dictionaries of start time, end time,
and parents for each node in DFS forest
"""
def dfs_re(graph: Graph, source: int):
    start, end, parent, time = {}, {}, {}, [1]

    def dfs_visit(u):
        start[u] = time[0]
        time[0] += 1
        for v in graph.neighbors(u):
            if v not in start:
                parent[v] = u
                dfs_visit(v)
        end[u] = time[0]
        time[0] += 1

    dfs_visit(source)

    for u in range(graph.size()):
        if u not in start:
            parent[u] = u
            dfs_visit(u)

    return parent, start, end


"""
Iterative DFS: uses stack, returns dictionary of node -> parent
"""
def dfs_it(graph: Graph, source: int):
    stack = deque([source])
    parent = {source: source}

    while len(stack) != 0:
        u = stack.pop()
        for v in graph.neighbors(u):
            if v not in parent:
                parent[v] = u
                stack.append(v)

    return parent


edges = [()]
g = Graph(6, [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (4, 5)])

# p, d = bfs(g, 0)
# print(d)

p = dfs_it(g, 0)
print(p)