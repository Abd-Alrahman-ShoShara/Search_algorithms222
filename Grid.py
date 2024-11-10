from Cell import Cell
from Stone import Stone
class Grid:

    def __init__(self,width,moves):
        self.width=width
        self.moves=moves
        self.grid = [[Cell("nCell") for _ in range(width)] for _ in range(width)]

    def put_stone(self,x,y,stone):
        if x < 0 or x >= self.width or y < 0 or y >= self.width:
            print("Invalid position. Out of grid bounds.")
            return False

        cell = self.grid[x][y]

        return cell.put_stone(stone)

    def set_cell_type(self, x, y, cell_type):
        if x < 0 or x >= self.width or y < 0 or y >= self.width:
            print("Invalid position. Out of grid bounds.")
            return False
        self.grid[x][y].name = cell_type
        return True

    def display_grid(self):
        for row in self.grid:
            row_display = []
            for cell in row:
                cell_info = f"{cell.name}"

                if cell.empty:
                    cell_info += ": Empty   "  # If cell is empty, indicate it's empty
                else:

                    if isinstance(cell.contain, Stone):
                        if cell.contain.s_Type == "iron":
                            cell_info += ": Iron    "
                        elif cell.contain.s_Type == "magnet":
                            cell_info += f": Magnet_{cell.contain.m_Type}"

                row_display.append(cell_info)

            # Print the row information
            print(" | ".join(row_display))
            print("-" * (self.width * 15))  # Line separator adjusted for readability
        #     cell=self.grid[1][2]
        # print(cell.empty)

    def get_mag(self):
        for i in range(self.width):
            for j in range(self.width):
                cell = self.grid[i][j]
                if cell.contain and isinstance(cell.contain,Stone):
                    return cell.contain

    # def move_stone(self, from_x, from_y, to_x, to_y):
    #     # Check if the source and destination coordinates are valid
    #     if not (0 <= from_x < self.width and 0 <= from_y < self.width):
    #         print("Invalid source cell coordinates.")
    #         return
    #     if not (0 <= to_x < self.width and 0 <= to_y < self.width):
    #         print("Invalid destination cell coordinates.")
    #         return
    #
    #     # Get the source and target cells
    #     from_cell = self.grid[from_x][from_y]
    #     to_cell = self.grid[to_x][to_y]
    #
    #     # Check if the source cell contains a valid stone (blue or red magnet)
    #     if from_cell.is_empty() or from_cell.contain.s_Type not in ["blue", "redd"]:
    #         print("Only blue and red magnets can be moved.")
    #         return
    #
    #     # Check if the destination cell is empty or a target (if not, it's blocked)
    #     if not to_cell.is_empty() and to_cell.name != "target":
    #         print("Destination cell is either occupied or blocked.")
    #         return
    #
    #     # Get the stone to move
    #     stone = from_cell.contain
    #
    #     # Move the stone to the destination cell
    #     if to_cell.put_stone(stone):  # Place the stone in the target cell
    #         from_cell.remove_stone()  # Remove the stone from the source cell
    #
    #         # Record the move
    #         self.moves.append(((from_x, from_y), (to_x, to_y)))
    #
    #         # Apply repulsion or attraction based on the stone type
    #         if stone.s_Type == "blue":
    #             self.apply_repulsion(to_x, to_y)
    #         elif stone.s_Type == "redd":
    #             self.apply_attraction(to_x, to_y)
    #
    #         # Check if the player has won
    #         if self.check_win():
    #             print("You won the level!")
    #             print("Moves you made:")
    #             for move in self.moves:
    #                 print(f"From {move[0]} to {move[1]}")

