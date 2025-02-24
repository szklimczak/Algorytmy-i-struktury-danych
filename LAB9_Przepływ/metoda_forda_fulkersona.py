# Skończone

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
         return hash(self.key)

    def __str__(self):
        return str(self.key)
    
class Edge:
    def __init__(self, capacity, isResidual=False):
        self.capacity = capacity
        self.flow = 0
        self.residual = capacity if not isResidual else 0
        self.isResidual = isResidual

    def __repr__(self):
        return str(self.capacity) + " " + str(self.flow) + " " + str(self.residual) + " " + str(self.isResidual)
    
class GrafLista:
    def __init__(self):
        self.nodes = {}

    def is_empty(self):
        return len(self.nodes) == 0

    def insert_vertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = {}

    def insert_edge(self, vertex1, vertex2, capacity):
        if vertex1 in self.nodes and vertex2 in self.nodes:
            self.nodes[vertex1][vertex2] = Edge(capacity)
            self.nodes[vertex2][vertex1] = Edge(0, isResidual=True)

    def bfs(self, s):
        visited = set()
        parent = {}
        queue = []

        visited.add(s)
        queue.append(s)

        while queue:
            current = queue.pop(0)
            for neighbor, edge in self.nodes[current].items():
                if neighbor not in visited and edge.residual > 0:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        return parent

    def find_path_capacity(self, s, t, parent):
        if t not in parent:
            return 0

        current = t
        min_flow = float('Inf')

        while current != s:
            e = parent[current]
            min_flow = min(min_flow, self.nodes[e][current].residual)
            current = e

        return min_flow

    def augment_path(self, s, t, parent, min_flow):
        v = t
        while v != s:
            u = parent[v]
            if self.nodes[u][v].residual > 0:
                self.nodes[u][v].flow += min_flow
                self.nodes[u][v].residual -= min_flow
                self.nodes[v][u].residual += min_flow
            else:
                self.nodes[u][v].residual -= min_flow
                self.nodes[v][u].flow -= min_flow
                self.nodes[v][u].residual += min_flow
            v = u

    def ford_fulkerson(self, s, t):
        max_flow = 0
        parent = self.bfs(s)
        path_flow = self.find_path_capacity(s, t, parent)
        while path_flow > 0:
            max_flow += path_flow
            self.augment_path(s, t, parent, path_flow)
            parent = self.bfs(s)
            path_flow = self.find_path_capacity(s, t, parent)
        return max_flow

    def vertices(self):
        return self.nodes.keys()

    def neighbours(self, vertex_id):
        return self.nodes[vertex_id].items()


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def test_max_flow(graph, s, t):
    graf = GrafLista()
    for edge in graph:
        graf.insert_vertex(edge[0])
        graf.insert_vertex(edge[1])
        graf.insert_edge(edge[0], edge[1], edge[2])

    max_flow = graf.ford_fulkerson(s, t)
    print("Max Flow:", max_flow)
    printGraph(graf)

def main():
    graf_0 = [('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf_1 = [('s','a',16), ('s','c',13), ('c','a',4), ('a','b',12), ('b','c',9), ('b','t',20), ('c','d',14), ('d','b',7), ('d','t',4)]
    graf_2 = [ ('s','a',3), ('s','c',3), ('a','b',4), ('b','s',3), ('b','c',1), ('b','d',2), ('c','e',6), ('c','d',2), ('d','t',1), ('e','t',9)]
    test_max_flow(graf_0, 's', 't')
    test_max_flow(graf_1, 's', 't')
    test_max_flow(graf_2, 's', 't')


if __name__ == '__main__':
    main()