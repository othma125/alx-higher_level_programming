#!/usr/bin/python3
"""N queen task
"""


class Board:
    """Board class
    """

    def __init__(self, n):
        """
        board constructor
        :param N:
        :type N: integer
        """
        self.__N = n
        self.__board = [[] for _ in range(self.__N)]

    def __get_solution(self):
        """Return the list of lists representation of a solved chessboard."""
        solution = []
        for r in range(self.__N):
            for c in range(self.__N):
                if board[r][c] == "Q":
                    solution.append([r, c])
                    break
        return solution


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
    for sol in board.back_track(0, 0, []):
        print(sol)
