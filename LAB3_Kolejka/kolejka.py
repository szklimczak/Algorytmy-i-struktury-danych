# Skończone

def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]

class Kolejka:
    def __init__(self, size = 5):
        self.tab = [None for i in range(size)]
        self.size = size
        self.zapis = 0
        self.odczyt = 0
    
    def is_empty(self):
        return self.odczyt == self.zapis

    def peek(self):
        return self.tab[self.odczyt]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.peek()
            self.tab[self.odczyt] = None
            self.odczyt += 1
            if self.odczyt == self.size:
                self.odczyt = 0     
            return data

    def enqueue(self, data):
        self.tab[self.zapis] = data
        self.zapis += 1
        if self.zapis == self.size:
            self.zapis = 0
        if self.zapis == self.odczyt:
            new_size = self.size * 2
            self.tab = realloc(self.tab, new_size)
            last = new_size
            for i in range(self.odczyt, self.size):
                self.tab[last - 1] = self.tab[self.size - i]
                self.tab[self.size - i] = None
                last -= 1
            self.odczyt = last
            self.size *= 2

    def __str__(self):
        string = "["
        element = self.odczyt
        while self.tab[element] is not None:
            string += str(self.tab[element]) + " "
            if element == self.size - 1:
                element = 0
            else:
                element += 1
        string = string.rstrip()
        return string + "]"

    def tab_str(self):
        string = "["
        for i in range(self.size):
            string += str(self.tab[i])
            if i != self.size - 1:
                string += " "
        return string + "]"


def main():
    kolejka = Kolejka()
    for i in range(1,5):
        kolejka.enqueue(i)
    print(kolejka.dequeue())
    print(kolejka.peek())
    print(kolejka)
    for i in range(5,9):
        kolejka.enqueue(i)
    print(kolejka.tab_str())
    while not kolejka.is_empty():
        print(kolejka.dequeue())
    print(kolejka)

if __name__ == '__main__':
    main()