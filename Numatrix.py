import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
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
                        board[row][col] = 0
                return False
    return True

def display_solution(board):
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            cells[i][j].insert(0, str(board[i][j]))

def check_solution():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            value = cells[i][j].get()
            board[i][j] = int(value) if value.isdigit() else 0
    original_board = [row[:] for row in board]
    if solve_sudoku(board):
        if original_board == board:
            messagebox.showinfo("Success", "Congratulations! The solution is correct.")
        else:
            messagebox.showerror("Try Again", "The solution is incorrect. Please try again.")
    else:
        messagebox.showerror("Error", "No solution exists for the given input.")

def show_solution():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            value = cells[i][j].get()
            board[i][j] = int(value) if value.isdigit() else 0
    if solve_sudoku(board):
        display_solution(board)
    else:
        messagebox.showerror("Error", "No solution exists for the given input.")

def initialize_board(puzzle):
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            cells[i][j].config(state='normal')

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                cells[i][j].insert(0, str(puzzle[i][j]))
                cells[i][j].config(state='disabled')

def on_select_difficulty():
    difficulty = difficulty_var.get()
    if difficulty == "Easy":
        puzzle = easy_puzzle
    elif difficulty == "Medium":
        puzzle = medium_puzzle
    else:
        puzzle = hard_puzzle
    initialize_board(puzzle)
    difficulty_frame.pack_forget()

easy_puzzle = [
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

medium_puzzle = [
    [0, 0, 0, 8, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 4, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [6, 0, 0, 9, 0, 4, 0, 0, 0],
    [0, 3, 7, 6, 0, 8, 0, 0, 0],
    [0, 7, 0, 4, 0, 0, 9, 0, 5],
    [0, 5, 0, 0, 8, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 6, 0, 0]
]

hard_puzzle = [
    [0, 0, 0, 0, 9, 0, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 4, 0, 0, 5],
    [0, 7, 0, 0, 6, 0, 0, 9, 0],
    [0, 0, 5, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 4],
    [0, 4, 0, 0, 0, 9, 0, 7, 0],
    [0, 0, 9, 0, 7, 0, 0, 0, 0]
]

root = tk.Tk()
root.title("Sudoku")

cells = [[None for _ in range(9)] for _ in range(9)]
frame = tk.Frame(root)
frame.pack()

difficulty_frame = tk.Frame(root)
difficulty_frame.pack()

difficulty_var = tk.StringVar(value="Easy")
easy_button = tk.Radiobutton(difficulty_frame, text="Easy", variable=difficulty_var, value="Easy", command=on_select_difficulty)
easy_button.pack()
medium_button = tk.Radiobutton(difficulty_frame, text="Medium", variable=difficulty_var, value="Medium", command=on_select_difficulty)
medium_button.pack()
hard_button = tk.Radiobutton(difficulty_frame, text="Hard", variable=difficulty_var, value="Hard", command=on_select_difficulty)
hard_button.pack()

for i in range(9):
    for j in range(9):
        entry = tk.Entry(frame, width=4, font=('Arial', 18), justify='center')
        entry.grid(row=i, column=j, padx=5, pady=5)

        if i % 3 == 0 and j % 3 == 0:
            entry.config(bd=4, relief="solid")  
        elif i % 3 == 0:
            entry.config(bd=1, relief="solid")  
        elif j % 3 == 0:
            entry.config(bd=1, relief="solid")  
        cells[i][j] = entry

check_button = tk.Button(root, text="Check Solution", command=check_solution)
check_button.pack(pady=5)

solve_button = tk.Button(root, text="Watch Solution", command=show_solution)
solve_button.pack(pady=5)

root.mainloop()