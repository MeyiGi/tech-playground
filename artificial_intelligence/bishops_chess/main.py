def backtracking_bishops(n=4):
    solutions = []
    board = [-1] * n  # board[row] = column

    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            if abs(prev_row - row) == abs(prev_col - col):
                return False
        return True

    def solve(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    solve(0)
    return solutions


solutions_backtracking = backtracking_bishops(5)
print("Количество решений (1 слон в строке):", len(solutions_backtracking))
