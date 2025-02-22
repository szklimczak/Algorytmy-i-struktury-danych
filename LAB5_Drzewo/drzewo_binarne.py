# Skończone

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        elem = self.root
        if elem is None:
            return None
        if elem.key == key:
            return elem.value
        else:
            return self.search_rek(key, elem)

    def search_rek(self, key, elem):
        if elem is None:
            return None
        if elem.key == key:
            return elem.value
        if key > elem.key:
            return self.search_rek(key, elem.right)
        if key < elem.key:
            return self.search_rek(key, elem.left)

    def insert(self, key, value):
        if self.root is None:
            self.root = Element(key, value)
        else:
            self.root = self.insert_rek(self.root, key, value)

    def insert_rek(self, elem, key, value):
            if elem is None:
                return Element(key, value)
            if key > elem.key:
                elem.right = self.insert_rek(elem.right, key, value)
                return elem
            elif key < elem.key:
                elem.left = self.insert_rek(elem.left, key, value)
                return elem
            else:
                elem.value = value
                return elem

    def delete(self, key):
        elem = self.root
        return self.delete_rek(elem, key)
    
    def delete_rek(self, elem, key):
        if elem is None:
            return elem
        if key < elem.key:
            elem.left = self.delete_rek(elem.left, key)
        elif key > elem.key:
            elem.right = self.delete_rek(elem.right, key)
        else:
            if elem.left is None:
                return elem.right   
            elif elem.right is None:
                return elem.left
            successor = elem.right
            while successor.left is not None:
                successor = successor.left
            elem.key = successor.key
            elem.value = successor.value
            elem.right = self.delete_rek(elem.right, successor.key)
        return elem
    
    def print(self):
        self.print_rek(self.root)
        print()

    def print_rek(self, elem):
        if elem.left:
            self.print_rek(elem.left)
        print(elem.key, elem.value, end = ", ")
        if elem.right:
            self.print_rek(elem.right)

    def height(self):
        return self.height_rek(self.root)

    def height_rek(self, elem):
        if elem is None:
            return -1
        left_height = self.height_rek(elem.left)
        right_height = self.height_rek(elem.right)
        return 1 + max(left_height, right_height)

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)


def main():
    tree = BST()
    elementy = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key, value in elementy.items():
        tree.insert(key, value)
    tree.print_tree()
    tree.print()
    print(tree.search(24))
    tree.insert(20, 'AA')
    tree.insert(6, 'M')
    tree.delete(62)
    tree.insert(59, 'N')
    tree.insert(100, 'P')
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, 'R')
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    tree.print()
    tree.print_tree()


if __name__ == '__main__':
    main()