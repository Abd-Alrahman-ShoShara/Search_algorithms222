class Cell:
    def __init__(self, cell_type, is_empty=True, contain=None):
        self.cell_type = cell_type
        self.is_empty = is_empty
        self.contain = contain

    def is_empty(self):
        return self.is_empty

    def put_stone(self, stone):

        if not self.is_empty:
            print("Cell is already occupied")
            return False
        self.is_empty = False
        self.contain = stone
        return True

    def remove_stone(self):

        if self.is_empty:
            print("Cell is already empty")
            return False
        self.is_empty = True
        self.contain = None
        return True
