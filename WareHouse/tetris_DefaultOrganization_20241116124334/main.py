'''
This is the main file that runs the Tetris game.
'''
import tkinter as tk
from tetris import Tetris
def main():
    root = tk.Tk()
    tetris = Tetris(root)
    tetris.start()
    root.mainloop()
if __name__ == "__main__":
    main()