'''
This is the main file of the Tetris game.
'''
import tkinter as tk
from tetris import Tetris
def main():
    root = tk.Tk()
    root.title("Tetris")
    tetris = Tetris(root)
    tetris.pack()
    root.mainloop()
if __name__ == "__main__":
    main()