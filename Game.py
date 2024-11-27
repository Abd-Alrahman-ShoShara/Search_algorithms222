from Grid import Grid
import copy
class Game:
    def __init__(self,width,moves,level):
        self.moves_done=[]
        self.cost = 0
        self.level = level
        self.grid=Grid(width,moves)

    def display_game(self):
        print(f"Game Level {self.level} - Grid size: {self.grid.width}x{self.grid.width}, Moves allowed: {self.grid.moves}")
        self.grid.display_grid()

    def move_stone_for_al(self, from_x: int, from_y: int, to_x: int, to_y: int):

        board_copy = copy.deepcopy(self)

        if not (0 <= from_x < board_copy.grid.width and 0 <= from_y < board_copy.grid.width):
            raise IndexError("Stone position out of board bounds")
        if not (0 <= to_x < board_copy.grid.width and 0 <= to_y < board_copy.grid.width):
            raise IndexError("Stone position out of board bounds")

        from_cell = board_copy.grid.grid[from_x][from_y]
        to_cell = board_copy.grid.grid[to_x][to_y]

        if from_cell.is_empty or from_cell.contain.s_Type not in ["N", "S"]:
            raise IndexError("Only magnets (type 'N' or 'S') can be moved.")

        if not to_cell.is_empty and to_cell.cell_type not in ["nCell", "gCell"]:
            raise IndexError("Target cell is not empty or is blocked.")

        stone = from_cell.contain
        stone.set_position(to_x, to_y)
        to_cell.put_stone(stone)
        from_cell.remove_stone()

        board_copy.moves_done.append(((from_x, from_y), (to_x, to_y)))

        if stone.s_Type == "N":
            board_copy.move_stones_around_for_n(to_x, to_y)
        elif stone.s_Type == "S":
            board_copy.move_stones_around_for_s(to_x, to_y)

        if board_copy.grid.moves == 0:
            raise IndexError("No more moves left.")

        board_copy.grid.moves -= 1

        return board_copy



    # def move_magnet(self, magnet, new_x, new_y):
    #
    #     if not (0 <= new_x < self.grid.width and 0 <= new_y < self.grid.width):
    #         print("New position is out of grid bounds.")
    #         return False
    #
    #     current_x, current_y = magnet.x, magnet.y
    #
    #     if not (0 <= current_x < self.grid.width and 0 <= current_y < self.grid.width):
    #         print(f"Error: Current position of the magnet ({current_x}, {current_y}) is out of bounds.")
    #         return False
    #
    #     target_cell = self.grid.grid[new_x][new_y]
    #
    #     if (target_cell.cell_type == "nCell" or target_cell.cell_type == "gCell") and target_cell.is_empty:
    #
    #         self.grid.put_stone(new_x, new_y, magnet)
    #         self.grid.grid[current_x][current_y].remove_stone()
    #         magnet.set_position(new_x, new_y)
    #
    #         self.grid.moves -= 1
    #
    #         if magnet.s_Type == "N":
    #             self.move_stones_around_for_n(new_x, new_y)
    #         else:
    #             self.move_stones_around_for_s(new_x, new_y)
    #
    #         if self.check_win():
    #             print("You won!")
    #             self.display_game()
    #         elif self.check_lose():
    #             print("No moves left. You lost.")
    #         else:
    #             print("You haven't won yet.")
    #         return True
    #     else:
    #         print("Target cell is not empty or is blocked.")
    #         return False
    def move_magnet(self, magnet, new_x, new_y):
        # self=copy.deepcopy(self)
        if not (0 <= new_x < self.grid.width and 0 <= new_y < self.grid.width):
            print("New position is out of grid bounds.")
            return False

        current_x, current_y = None, None
        for i in range(self.grid.width):
            for j in range(self.grid.width):
                cell = self.grid.grid[i][j]
                if cell.contain == magnet:
                    current_x, current_y = i, j
                    break
            if current_x is not None:
                break

        if current_x is None or current_y is None:
            print("Magnet not found on the grid.")
            return False

        target_cell = self.grid.grid[new_x][new_y]

        if (target_cell.cell_type == "nCell" or target_cell.cell_type == "gCell") and target_cell.is_empty:
            self.grid.put_stone(new_x, new_y, magnet)
            self.grid.grid[current_x][current_y].remove_stone()
            self.grid.moves -= 1

            if magnet.s_Type == "N":
                self.move_stones_around_for_n(new_x, new_y)
            else:
                self.move_stones_around_for_s(new_x, new_y)

            self.display_game()
            if self.check_win():
                print(" You won ")
            elif self.check_lose():
                print("No moves left. You lost.")
            else:
                print("You haven't won yet.")
            return True
        else:
            print("Target cell is not empty or is blocked.")
            return False

    def move_stones_around_for_n(self, x: int, y: int):
        # Right
        start = y + 1
        while start < self.grid.width and not self.grid.grid[x][start].contain:
            start += 1

        if start < self.grid.width:
            end = start
            while end < self.grid.width and (self.grid.grid[x][end].contain or self.grid.grid[x][end].cell_type == 'bCell'):
                end += 1
            if end < self.grid.width:
                while end != start:
                    start_cell = self.grid.grid[x][end - 1]
                    end_cell = self.grid.grid[x][end]
                    if start_cell.contain and end_cell.is_empty and end_cell.cell_type != 'bCell':
                        end_cell.put_stone(start_cell.contain)
                        start_cell.remove_stone()
                    end -= 1
        # Left
        start = y - 1
        while start >= 0 and not self.grid.grid[x][start].contain:
            start -= 1
        if start >= 0:
            end = start
            while end >= 0 and (self.grid.grid[x][end].contain or self.grid.grid[x][end].cell_type == 'bCell'):
                end -= 1
            if end >= 0:
                while end != start:
                    start_cell = self.grid.grid[x][end + 1]
                    end_cell = self.grid.grid[x][end]
                    if start_cell.contain and end_cell.is_empty and end_cell.cell_type != 'bCell':
                        end_cell.put_stone(start_cell.contain)
                        start_cell.remove_stone()
                    end += 1
        # down
        start = x + 1
        while start < self.grid.width and not self.grid.grid[start][y].contain:
            start += 1
        if start < self.grid.width:
            end = start
            while end < self.grid.width and (self.grid.grid[end][y].contain or self.grid.grid[end][y].cell_type == 'bCell'):
                end += 1
            if end < self.grid.width:
                while end != start:
                    start_cell = self.grid.grid[end - 1][y]
                    end_cell = self.grid.grid[end][y]
                    if start_cell.contain and end_cell.is_empty and end_cell.cell_type != 'bCell':
                        end_cell.put_stone(start_cell.contain)
                        start_cell.remove_stone()
                    end -= 1
        # up
        start = x - 1
        while start >= 0 and not self.grid.grid[start][y].contain:
            start -= 1
        if start >= 0:
            end = start
            while end >= 0 and (self.grid.grid[end][y].contain or self.grid.grid[end][y].cell_type == 'bCell'):
                end -= 1
            if end >= 0:
                while end != start:
                    start_cell = self.grid.grid[end + 1][y]
                    end_cell = self.grid.grid[end][y]
                    if start_cell.contain and end_cell.is_empty and end_cell.cell_type != 'bCell':
                        end_cell.put_stone(start_cell.contain)
                        start_cell.remove_stone()
                    end += 1


    def move_stones_around_for_s(self,x,y):
        # right
        for dy in range(y + 1, self.grid.width):
            current_cell = self.grid.grid[x][dy]
            if not current_cell.is_empty:
                next_y = dy -1
                if next_y >=0:
                    next_cell = self.grid.grid[x][next_y]
                    if next_cell.is_empty:
                        self.grid.put_stone(x,next_y,current_cell.contain)
                        current_cell.remove_stone()

        for dy in range(y - 1, -1, -1):
            current_cell = self.grid.grid[x][dy]
            if not current_cell.is_empty:
                next_y = dy + 1
                if next_y < self.grid.width:
                    next_cell = self.grid.grid[x][next_y]
                    if next_cell.is_empty:
                        self.grid.put_stone(x, next_y, current_cell.contain)
                        current_cell.remove_stone()
            # Up
        for dx in range(x - 1, -1, -1):
            current_cell = self.grid.grid[dx][y]
            if not current_cell.is_empty:
                next_x = dx + 1
                if next_x < self.grid.width:
                    next_cell = self.grid.grid[next_x][y]
                    if next_cell.is_empty:
                        self.grid.put_stone(next_x, y, current_cell.contain)
                        current_cell.remove_stone()

        for dx in range(x + 1, self.grid.width):
            current_cell = self.grid.grid[dx][y]
            if not current_cell.is_empty:
                next_x = dx - 1
                if next_x >= 0:
                    next_cell = self.grid.grid[next_x][y]
                    if next_cell.is_empty:
                        self.grid.put_stone(next_x, y, current_cell.contain)
                        current_cell.remove_stone()

    def check_win(self):
        for y in range(self.grid.width):
            for x in range(self.grid.width):
                cell = self.grid.grid[x][y]
                if (cell.cell_type =="gCell") and cell.is_empty:
                    return False
        return True

    def check_lose(self):
        if self.grid.moves <= 0:
            return True
        else:
            return False

    def play(self):
        while self.grid.moves > 0 and not self.check_win():
            try:
                self.grid.display_grid()
                magnets = self.get_all_magnets()
                if not magnets:
                    print("There are no magnets.")
                    return
                print("Available Magnets:")
                for index, (cell, x, y) in enumerate(magnets):
                    magnet_type = cell.contain.s_Type
                    print(f"{index + 1}. Magnet at ({x}, {y}), type: {magnet_type}")
                magnet_choice = int(input("Enter the number of the magnet you want to move: ")) - 1
                if magnet_choice < 0 or magnet_choice >= len(magnets):
                    print("Invalid number. Try again.")
                    continue
                selected_magnet, current_x, current_y = magnets[magnet_choice]
                new_x = int(input("Enter the new X coordinate for the magnet: "))
                new_y = int(input("Enter the new Y coordinate for the magnet: "))
                # print(selected_magnet.contain.x)
                self.move_magnet(selected_magnet.contain, new_x, new_y)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_all_magnets(self):
        magnets = []
        for y in range(self.grid.width):
            for x in range(self.grid.width):
                cell = self.grid.grid[x][y]
                if cell.contain and cell.contain.s_Type in ["N", "S"]:
                    magnets.append((cell, x, y))
        return magnets

    def get_all_magnets_al(self):
        magnets = []
        for y in range(self.grid.width):
            for x in range(self.grid.width):
                cell = self.grid.grid[x][y]
                if cell.contain and cell.contain.s_Type in ["N", "S"]:
                    magnets.append((cell.contain, x, y))
        return magnets

