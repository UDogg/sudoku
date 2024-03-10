# 9x9 Sudoku Solver Program
Graphical sudoku solver with tkinter and Python
### Introduction
This README provides instructions on how to run a Sudoku Solver program written in Python using Tkinter for the graphical user interface (GUI). This program allows users to input Sudoku puzzles and solve them using a **backtracking algorithm.**  

### Requirements
+ Python 3.x installed on your system.
+ Tkinter library (usually comes with Python installation).
+ but if it doesn't run the following
  1. For MacOS
```bash
brew install python-tk@3.9
```
  2. For Linux (Debian-based)
```bash
sudo apt-get install python3-tk
```
  3. For Arch Linux
```bash
sudo pacman -S python-tkinter
```

### Running the program
Follow these steps to run the Sudoku Solver program:
1. Ensure Python 3.x is installed on your system. You can check this by running python --version or python3 --version in your terminal or command prompt. If Python is not installed, download and install it from the official Python website.
2. Clone or download the program files to your local machine. If you have git installed, you can clone the repository using:
```bash
git clone https://github.com/UDogg/sudoku.git
cd sudoku_solver
```
3. If you downloaded the program as a ZIP file, extract it to a directory of your choice.
4. Open a terminal or command prompt and navigate to the directory where you saved the program files.
5. Run the program using Python:
```bash
python sudoku_gui.py
```
or  
```bash
python3 sudoku.py
```
depending on your system's configuration.  

### Using the Sudoku Solver
After launching the program, you will see a 9x9 grid representing a Sudoku puzzle.
+ To input numbers into the puzzle, click on a cell and type a number between 1 and 9.
+ After filling in the initial numbers of the puzzle, click the "Solve" button to solve the puzzle. The program will automatically fill in the remaining cells with the correct numbers using a backtracking algorithm.



