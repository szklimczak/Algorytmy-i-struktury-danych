# Skończone

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        napis = ""
        napis += str(self.key) + ":" + str(self.value)
        return napis


class Tablica_Mieszajaca:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def mix(self, key):
        if isinstance(key, str):
            key = sum(ord(c) for c in key)
        return key % len(self.tab)
    
    def kolizja(self, idx, i):
        new_index = (idx + self.c1 * i + self.c2 * i * i) % self.size
        return new_index

    def search(self, key):
        idx = self.mix(key)
        for i in range(self.size):
            new_index = self.kolizja(idx, i)
            if isinstance(self.tab[new_index], Element) and self.tab[new_index].key == key:
                return self.tab[new_index].value
        return None

    def insert(self, elem: Element):
        idx = self.mix(elem.key)
        for i in range(self.size):
            new_index = self.kolizja(idx, i)
            if self.tab[new_index] is None or self.tab[new_index].key == elem.key:
                self.tab[new_index] = elem
                return
        print("Brak miejsca")

    def remove(self, key):
        idx = self.mix(key)
        for i in range(self.size):
            new_index = self.kolizja(idx, i)
            if self.tab[new_index] is None:
                print("Brak danej")
                return
            if isinstance(self.tab[new_index], Element) and self.tab[new_index].key == key:
                self.tab[new_index] = None
                return

    def __str__(self):
        s = "{"
        for elem in self.tab:
            s += str(elem) + ", "
        return s[:-2] + "}"


def test1(c1, c2):
    tablica = Tablica_Mieszajaca(13, c1, c2)
    litery = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    for i in range(1, 16):
        if i == 6:
            tablica.insert(Element(18, "F"))
            continue
        if i == 7:
            tablica.insert(Element(31, "G"))
            continue
        tablica.insert(Element(i, litery[i - 1]))

    print(tablica)
    print(tablica.search(5))
    print(tablica.search(14))
    tablica.insert(Element(5, "Z"))
    print(tablica.search(5))
    tablica.remove(5)
    print(tablica)
    print(tablica.search(31))
    tablica.insert(Element("test", "W"))
    print(tablica)

def test2(c1, c2):
    tablica = Tablica_Mieszajaca(13, c1, c2)
    litery = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    for i in range(1, 14):
        tablica.insert(Element(i * 13, litery[i - 1]))
    print(tablica)

def main():
    test1(1, 0)
    test2(1, 0)
    test2(0, 1)
    test1(0, 1)


if __name__ == '__main__':
    main()