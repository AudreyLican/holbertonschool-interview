#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row=0, board=[], solutions=[]):
    """Use backtracking to solve the N queens problem."""
    if row == N:
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(N, row + 1, board, solutions)
            board.pop()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(N, board=[], solutions=solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
