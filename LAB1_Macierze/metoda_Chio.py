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


def wyznacznik_2x2(matrix: Macierz):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def swap_rows(matrix: Macierz, i, j):
    new_matrix = [row[:] for row in matrix]
    new_matrix[i], new_matrix[j] = new_matrix[j], new_matrix[i]
    return Macierz(new_matrix)


def metoda_Chio(matrix: Macierz, wsp = 1.0):
    if matrix.size()[0] != matrix.size()[1]:
        return None
    
    if matrix.size() == (2, 2):
        return wsp * wyznacznik_2x2(matrix)
    
    if matrix[0][0] == 0:
        for i in range(1, matrix.size()[0] + 1):
            if matrix[i][0] != 0:
                matrix = swap_rows(matrix, 0, i)
                wsp *= -1
                break
    
    nowy_wsp = wsp / (matrix[0][0] ** (matrix.size()[0] - 2))

    new_matrix = []
    for i in range(matrix.size()[0] - 1):
        new_row = []
        for j in range(matrix.size()[0] - 1):
            new_row.append(wyznacznik_2x2(Macierz([[matrix[0][0], matrix[0][j + 1]], [matrix[i + 1][0], matrix[i + 1][j + 1]]])))
        new_matrix.append(new_row)
    return metoda_Chio(Macierz(new_matrix), nowy_wsp)


def wyznacznik(matrix: Macierz):
    if matrix.size() == (2, 2):
        return wyznacznik_2x2(matrix)
    else:
        return metoda_Chio(matrix)


def main():
    m1 = Macierz([[0, 1, 1, 2, 3],
                 [4, 2, 1, 7, 3],
                 [2, 1, 2, 4, 7],
                 [9, 1, 0, 7, 0],
                 [1, 4, 7, 2, 2]])
    print(wyznacznik(m1))

if __name__ == '__main__':
    main()