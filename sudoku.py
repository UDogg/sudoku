import tkinter as tk
from tkinter import ttk

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid = []
        self.setup_grid()

    def setup_grid(self):
        # Adjust the default font and size for square appearance
        default_font = ('Arial', 18)
        
        for row in range(9):
            self.grid.append([])
            for col in range(9):
                entry = ttk.Entry(self.root, font=default_font, width=2, justify='center')
                # Determine padding to simulate bold lines
                padx, pady = (0, 0), (0, 0)
                if col in [2, 5]:
                    padx = (0, 10)  # Add extra space on the right of the 3rd and 6th column
                if row in [2, 5]:
                    pady = (0, 10)  # Add extra space below the 3rd and 6th row
                entry.grid(row=row, column=col, padx=padx, pady=pady, sticky="nsew")
                self.grid[row].append(entry)

        solve_button = ttk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9, pady=(10, 0))  # Add some padding above the solve button

    @staticmethod
    def is_valid_move(grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num or grid[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    @staticmethod
    def find_empty_location(grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    @staticmethod
    def solve_sudoku(grid):
        empty = SudokuGUI.find_empty_location(grid)
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if SudokuGUI.is_valid_move(grid, row, col, num):
                grid[row][col] = num
                if SudokuGUI.solve_sudoku(grid):
                    return True
                grid[row][col] = 0
        return False

    def solve(self):
        grid = []
        for row in self.grid:
            current_row = []
            for entry in row:
                val = entry.get()
                current_row.append(int(val) if val.isdigit() else 0)
            grid.append(current_row)

        if SudokuGUI.solve_sudoku(grid):
            for i in range(9):
                for j in range(9):
                    self.grid[i][j].delete(0, tk.END)
                    self.grid[i][j].insert(0, grid[i][j])

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
