'''
This is the main file of the Tetris game.
'''
import tkinter as tk
from tetris import Tetris
def main():
    root = tk.Tk()
    tetris = Tetris(root)
    root.mainloop()
if __name__ == "__main__":
    main()