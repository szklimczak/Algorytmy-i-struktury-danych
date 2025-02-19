# Skończone

class Element:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None
    
    def add(self, data):
        nowy_element = Element(data, self.head)
        self.head = nowy_element

    def append(self, data):
        nowy_element = Element(data)
        if not self.head:
            self.head = nowy_element
        else:
            ostatni = self.head
            while ostatni.next:
                ostatni = ostatni.next
            ostatni.next = nowy_element
    
    def remove(self):
        if not self.head:
            return None
        self.head = self.head.next

    def remove_end(self):
        if not self.head:
            return None
        elif self.length() == 1:
            self.head = None
        else:
            wsk = self.head
            ostatni = self.head
            while wsk.next is not None:
                ostatni = wsk
                wsk = wsk.next
            ostatni.next = None
        
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

    uczelnie = LinkedList()
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