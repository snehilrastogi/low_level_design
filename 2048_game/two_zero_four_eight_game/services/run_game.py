from two_zero_four_eight_game.services.board_service import BoardService
from two_zero_four_eight_game.services.game_service import GameService


class RunGame:
    """
    All inputs follow zero indexing
    """

    def __init__(self, total_row, total_column):
        self.rows = total_row
        self.col = total_column

    def start_playing(self, ):
        # 1. initialize board
        board_obj = BoardService.initialize_board(self.rows, self.col)
        board_obj = self.get_initial_values(board_obj)
        # now play
        GameService.play(board_obj)

    def get_initial_values(self, board_obj):
        """

        :param board_obj:
        :return: updated board_obj
        """
        # mapped_values = map(int, input("Enter two initial positions where the vale will be preloaded in "
        #                                         "order -- row1 col1 row2 col2 and separated by comma"))
        mapped_values = [1, 1, 1, 2]
        print (mapped_values)
        row1, col1, row2, col2 = [val for val in mapped_values]
        print("row1", row1, "col1", col1)
        board_obj = BoardService.update_initial_values(board_obj, int(row1), int(col1), 2)
        print("row2", row2, "col2", col2)
        board_obj = BoardService.update_initial_values(board_obj, int(row2), int(col2), 2)
        return board_obj
