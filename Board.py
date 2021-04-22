from Cell import Cell
from random import randint
from tkinter import *


class Board:
    def __init__(self, rows, columns):
        """
        constructor take user input and fill the grid with cells +
        creates the buttons with the commands that runs onclick
        """
        self.root = Tk()
        self.root.title("Jeu De Vie")
        self._rows = rows
        self._columns = columns
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]
        self._stop = False
        start_btn = Button(self.root, text="Start", width=12, command=self.start)
        stop_btn = Button(self.root, text="Stop", width=12, command=self.stop)
        generate_board_btn = Button(self.root, text="Generate Board", width=12,
                                    command=lambda: [self._generate_board(), self.draw_board()])
        next_iteration_btn = Button(self.root, text="Next Iteration", width=12, command=self.next)
        clear_board_btn = Button(self.root, text="Clear Board", width=12, command=self.clear)
        start_btn.grid(row=0, column=self._columns + 1)
        stop_btn.grid(row=1, column=self._columns + 1)
        next_iteration_btn.grid(row=2, column=self._columns + 1)
        generate_board_btn.grid(row=3, column=self._columns + 1)
        clear_board_btn.grid(row=4, column=self._columns + 1)

    def draw_board(self):
        """
        method for drawing the board GUI
        """
        for i in range(self._rows):
            for j in range(self._columns):
                if self._grid[i][j].is_alive():
                    e = Entry(self.root, state='readonly',
                              readonlybackground='blue', width=2,
                              font=('Arial', 16, 'bold'))
                else:
                    e = Entry(self.root, state='readonly',
                              readonlybackground='black', width=2,
                              font=('Arial', 16, 'bold'))
                e.bind("<1>", lambda ev: [self._grid[ev.widget.grid_info()["row"]][ev.widget.grid_info()["column"]]
                       .switch_status(), self.draw_board()])
                e.grid(row=i, column=j)
                e.insert(END, self._grid[i][j])

        self.root.update()

    def _generate_board(self):
        """
        method to randomly set cell statuses
        """
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]
        for row in self._grid:
            for column in row:
                chance_number = randint(0, 2)
                if chance_number == 1:
                    column.set_alive()

    def update_board(self):
        """
        method that updates the board
        """
        # cells list for living cells to kill and cells to resurrect or keep alive
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                # check neighbour of the cell:
                check_neighbour = self.check_neighbour(row, column)

                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    # check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.is_alive()

                # If the cell is alive, check the neighbour status.
                if status_main_cell:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        # set cell statuses
        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()

    def have_next_iteration(self):
        """
        method to check if theres more iterations left
        """
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                # check neighbour of the cell:
                check_neighbour = self.check_neighbour(row, column)

                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    # check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.is_alive()

                # If the cell is alive, check the neighbour status.
                if status_main_cell:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)
        return not goes_alive and not gets_killed

    def check_neighbour(self, check_row, check_column):
        """
        method that checks all the neighbours for all the cells
        and returns the list of the valid neighbours so the update
        method can set the new status
        """
        neighbour_list = []
        for row in range(-1, 2):
            for column in range(-1, 2):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                valid_neighbour = True

                if neighbour_row == check_row and neighbour_column == check_column:
                    valid_neighbour = False

                if neighbour_row < 0 or neighbour_row >= self._rows:
                    valid_neighbour = False

                if neighbour_column < 0 or neighbour_column >= self._columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self._grid[neighbour_row][neighbour_column])
        return neighbour_list

    def start(self):
        """
        method that runs when the start button is clicked
        """
        self._stop = False
        while not self.have_next_iteration() and not self._stop:
            self.root.after(3000, self.update_board())
            self.draw_board()

    def stop(self):
        """
        method that runs when the stop button is clicked
        """
        self._stop = True

    def next(self):
        """
        method that runs when the next button is clicked
        """
        self.update_board()
        self.draw_board()

    def clear(self):
        """
        method that runs when the clear board button is clicked
        """
        for i in range(self._rows):
            for j in range(self._columns):
                self._grid[i][j].set_dead()
        self.draw_board()
