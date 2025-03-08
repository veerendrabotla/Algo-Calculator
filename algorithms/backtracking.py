def n_queens(n):
    """Solve the N-Queens problem using backtracking."""
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve_n_queens_util(board, col):
        if col >= n:
            result.append([''.join('Q' if cell else '.' for cell in row) for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve_n_queens_util(board, col + 1)
                board[i][col] = 0  # Backtrack

    result = []
    board = [[0] * n for _ in range(n)]
    solve_n_queens_util(board, 0)
    return result


def sudoku_solver(board):
    """Solve a Sudoku puzzle using backtracking."""
    def is_valid(board, row, col, num):
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve_sudoku(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve_sudoku(board):
                                return True
                            board[row][col] = 0  # Backtrack
                    return False
        return True

    solve_sudoku(board)
    return board