from two_zero_four_eight_game.services.run_game import RunGame


class Run:
    def input(self):
        row = int(input("Enter number of rows"))
        col = int(input("Enter number of columns"))
        print("row", row, "column", col)
        RunGame(row, col).start_playing()


if __name__ == "__main__":
    print ("Running two_zero_four_eight_game")
    Run().input()
