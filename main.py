from datetime import datetime
import copy

max_tree_depth: int = 0
backtracking_execution_counter: int = 0

sudoku = [[0, 0, 7, 0, 0, 9, 0, 4, 5],
                   [9, 3, 0, 7, 0, 8, 0, 6, 0],
                   [6, 0, 0, 0, 5, 0, 0, 0, 7],
                   [0, 0, 0, 0, 8, 0, 0, 7, 0],
                   [0, 0, 0, 0, 0, 0, 0, 3, 0],
                   [7, 4, 2, 0, 6, 3, 9, 1, 0],
                   [0, 0, 0, 2, 0, 0, 0, 0, 6],
                   [0, 6, 0, 9, 1, 0, 0, 0, 3],
                   [1, 0, 3, 0, 0, 0, 0, 0, 0]]

solutions: [[[int]]] = []

def backtracking(current_tree_depth: int) -> None:
    global backtracking_execution_counter
    backtracking_execution_counter += 1
    save_max_tree_depth(current_tree_depth)
    if all_fields_filled():
        solutions.append(copy.deepcopy(sudoku))
        return # Found one solution
    row, col = next_empty_field()
    for number in range(1, 10):
        if number_allowed(row, col, number):
            sudoku[row][col] = number
            backtracking(current_tree_depth + 1)
            sudoku[row][col] = 0
    return

def number_allowed(row, col, number) -> bool:
    # number allowed in row
    for col_temp in range(0, 9):
        if sudoku[row][col_temp] == number:
            return False
    # number allowed in col
    for row_temp in range(0, 9):
        if sudoku[row_temp][col] == number:
            return False
    # number allowed in small square
    x_square: int = int(row / 3)
    y_square: int = int(col / 3)
    for row_temp in range(x_square * 3, x_square * 3 + 3):
        for col_temp in range(y_square * 3, y_square * 3 + 3):
            if sudoku[row_temp][col_temp] == number:
                return False
    return True

def all_fields_filled() -> bool:
    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                return False
    return True

def next_empty_field() -> (int, int):
    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                return row, col

def print_sudoku(temp_sudoku: [[]]):
    sudoku_row: str
    for row in range(0, 9):
        if divmod(row, 3)[1] == 0:
            print('*' * 13)
        sudoku_row = ''
        for col in range (0, 9):
            if divmod(col, 3)[1] == 0:
                sudoku_row += '*'
            sudoku_row += str(temp_sudoku[row][col])
        sudoku_row += '*'
        print(sudoku_row)
    print('*' * 13)

def save_max_tree_depth(current_depth: int):
    global max_tree_depth
    if current_depth > max_tree_depth:
        max_tree_depth = current_depth

if __name__ == '__main__':
    time_start = datetime.now()
    backtracking(1)
    time_stop = datetime.now()
    if len(solutions) > 0:
        print("Sudoku solved")
        print("Number of solutions found:", str(len(solutions)))
        for solution in solutions:
            print_sudoku(solution)
    else:
        print("Sudoku not solved")
    time_duration = time_stop - time_start
    print("Duration: " + str(time_duration.microseconds) + " microseconds")
    print("Number of nodes evaluated: " + str(backtracking_execution_counter))
    print("Maximal tree depth: " + str(max_tree_depth))