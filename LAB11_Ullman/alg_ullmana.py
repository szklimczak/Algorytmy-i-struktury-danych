# Skończone
import numpy as np
from copy import deepcopy

class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
         return hash(self.key)

    def __str__(self):
        return str(self.key)

class GrafMacierz:
    def __init__(self, init_value=0):
        self.nodes = []
        self.matrix = []

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
    
    def a_matrix(self):
        return self.matrix

def create_M0(G, P):
    M0 = np.zeros((len(P), len(G)), dtype=int)
    for i in range(len(P)):
        for j in range(len(G)):
            if sum(P[i]) <= sum(G[j]):
                M0[i][j] = 1
    return M0

def ullmann1(used_columns, current_row, M, G, P, isomorphisms, calls):
    calls[0] += 1
    if current_row == len(M):
        MG = M @ G
        MGT = M @ np.transpose(MG)
        if (P == MGT).all():
            isomorphisms.append(deepcopy(M))
        return

    for c in range(len(M[0])):
        if not used_columns[c]:
            used_columns[c] = True
            M[current_row] = np.zeros(len(M[0]))
            M[current_row][c] = 1
            ullmann1(used_columns, current_row + 1, M, G, P, isomorphisms, calls)
            used_columns[c] = False

def ullmann2(used_columns, current_row, M, G, P, isomorphisms, calls):
    calls[0] += 1
    if current_row == len(M):
        MG = M @ G
        MGT = M @ np.transpose(MG)
        if (P == MGT).all():
            isomorphisms.append(deepcopy(M))
        return

    M_copy = deepcopy(M)
    for c in range(len(M_copy[0])):
        if not used_columns[c] and M[current_row][c] == 1:
            used_columns[c] = True
            M_copy[current_row] = np.zeros(len(M_copy[0]))
            M_copy[current_row][c] = 1
            ullmann2(used_columns, current_row + 1, M_copy, G, P, isomorphisms, calls)
            used_columns[c] = False

def prune(M, G, P):
    change = True
    while change:
        change = False
        for i in range(len(P)):
            for j in range(len(G)):
                if M[i][j] == 1:
                    P_neighbors = [idx for idx, val in enumerate(P[i]) if val]
                    G_neighbors = [idx for idx, val in enumerate(G[j]) if val]
                    if not any(M[p_n][g_n] == 1 for p_n in P_neighbors for g_n in G_neighbors):
                        M[i][j] = 0
                        change = True
    return M

def ullmann3(used_columns, current_row, M, G, P, isomorphisms, calls):
    calls[0] += 1
    if current_row == len(M):
        MG = M @ G
        MGT = MGT = M @ np.transpose(MG)
        if (P == MGT).all():
            isomorphisms.append(deepcopy(M))
        return

    M_copy = deepcopy(M)
    M_prune = prune(deepcopy(M_copy), G, P)
    for c in range(len(M_copy[0])):
        if not used_columns[c] and M[current_row][c] == 1:
            used_columns[c] = True
            M_prune[current_row] = np.zeros(len(M_prune[0]))
            M_prune[current_row][c] = 1
            ullmann3(used_columns, current_row + 1, M_prune, G, P, isomorphisms, calls)
            used_columns[c] = False

def main():
    graph_G = GrafMacierz()
    vertices_G = ['A', 'B', 'C', 'D', 'E', 'F']
    for v in vertices_G:
        graph_G.insert_vertex(Node(v))
    edges_G = [('A', 'B'), ('B', 'F'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
    for edge in edges_G:
        graph_G.insert_edge(Node(edge[0]), Node(edge[1]))

    graph_P = GrafMacierz()
    vertices_P = ['A', 'B', 'C']
    for v in vertices_P:
        graph_P.insert_vertex(Node(v))
    edges_P = [('A', 'B'), ('B', 'C'), ('A', 'C')]
    for edge in edges_P:
        graph_P.insert_edge(Node(edge[0]), Node(edge[1]))
    
    G_matrix = np.array(graph_G.a_matrix())
    P_matrix = np.array(graph_P.a_matrix())
    M = np.zeros((len(P_matrix), len(G_matrix[0])))
    
    # Ullmann1
    isomorphisms = []
    calls = [0]
    ullmann1([False] * len(G_matrix[0]), 0, M, G_matrix, P_matrix, isomorphisms, calls)
    print(len(isomorphisms), calls[0])

    # Ullmann2
    M0 = create_M0(G_matrix, P_matrix)
    isomorphisms = []
    calls = [0]
    ullmann2([False] * len(G_matrix[0]), 0, M0, G_matrix, P_matrix, isomorphisms, calls)
    print(len(isomorphisms), calls[0])

    # Ullmann3
    M0 = create_M0(G_matrix, P_matrix)
    M0_prune = prune(M0, G_matrix, P_matrix)
    isomorphisms = []
    calls = [0]
    ullmann3([False] * len(G_matrix[0]), 0, M0_prune, G_matrix, P_matrix, isomorphisms, calls)
    print(len(isomorphisms), calls[0])

if __name__ == '__main__':
    main()