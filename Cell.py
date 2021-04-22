class Cell:
    def __init__(self):
        """
        Constructor for creating a Cell with Dead status
        """
        self._status = 'Dead'

    def set_dead(self):
        """
        method sets the cell status to DEAD
        """
        self._status = 'Dead'

    def set_alive(self):
        """
        method sets the cell status to ALIVE
        """
        self._status = 'Alive'

    def switch_status(self):
        """
        method to switch the status of a cell:
           if DEAD change to ALIVE else change to DEAD
        """
        if self._status == 'Dead':
            self.set_alive()
        else:
            self.set_dead()

    def is_alive(self):
        """
        method checks if the cell is ALIVE
        returns True if it is alive, False if not.
        """
        if self._status == 'Alive':
            return True
        return False

    def get_status(self):
        """
        method to return the status of a cell
        """
        return self._status
