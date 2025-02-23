# Nieskończone
import polska

class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
         return hash(self.key)

    def __str__(self):
        return str(self.key)

class GrafLista:
    def __init__(self):
        self.nodes = {}

    def is_empty(self):
        return len(self.nodes) == 0

    def insert_vertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        if vertex1 in self.nodes and vertex2 in self.nodes:
            self.nodes[vertex1][vertex2] = edge
            self.nodes[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.nodes:
            del self.nodes[vertex]
            for v in self.nodes:
                if vertex in self.nodes[v]:
                    del self.nodes[v][vertex]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.nodes and vertex2 in self.nodes:
            if vertex2 in self.nodes[vertex1]:
                del self.nodes[vertex1][vertex2]
            if vertex1 in self.nodes[vertex2]:
                del self.nodes[vertex2][vertex1]

    def get_vertex(self, vertex_id):
        return vertex_id
    
    def neighbours(self, vertex_id):
        return self.nodes[vertex_id].items()

    def vertices(self):
        return self.nodes.keys()
    
class GrafMacierz:
    def __init__(self, init_value = 0):
        self.nodes = []
        self.matrix = [[init_value for _ in range(len(self.nodes))] for _ in range(len(self.nodes))]

    def is_empty(self):
        return len(self.nodes) == 0

    def insert_vertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes.append(vertex)
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * len(self.nodes))

    def insert_edge(self, vertex1, vertex2, edge=1):
        if vertex1 in self.nodes and vertex2 in self.nodes:
            index1 = self.nodes.index(vertex1)
            index2 = self.nodes.index(vertex2)
            self.matrix[index1][index2] = edge
            self.matrix[index2][index1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.nodes:
            index = self.nodes.index(vertex)
            del self.nodes[index]
            del self.matrix[index]
            for row in self.matrix:
                del row[index]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.nodes and vertex2 in self.nodes:
            index1 = self.nodes.index(vertex1)
            index2 = self.nodes.index(vertex2)
            self.matrix[index1][index2] = 0
            self.matrix[index2][index1] = 0

    def get_vertex(self, vertex_id):
        return self.nodes[vertex_id]

    def neighbours(self, vertex_id):
        neighbors = []
        for idx, row in enumerate(self.matrix[vertex_id]):
            if row != 0:
                neighbors.append((idx, row))
        return neighbors
    
    def vertices(self):
        return range(len(self.nodes))


def main():
    graf_lista = GrafLista()
    graf_macierz = GrafMacierz()
    for edge in polska.graf:
        vertex1 = Node(edge[0])
        vertex2 = Node(edge[1])
        graf_lista.insert_vertex(vertex1)
        graf_lista.insert_vertex(vertex2)
        graf_lista.insert_edge(vertex1, vertex2)
        graf_macierz.insert_vertex(vertex1)
        graf_macierz.insert_vertex(vertex2)
        graf_macierz.insert_edge(vertex1, vertex2)
    graf_lista.delete_vertex(Node("K"))
    graf_lista.delete_edge(Node("W"), Node("E"))
    graf_macierz.delete_vertex(Node("K"))
    graf_macierz.delete_edge(Node("W"), Node("E"))
    #polska.draw_map(graf_lista)
    polska.draw_map(graf_macierz)

if __name__ == '__main__':
    main()