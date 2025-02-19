# Skończone

class Element:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def destroy(self):
        obecny = self.head
        while obecny:
            nastepny = obecny.next
            del obecny
            obecny = nastepny
        self.head = None
        self.tail = None
    
    def add(self, data):
        nowy_element = Element(data)
        if not self.head:
            self.head = self.tail = nowy_element
        else:
            nowy_element.next = self.head
            self.head.prev = nowy_element
            self.head = nowy_element
        

    def append(self, data):
        nowy_element = Element(data)
        if not self.head:
            self.head = self.tail = nowy_element
        else:
            nowy_element.prev = self.tail
            self.tail.next = nowy_element
            self.tail = nowy_element
    
    def remove(self):
        if not self.head:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove_end(self):
        if not self.tail:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
    def is_empty(self):
        return self.head is None

    def length(self):
        ile = 0
        obecny_element = self.head
        while obecny_element != None:
            ile += 1
            obecny_element = obecny_element.next
        return ile

    def get(self):
        if not self.head:
            return None
        return self.head.data

    def display(self):
        obecny = self.head
        while obecny:
            print("->", obecny.data)
            obecny = obecny.next


def main():
    dene_uczelni = [
        ('AGH', 'Kraków', 1919),
        ('UJ', 'Kraków', 1364),
        ('PW', 'Warszawa', 1915),
        ('UW', 'Warszawa', 1915),
        ('UP', 'Poznań', 1919),
        ('PG', 'Gdańsk', 1945)
    ]

    uczelnie = DoubleLinkedList()
    for data in dene_uczelni[:3]:
        uczelnie.append(data)
    for data in dene_uczelni[3:]:
        uczelnie.add(data)
    uczelnie.display()
    print(uczelnie.length())
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    uczelnie.display()
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(('AGH', 'Kraków', 1919))
    uczelnie.remove_end()
    print(uczelnie.is_empty())


if __name__ == '__main__':
    main()