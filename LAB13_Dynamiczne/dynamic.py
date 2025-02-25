# Skończone
import numpy as np

def string_compare(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    change = string_compare(P, T, i-1, j-1) + (P[i] != T[j])
    insert = string_compare(P, T, i, j-1) + 1
    delete = string_compare(P, T, i-1, j) + 1
    min_cost = min(change, insert, delete)
    return min_cost

def string_compare_PD(P, T):
    D = [[0] * len(T) for _ in range(len(P))]
    parent = [['X'] * len(T) for _ in range(len(P))]
    for i in range(1, len(P)):
        D[i][0] = i
        parent[i][0] = 'D'
    for j in range(1, len(T)):
        D[0][j] = j
        parent[0][j] = 'I'
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            change = D[i-1][j-1] + (P[i] != T[j])
            insert = D[i][j-1] + 1
            delete = D[i-1][j] + 1
            min_cost = min(change, insert, delete)
            D[i][j] = min_cost
            if min_cost == change:
                if P[i] != T[j]:
                    parent[i][j] = 'S'
                else:
                    parent[i][j] = 'M'
            elif min_cost == insert:
                parent[i][j] = 'I'
            else:
                parent[i][j] = 'D'
    
    return D[len(P)-1][len(T)-1], parent

def path_reconstruction(P, T, parent):
    path = []
    i = len(P) - 1
    j = len(T) - 1
    znak = parent[i][j]
    while znak != 'X':
        if znak == 'S' or znak == 'M':
            i -= 1
            j -= 1
        elif znak == 'I':
            j -= 1
        elif znak == 'D':
            i -= 1
        path.append(znak)
        znak = parent[i][j]
    path.reverse()
    return ''.join(path)

def find_substring(P, T):
    D = [[0] * len(T) for _ in range(len(P))]
    parent = [['X'] * len(T) for _ in range(len(P))]
    for i in range(1, len(P)):
        D[i][0] = i
        parent[i][0] = 'D'
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            change = D[i-1][j-1] + (P[i] != T[j])
            insert = D[i][j-1] + 1
            delete = D[i-1][j] + 1
            min_cost = min(change, insert, delete)
            D[i][j] = min_cost
            if change <= insert and change <= delete:
                if P[i] == T[j]:
                    parent[i][j] = 'M'
                else:
                    parent[i][j] = 'S'
            elif insert < change and insert < delete:
                parent[i][j] = 'I'
            else:
                parent[i][j] = 'D'
    end = D[-1].index(min(D[-1]))
    start = end - len(P) + 2
    return start, end 

def common_sequence(P, T):
    D = [[0] * len(T) for _ in range(len(P))]
    parent = [['X'] * len(T) for _ in range(len(P))]
    for i in range(1, len(P)):
        D[i][0] = i
        parent[i][0] = 'D'
    for j in range(1, len(T)):
        D[0][j] = j
        parent[0][j] = 'I'
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            x = 0
            if T[j] != P[i]:
                x = np.inf
            change = D[i-1][j-1] + x
            insert = D[i][j-1] + 1
            delete = D[i-1][j] + 1
            min_cost = min(change, insert, delete)
            D[i][j] = min_cost
            if min_cost == change:
                if P[i] != T[j]:
                    parent[i][j] = 'S'
                else:
                    parent[i][j] = 'M'
            elif min_cost == insert:
                parent[i][j] = 'I'
            else:
                parent[i][j] = 'D'
    
    path = []
    i = len(parent) - 1
    j = len(parent[0]) - 1
    znak = parent[i][j]
    while znak != 'X':
        if znak == 'S' or znak == 'M':
            i -= 1
            j -= 1
            if znak == "M":
                path.append(P[i + 1])
        elif znak == 'I':
            j -= 1
        elif znak == 'D':
            i -= 1
        znak = parent[i][j]
    path.reverse()
    return ''.join(path)    

def monotonic_sequence(T):
    P = ''.join(sorted(set(T)))
    return common_sequence(P, T)


def main():
    #a)
    P = ' kot'
    T = ' pies'
    print(string_compare(P, T, len(P) - 1, len(T) - 1))
    #b)
    P = ' biały autobus'
    T = ' czarny autokar'
    print(string_compare_PD(P, T)[0])
    #c)
    P = ' thou shalt not'
    T = ' you should not'
    parent = string_compare_PD(P, T)[1]
    print(path_reconstruction(P, T, parent))
    #d)
    P = ' ban'
    T = ' mokeyssbanana'
    start, end = find_substring(P, T)
    print(start)
    #e)
    P = ' democrat'
    T = ' republican'
    print(common_sequence(P, T))
    #f)
    T = ' 243517698'
    print(monotonic_sequence(T))


if __name__ == '__main__':
    main()