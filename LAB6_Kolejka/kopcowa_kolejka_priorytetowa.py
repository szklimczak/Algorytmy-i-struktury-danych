# Skończone

class Element:
    def __init__(self, dane, priorytet):
        self.dane = dane
        self.priorytet = priorytet
    
    def __lt__(self, other):
        return self.priorytet < other.priorytet

    def __gt__(self, other):
        return self.priorytet > other.priorytet

    def __repr__(self):
        return str(self.priorytet) + ":" + str(self.dane)

class Kolejka:
    def __init__(self):
        self.queue = []
        self.size = 0

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
        return self.queue[0]

    def dequeue(self):
        if self.is_empty():
            return None
        korzen = self.queue[0]
        self.queue[0] = self.queue[self.size - 1]
        self.size -= 1
        self.naprawa(0)
        return korzen

    def enqueue(self, element):
        if self.size == len(self.queue):
            self.queue.append(element)
        else:
            self.queue[self.size] = element
        idx = self.size
        self.size += 1
        while idx > 0 and self.queue[self.parent(idx)] < self.queue[idx]:
            self.queue[self.parent(idx)], self.queue[idx] = self.queue[idx], self.queue[self.parent(idx)]
            idx = self.parent(idx)
    
    def naprawa(self, idx):
        left_idx = self.left(idx)
        right_idx = self.right(idx)
        largest = idx

        if left_idx < self.size and self.queue[left_idx] > self.queue[largest]:
            largest = left_idx
        if right_idx < self.size and self.queue[right_idx] > self.queue[largest]:
            largest = right_idx
        if largest != idx:
            self.queue[idx], self.queue[largest] = self.queue[largest], self.queue[idx]
            self.naprawa(largest)
        
    def print_tab(self):
        print ('{', end=' ')
        print(*self.queue[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx < self.size:           
            self.print_tree(self.right(idx), lvl + 1)   
            print(2*lvl*'  ', self.queue[idx] if self.queue[idx] else None)        
            self.print_tree(self.left(idx), lvl + 1)


def main():
    kolejka = Kolejka()
    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    napis = "GRYMOTYLA"
    for i in range(len(priorytety)):
        kolejka.enqueue(Element(napis[i], priorytety[i]))
    kolejka.print_tree(0, 0)
    kolejka.print_tab()
    dana = kolejka.dequeue()
    print(kolejka.peek())
    kolejka.print_tab()
    print(dana)
    while not kolejka.is_empty():
        print(kolejka.dequeue())
    kolejka.print_tab()


if __name__ == '__main__':
    main()