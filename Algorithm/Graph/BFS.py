from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # undirected graph
        self.graph[v].append(u)

    def BFS(self, start):

        queue = []
        visited = [False] * len(self.graph)

        queue.append(start)
        visited[start] = True

        while queue:
            unvisited_node = queue.pop(0)
            print(unvisited_node, end=" ")

            for adjacent_node in self.graph[unvisited_node]:
                if not visited[adjacent_node]:
                    queue.append(adjacent_node)
                    visited[adjacent_node] = True


# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal")
g.BFS(3)
