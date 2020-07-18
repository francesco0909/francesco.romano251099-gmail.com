import time

class Queens():

    def __init__(self,size):
        self.size = size
        self.answers = 0
        queens = [0] * self.size
        self.solve(queens, 0, 0)
        print("There are", self.answers, "answers for this size.")

    def printBoard(self, queens):
        self.board = []
        for i in range(self.size):
            self.board.append((["□"] * self.size))
            temp = queens[i]
            self.board[i][temp] = "■"
            print(self.board[i])
        print("\n")

    def solve(self, queens, row, column):
        if row == self.size:
            self.answers +=1
            print(queens)
            self.printBoard(queens)
            return True
        else:
            while column < self.size:
                if self.check(queens, row, column):
                    queens[row] = column
                    self.solve(queens, row + 1, 0)
                column += 1

    def check(self, queens ,row ,column):
        for i in range (row):
            if queens[i] == column:
                return False
            if column + row == queens[i] + i:
                return False
            if column - row == queens[i] - i:
                return False
        return True

time_1 = time.time()
Queens(8)
time_2 = time.time()
print("It took", time_2 - time_1, "seconds to run the program!")
