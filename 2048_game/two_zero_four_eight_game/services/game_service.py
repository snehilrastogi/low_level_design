


from two_zero_four_eight_game import constants
from two_zero_four_eight_game.services.board_service import BoardService
from two_zero_four_eight_game.utils.fibonacci_util import FibUtil


class GameService:
    @classmethod
    def play(self, board_obj):
        print ("--- game starts ----")
        status = False if int(input("Press 0 to exit and any other key to continue")) == 0 else True
        while (status):
            direction_to_move = (input("Enter Direction - L- left  1 , R - Right- 2, U- Up 3 ,D-Down 4"))
            print direction_to_move
            if direction_to_move == 1:
                print ("left move")
                board_obj = GameService.left_move(board_obj)
                BoardService.print_board(board_obj)
            elif direction_to_move == 2:
                print ("Right move")
                board_obj = GameService.right_move(board_obj)
                BoardService.print_board(board_obj)
            elif direction_to_move == 3:
                print ("UP move")
                board_obj = GameService.up_move(board_obj)
                BoardService.print_board(board_obj)
            elif direction_to_move == 4:
                print ("Down move")
                board_obj = GameService.down_move(board_obj)
                BoardService.print_board(board_obj)
            else:
                print ("wrong input .. exitting")
                exit()
            res = GameService.game_state(board_obj)
            print ("result ", res)
            status = False if int(input("Press 0 to exit nd any other key to continue")) == 0 else True
        print ("--FINISHING--")

    @classmethod
    def _check_fibonacci_number(self, number):
        for fib in FibUtil.fibs():
            if fib == number:
                return True
            if fib > number:
                return False

    @classmethod
    def left_move(self, board_obj):
        """

        :param board_obj:
        :return:
        """
        row = 0
        while row < board_obj.rows:
            col = 1
            merge_op = {}
            while col < board_obj.cols:
                if board_obj.cells[row][col].value == 0:
                    col += 1
                    continue
                elif board_obj.cells[row][col - 1].value == 0:
                    board_obj.cells[row][col - 1].value = board_obj.cells[row][col - 1].value + \
                                                          board_obj.cells[row][col].value
                    board_obj.cells[row][col].value = 0
                    col = 1
                elif not merge_op.get(row) and GameService._check_fibonacci_number(
                                board_obj.cells[row][col - 1].value + board_obj.cells[row][col].value) \
                        and (board_obj.cells[row][col - 1].value != 0):
                    board_obj.cells[row][col - 1].value = board_obj.cells[row][col - 1].value + board_obj.cells[row][
                        col].value
                    board_obj.cells[row][col].value = 0
                    merge_op[row] = 1
                    col = 1
                else:
                    col += 1
            row += 1

        return board_obj

    @classmethod
    def right_move(self, board_obj):
        """

        :param board_obj:
        :return:
        """
        row = 0
        while row < board_obj.rows:
            col = 0
            while col < board_obj.cols - 1:
                if board_obj.cells[row][col].value == 0:
                    col += 1
                    continue
                elif board_obj.cells[row][col + 1] == 0 or self._check_fibonacci_number(
                                board_obj.cells[row][col + 1].value + board_obj.cells[row][col].value):
                    board_obj.cells[row][col + 1].value = board_obj.cells[row][col + 1].value + \
                                                          board_obj.cells[row][col].value
                    board_obj.cells[row][col].value = 0
                    col = 0
                else:
                    col += 1
            row += 1

        return board_obj

    @classmethod
    def up_move(self, board_obj):
        """

        :param board_obj:
        :return:
        """
        row = 1
        col = 0
        merge_op = {}
        while row < board_obj.rows:
            col = 0
            while col < board_obj.cols:
                if board_obj.cells[row][col].value == 0:
                    col += 1
                    continue
                elif board_obj.cells[row - 1][col].value == 0:
                    board_obj.cells[row - 1][col].value = board_obj.cells[row - 1][col].value + \
                                                          board_obj.cells[row][col].value
                    board_obj.cells[row][col].value = 0
                    col += 1
                elif not merge_op.get(col) and self._check_fibonacci_number(board_obj.cells[row - 1][col].value +
                                                                                    board_obj.cells[row][
                                                                                        col].value) and (
                            board_obj.cells[row - 1][col].value != 0):
                    board_obj.cells[row - 1][col].value = board_obj.cells[row][col - 1].value + board_obj.cells[row][
                        col].value
                    board_obj.cells[row][col].value = 0
                    merge_op[col] = 1
                    row = 1
                    col += 1
                else:
                    col += 1
                row += 1

        return board_obj

    @classmethod
    def down_move(self, board_obj):
        """

        :param board_obj:
        :return:
        """
        row = 1
        while row < board_obj.rows - 1:
            col = 0
            while col < board_obj.cols:
                if board_obj.cells[row][col].value == 0:
                    col += 1
                    continue
                elif board_obj.cells[row - 1][col] == 0 or self._check_fibonacci_number(
                                board_obj.cells[row - 1][col].value
                                + board_obj.cells[row]
                        [col].value):
                    board_obj.cells[row - 1][col].value = board_obj.cells[row - 1][col].value + \
                                                          board_obj.cells[row][col].value
                    board_obj.cells[row][col].value = 0
                    row = 1
                else:
                    col += 1
            row += 1

        return board_obj

    @classmethod
    def game_state(self, board_obj):
        for i in range(board_obj.rows):
            for j in range(board_obj.cols):
                if board_obj.cells[i][j].value == 2048:
                    return constants.GAME_STATUSES[constants.WIN]
        print ("After 1")
        for i in range(0, board_obj.rows - 1):
            for j in range(0,
                           board_obj.cols - 1):
                if board_obj.cells[i][j].value == board_obj.cells[i + 1][j].value or board_obj.cells[i][j + 1].value == \
                        board_obj.cells[i][j].value:
                    return constants.GAME_STATUSES[constants.NOT_OVER]
        print ("After 2")
        for i in range(board_obj.rows):
            for j in range(board_obj.cols):
                if board_obj.cells[i][j].value == 0:
                    return constants.GAME_STATUSES[constants.NOT_OVER]
        print ("After 3")
        for k in range(board_obj.rows - 1):
            if board_obj.cells[board_obj.rows - 1][k].value == board_obj.cells[board_obj.rows - 1][k + 1].value:
                return constants.GAME_STATUSES[constants.NOT_OVER]
        print ("After 4")
        for j in range(board_obj.rows - 1):
            if board_obj.cells[j][board_obj.rows - 1].value == board_obj.cells[j + 1][board_obj.rows - 1].value:
                return constants.GAME_STATUSES[constants.NOT_OVER]
        print ("After 5")
        return constants.GAME_STATUSES[constants.LOSE]
