from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # undirected graph
        self.graph[v].append(u)

    def DFS_core(self, visited, node):
        print(node, end=" ")
        visited[node] = True

        for adjacent_node in self.graph[node]:
            if not visited[adjacent_node]:
                self.DFS_core(visited, adjacent_node)


    def DFS(self, start):
        visited = [None] * len(self.graph)

        self.DFS_core(visited, start)

# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS&BFS from (starting from vertex 2)")
g.DFS(2)