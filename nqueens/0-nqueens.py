#!/usr/bin/python3
""" N queens """
import sys

def is_safe(board, row, col, N):
    """Check if a queen can be placed at board safely (row, col)."""
    for i in range(row):
        if board[i] == col or \
        board[i] - i == col - row or \
        board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    """Recursively place queens and store valid solutions."""
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)

def nqueens(N):
    """Solve N-Queens problem and print all solutions."""
    solutions = []
    board = [-1] * N  # Each index represents a row, value represents column
    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

def main():
    """Handle input validation and call the solver."""
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

    nqueens(N)

if __name__ == "__main__":
    main()
