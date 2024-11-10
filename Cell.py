
class Cell:
    def __init__(self, name, empty=True, contain=None):
        self.name =name
        self.empty=empty
        self.contain=contain

    def is_empty(self):
        return self.empty

    def put_stone(self,stone):
        # if not self.empty:
        #     print("Cell is already occupied")
        #     return False
        self.empty = False
        self.contain = stone
        # return True

    def remove_stone(self):
        # if self.empty:
        #     print("cell is already empty")
        #     return False
        self.contain = None
        self.empty = True
        # return True



