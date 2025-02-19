# Skończone

class Macierz:
    def __init__(self, matrix, value=0):
        if isinstance(matrix, tuple):
            self.rows, self.cols = matrix
            self.matrix = [[value for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.matrix = matrix

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        if self.size() != other.size():
            return None
 
        suma = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.size()[1])] for i in range(self.size()[0])]
        return Macierz(suma)
    
    def __mul__(self, other):
        if self.size()[1] != other.size()[0]:
            return None         

        iloczyn = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.size()[1])) for j in range(other.size()[1])] for i in range(self.size()[0])]
        return Macierz(iloczyn)

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        wynik = ""
        for row in self.matrix:
            wynik += "| " + " ".join(str(elem) for elem in row) + " |\n"
        return wynik


def transpozycja(matrix: Macierz):
    rows, cols = matrix.size()
    macierz_transponowana = Macierz((cols, rows))
    for i in range(rows):
        for j in range(cols):
            macierz_transponowana[j][i] = matrix[i][j]
    return macierz_transponowana


def main():
    m1 = Macierz([[1, 0, 2], [-1, 3, 1]])
    print(transpozycja(m1))
    m2 = Macierz((2, 3), value=1)
    print(m1 + m2)
    m3 = Macierz([[3, 1], [2, 1], [1, 0]])
    print(m1 * m3)

if __name__ == '__main__':
    main()