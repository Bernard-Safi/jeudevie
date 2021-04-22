from Board import Board
from tkinter import *


def main():
    game_info = Tk()
    game_info.geometry("1150x500")
    game_info.title("Jeu de vie")
    label = Label(game_info, text="some instructions before proceeding to game :\n"
                                  "when the game start you have an empty board \n"
                                  "board could be filled in multiple ways :\n"
                                  "1- using the generate board button \n"
                                  "2- clicking on cells to change them from dead to alive or alive to dead\n"
                                  "theres two ways to see the iterations : \n"
                                  "1- by clicking on the start button the app run through all the iterations possible"
                                  " or till you click the stop button\n"
                                  "2- by clicking on next iteration button you see only the following iteration\n"
                                  "Finally clear board button will clear the board \n"
                                  "To proceed to game choose grid size and click proceed else close window",
                  anchor="center", font=('Arial', 16, 'bold'))
    rows_lbl = Label(game_info, text="how many rows", font=('Arial', 16, 'bold'), fg="blue")
    columns_lbl = Label(game_info, text="how many columns", font=('Arial', 16, 'bold'), fg="blue")
    rows_entry = Entry(game_info, width=20, font=('Arial', 16, 'bold'))
    columns_entry = Entry(game_info, width=20, font=('Arial', 16, 'bold'))
    proceed_btn = Button(game_info, text=" Proceed", width=12, command=lambda: test(
        game_info, rows_entry.get(), columns_entry.get()))
    label.pack()
    rows_lbl.pack()
    rows_entry.pack()
    columns_lbl.pack()
    columns_entry.pack()
    proceed_btn.pack()
    game_info.mainloop()


def test(root, rows, columns):
    if rows != "" and columns != "" and rows.isnumeric() and columns.isnumeric():
        root.destroy()
        game_of_life_board = Board(int(rows), int(columns))
        game_of_life_board.draw_board()


if __name__ == '__main__':
    main()
