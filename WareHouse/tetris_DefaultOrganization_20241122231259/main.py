'''
This is the main file of the Tetris game. It initializes the game and starts the GUI.
'''
import tkinter as tk
from tetris import Tetris
def main():
    root = tk.Tk()
    root.title("Tetris")
    tetris = Tetris(root)
    root.bind("<Left>", lambda event: tetris.move_piece("left"))
    root.bind("<Right>", lambda event: tetris.move_piece("right"))
    root.bind("<Down>", lambda event: tetris.move_piece("down"))
    root.bind("<Up>", lambda event: tetris.rotate_piece())
    root.after(1000, tetris.update_board)
    tetris.start_game()
    root.mainloop()
if __name__ == "__main__":
    main()