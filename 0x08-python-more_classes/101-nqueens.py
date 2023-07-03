#!/usr/bin/python3
"""N queen task
"""


class Board:
    """Board class
    """

    def __init__(self, n):
        """
        board constructor
        :param n:
        :type n: integer
        """
        self.N = n
        self.board = [[' ' for _ in range(self.N)] for _ in range(self.N)]

    def get_solution(self):
        """Return the matrix representation of a solved chessboard.
        """
        solutions = []
        for r in range(self.N):
            for c in range(self.N):
                if self.board[r][c] == "Q":
                    solutions.append([r, c])
                    break
        return solutions

    def clone(self):
        new = Board(self.N)
        for i in range(self.N):
            for j in range(self.N):
                new.board[i][j] = self.board[i][j]
        return new

    def Xout(self, row, col):
        """
        all spots where non-attacking queens can no
        longer be played are X-ed out.
        """
        for c in range(col + 1, self.N):
            self.board[row][c] = "x"
        for c in range(col - 1, -1, -1):
            self.board[row][c] = "x"
        for r in range(row + 1, self.N):
            self.board[r][col] = "x"
        for r in range(row - 1, -1, -1):
            self.board[r][col] = "x"
        c = col + 1
        for r in range(row + 1, self.N):
            if c >= self.N:
                break
            self.board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            self.board[r][c] = "x"
            c -= 1
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c >= self.N:
                break
            self.board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row + 1, self.N):
            if c < 0:
                break
            self.board[r][c] = "x"
            c -= 1

    def back_track(self, r, queens, solutions):
        """ return the solution using backtrack technique.
        """
        if queens == self.N:
            solutions.append(self.get_solution())
            return solutions
        for c in range(self.N):
            if self.board[r][c] == " ":
                cpy = self.clone()
                cpy.board[r][c] = "Q"
                cpy.Xout(r, c)
                solutions = cpy.back_track(r + 1, queens + 1, solutions)
                # return cpy.back_track(r + 1, queens + 1, solutions)
        return solutions


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = Board(N)
    for solution in board.back_track(0, 0, []):
        print(solution)
