class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[] for i in range(self.rows)]

    def update_board(self, row, col, value=0):
        cell_obj = self.cells[row][col]
        cell_obj.update_cell_value(value)
        return self


