'''
This is the main file of the Tetris application.
'''
import tkinter as tk
from tetris import TetrisGame
def main():
    root = tk.Tk()
    root.title("Tetris")
    game = TetrisGame(root)
    game.start()
    root.mainloop()
if __name__ == "__main__":
    main()