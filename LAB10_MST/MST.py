# Skończone
import graf_mst

class Node:
    def __init__(self, key, color=None):
        self.key = key
        self.color = color

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
         return hash(self.key)

    def __str__(self):
        return str(self.key)
    
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class GrafLista:
    def __init__(self):
        self.nodes = {}

    def is_empty(self):
        return len(self.nodes) == 0

    def insert_vertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = {}

    def insert_edge(self, vertex1, vertex2, weight=None):
        if vertex1 in self.nodes and vertex2 in self.nodes:
            self.nodes[vertex1][vertex2] = weight
            self.nodes[vertex2][vertex1] = weight

    def get_vertex(self, vertex_id):
        return vertex_id
    
    def neighbours(self, vertex_id):
        return self.nodes[vertex_id].items()

    def vertices(self):
        return self.nodes.keys()
    
    def mst_prim(self, start_vertex):
        intree = {v: 0 for v in self.nodes}
        distance = {v: float('inf') for v in self.nodes}
        parent = {v: None for v in self.nodes}
        mst = GrafLista()
        sum = 0

        current_vertex = start_vertex
        intree[current_vertex] = 1
        distance[current_vertex] = 0

        while not all(intree.values()):
            for neighbor, weight in self.neighbours(current_vertex):
                if not intree[neighbor] and weight < distance[neighbor]:
                    distance[neighbor] = weight
                    parent[neighbor] = current_vertex

            min_distance = float('inf')
            next_vertex = None
            for v in self.nodes:
                if not intree[v] and distance[v] < min_distance:
                    min_distance = distance[v]
                    next_vertex = v

            if next_vertex is None:
                break

            current_vertex = next_vertex
            if parent[current_vertex] is not None:
                mst.insert_vertex(current_vertex)
                mst.insert_vertex(parent[current_vertex])
                mst.insert_edge(current_vertex, parent[current_vertex], min_distance)
                sum += min_distance

            intree[current_vertex] = 1

        return mst, sum

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
   

def main():
    graph = GrafLista()
    for edge in graf_mst.graf:
        graph.insert_vertex(edge[0])
        graph.insert_vertex(edge[1])
        graph.insert_edge(edge[0], edge[1], edge[2])

    mst, sum = graph.mst_prim('B')
    printGraph(mst)

if __name__ == '__main__':
    main()