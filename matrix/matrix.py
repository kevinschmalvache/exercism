class Matrix:

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        rows = self.matrix_string.split('\n')[index - 1].split(' ')
        return list(map(int, rows))

    def column(self, index):
        return [int(i.split(' ')[index - 1]) for i in self.matrix_string.split('\n')]
