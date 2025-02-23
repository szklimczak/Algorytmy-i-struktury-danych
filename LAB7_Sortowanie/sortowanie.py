# Skończone
import random
import time
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

    def print_tree(self, idx, lvl):
        if idx < self.size:           
            self.print_tree(self.right(idx), lvl + 1)   
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)        
            self.print_tree(self.left(idx), lvl + 1)


def swap(tab):
    for i in range(len(tab)):
        min_idx = i
        for j in range(i, len(tab)):
            if tab[j] < tab[min_idx]:
                min_idx = j
        tab[i], tab[min_idx] = tab[min_idx], tab[i]
    return tab

def shift(tab):
    for i in range(len(tab)):
        min_idx = i
        for j in range(i, len(tab)):
            if tab[j] < tab[min_idx]:
                min_idx = j
        min_val = tab.pop(min_idx)
        tab.insert(i, min_val)
    return tab


def main():
    tab = [Element(key, value) for key,value in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    tab_kopia = deepcopy(tab)
    tablica = Kopiec(tab_kopia)
    tablica.print_tab()
    tablica.print_tree(0,0)
    tablica.heap_sort()
    tablica.print_tab()
    #sortowanie nie jest stabilne
    lista = []
    for i in range(10000):
        lista.append(int(random.random() * 100))
    t_start = time.perf_counter()
    tab2 = Kopiec(lista)
    tab2.heap_sort()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    tab_kopia2 = deepcopy(tab)
    print(tab_kopia2)
    print(swap(tab_kopia2))
    #algorytm swap nie jest stabilny
    lista2 = []
    for i in range(10000):
        lista2.append(int(random.random() * 100))
    t_start_swap = time.perf_counter()
    swap(lista2)
    t_stop_swap = time.perf_counter()
    print("Czas obliczeń swap:",
          "{:.7f}".format(t_stop_swap - t_start_swap))
    
    tab_kopia3 = deepcopy(tab)
    print(tab_kopia3)
    print(shift(tab_kopia3))
    #algorytm shift jest stabilny
    lista3 = []
    for i in range(10000):
        lista3.append(int(random.random() * 100))
    t_start_shift = time.perf_counter()
    shift(lista3)
    t_stop_shift = time.perf_counter()
    print("Czas obliczeń shift:",
          "{:.7f}".format(t_stop_shift - t_start_shift))

if __name__ == '__main__':
    main()