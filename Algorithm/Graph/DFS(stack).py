from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.stack = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # undirected graph
        self.graph[v].append(u)

    def DFS(self, start):

        visited = [False] * len(self.graph)

        self.stack.append(start)

        while self.stack:
            node = self.stack.pop()

            if not visited[node]:

                print(node, end=" ")

            visited[node] = True
            for adjacent_node in self.graph[node]:
                if not visited[adjacent_node]:
                    self.stack.append(adjacent_node)

# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex )")
g.DFS(3)