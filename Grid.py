from Cell import Cell
from Stone import Stone


class Grid:
    def __init__(self, width, moves):
        self.width = width
        self.moves = moves
        self.grid = [[Cell("nCell") for _ in range(width)] for _ in range(width)]

    def put_stone(self, x, y, stone):
        if x < 0 or x >= self.width or y < 0 or y >= self.width:
            print("Invalid position. Out of grid bounds.")
            return False

        cell = self.grid[x][y]
        stone.set_position(x, y)
        if not cell.put_stone(stone):
            return False
        return True

    def set_cell_type(self, x, y, cell_type):
        if x < 0 or x >= self.width or y < 0 or y >= self.width:
            print("Invalid position. Out of grid bounds.")
            return False
        self.grid[x][y].cell_type = cell_type
        return True

    def display_grid(self):
        for row in self.grid:
            row_display = []
            for cell in row:
                cell_info = f"{cell.cell_type}"

                if cell.is_empty:
                    cell_info += ": Empty   "
                else:

                    if isinstance(cell.contain, Stone):
                        if cell.contain.s_Type == "iron":
                            cell_info += ": Iron    "
                        elif cell.contain.s_Type in ["N","s"]:
                            cell_info += f": Magnet_{cell.contain.s_Type}"

                row_display.append(cell_info)

            print(" | ".join(row_display))
            print("-" * (self.width * 15))
