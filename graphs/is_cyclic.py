from collections import defaultdict

# We generate graph with defaultdict


class Graph:

    def __init__(self, V):
        self.graph = defaultdict(list)
        self.v = V

    def add_edge(self, v, e):
        self.graph[v].append(e)

    def is_cyclic(self):

        visited = [False for i in range(self.v)]
        recStack = [False for i in range(self.v)]
        visited_nodes = []

        for node in range(self.v):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, recStack, visited_nodes):
                    return True
        return visited_nodes

    def is_cyclic_util(self, node, visited, recStack, visited_nodes):

        visited[node] = True
        recStack[node] = True

        neighbours = self.graph[node]

        for neighbour in neighbours:
            if not visited[neighbour]:
                self.is_cyclic_util(neighbour, visited,
                                    recStack, visited_nodes)
            elif recStack[neighbour]:
                return True

        # Unset the recStack elements
        recStack[node] = False
        visited_nodes.append(node)


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
ans = g.is_cyclic()
breakpoint()
