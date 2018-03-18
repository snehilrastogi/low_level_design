from two_zero_four_eight_game.models.board import Board
from two_zero_four_eight_game.models.cell import Cell
from two_zero_four_eight_game.services.base_service import BaseService


class BoardService(BaseService):
    """
    initialize board - created the board - matrix of rows and columns and (list of lists) and at the same time initialize it with 0
    """

    @classmethod
    def initialize_board(self, rows, cols):
        board_obj = Board(rows, cols)
        for row in range(board_obj.rows):
            for col in range(board_obj.cols):
                board_obj.cells[row].append(Cell(row, col, 0))

        BoardService.print_board(board_obj)

        return board_obj

    @classmethod
    def update_initial_values(self, board_obj, row, col, value=0):
        """

        :param board_obj:
        :return: updated board_obj
        """
        board_obj = board_obj.update_board(row, col, value)
        BoardService.print_board(board_obj)
        return board_obj

    @classmethod
    def print_board(cls, board_obj):
        print("-------Updated Board --------")
        for row in range(0, board_obj.rows):
            for col in range(0, board_obj.cols):
                print("row", row, "col", col, "value --", board_obj.cells[row][col].value)
