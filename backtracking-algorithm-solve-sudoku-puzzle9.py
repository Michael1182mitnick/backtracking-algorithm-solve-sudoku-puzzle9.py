# backtracking_algorithm_solve_sudoku_puzzle
# Implement a solver for a Sudoku puzzle using backtracking to fill in the missing numbers while satisfying all Sudoku rules.

# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Check if placing num at board[row][col] is valid


def is_valid(board, row, col, num):
    # Check if the number is in the row
    if num in board[row]:
        return False

    # Check if the number is in the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Backtracking algorithm to solve the Sudoku puzzle


def solve_sudoku(board):
    # Find the next empty space (denoted by 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try placing numbers from 1 to 9 in the empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number

                        # Recursively try to solve the rest of the board
                        if solve_sudoku(board):
                            return True

                        # Backtrack: reset the cell if placing num doesn't lead to a solution
                        board[row][col] = 0

                # If no number fits, return False (backtrack)
                return False

    # Return True when the board is completely solved
    return True


# Example usage with a Sudoku puzzle
if __name__ == "__main__":
    # 0 represents empty cells
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku puzzle:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists!")
