# Skończone
import time
import random
from copy import deepcopy

class Element:
    def __init__(self, priorytet, dane):
        self.dane = dane
        self.priorytet = priorytet
    
    def __lt__(self, other):
        return self.priorytet < other.priorytet

    def __gt__(self, other):
        return self.priorytet > other.priorytet

    def __repr__(self):
        return str(self.priorytet) + ":" + str(self.dane)
    
class Kopiec:
    def __init__(self, tab = None):
        if tab is None:
            self.tab = []
            self.size = 0
        else:
            self.tab = tab
            self.size = len(tab)
            for i in range(self.size - 1, -1, -1):
                self.naprawa(i)

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2

    def parent(self, idx):
        return (idx - 1)//2

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]
    
    def naprawa(self, idx):
        left_idx = self.left(idx)
        right_idx = self.right(idx)
        largest = idx

        if left_idx < self.size and self.tab[left_idx] > self.tab[largest]:
            largest = left_idx
        if right_idx < self.size and self.tab[right_idx] > self.tab[largest]:
            largest = right_idx
        if largest != idx:
            self.tab[idx], self.tab[largest] = self.tab[largest], self.tab[idx]
            self.naprawa(largest)

    def heap_sort(self):
        size = self.size
        while self.size > 1:
            el = self.peek()
            self.tab[0] = self.tab[self.size-1]
            self.tab[self.size - 1] = el
            self.size -= 1
            self.naprawa(0)
        self.size = size
        
    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end = ' ')
        print( '}')

    
def insertion_sort(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab

def shell_sort(tab):
    h = 1
    while h < len(tab)/3:
        h = h*3+1
    while h >= 1:
        for i in range(h, len(tab)):
            temp = tab[i]
            j = i
            while j >= h and tab[j - h] > temp:
                tab[j] = tab[j - h]
                j -= h
            tab[j] = temp
        h //= 3
    return tab

def main():
    tab = [Element(key, value) for key,value in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    tab_kopia1 = deepcopy(tab)
    print(tab_kopia1)
    print(insertion_sort(tab_kopia1))
    print("Algorytm insertion_sort jest stabilny")
    lista1 = []
    for i in range(10000):
        lista1.append(int(random.random() * 100))
    t_start_insertion = time.perf_counter()
    insertion_sort(lista1)
    t_stop_insertion = time.perf_counter()
    print("Czas obliczeń insertion_sort:",
          "{:.7f}".format(t_stop_insertion - t_start_insertion))
    
    tab_kopia2 = deepcopy(tab)
    print(tab_kopia2)
    print(shell_sort(tab_kopia2))
    print("Algorytm shell_sort nie jest stabilny")
    lista2 = []
    for i in range(10000):
        lista2.append(int(random.random() * 100))
    t_start_shell = time.perf_counter()
    shell_sort(lista2)
    t_stop_shell = time.perf_counter()
    print("Czas obliczeń shell_sort:",
          "{:.7f}".format(t_stop_shell - t_start_shell))

    lista = []
    for i in range(10000):
        lista.append(int(random.random() * 100))
    t_start = time.perf_counter()
    tab2 = Kopiec(lista)
    tab2.heap_sort()
    t_stop = time.perf_counter()
    print("Czas obliczeń heap_sort:", "{:.7f}".format(t_stop - t_start))
    

if __name__ == '__main__':
    main()