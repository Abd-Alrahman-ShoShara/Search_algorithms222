from Grid import Grid
import copy
from Stone import Stone
class Game:
    def __init__(self,width,moves,level):
        self.width=width
        self.moves = moves
        self.moves_done=[]
        self.level = level
        self.grid=Grid(width,moves)

    def display_game(self):
        print(f"Game Level {self.level} - Grid size: {self.width}x{self.width}, Moves allowed: {self.moves}")
        self.grid.display_grid()

    def move_stone_for_al(self, from_x, from_y, to_x, to_y):

        if not (0 <= from_x < self.width and 0 <= from_y < self.width):
            print("Invalid source cell coordinates")
            return
        if not (0 <= to_x < self.width and 0 <= to_y < self.width):
            print("Invalid destination cell coordinates")
            return

        from_cell = self.grid.grid[from_x][from_y]
        to_cell = self.grid.grid[to_x][to_y]

        if from_cell.empty or from_cell.contain.s_Type not in ["magnet"]:
            print("Only magnets can be moved.")
            return

        if not to_cell.empty and to_cell.name != ["nCell","gCell"]:
            # print()
            print("cell is not empty or blocked")
            return

        stone = from_cell.contain
        to_cell.put_stone(stone)
        from_cell.remove_stone()

        self.moves_done.append(((from_x, from_y), (to_x, to_y)))

        if stone.m_Type == "N":
            self.move_stones_around_for_n(to_x, to_y)

        if stone.m_Type == "S":
            self.move_stones_around_for_s(to_x, to_y)

    def move_magnet(self, magnet, new_x, new_y):
        # self=copy.deepcopy(self)
        if not (0 <= new_x < self.width and 0 <= new_y < self.width):
            print("New position is out of grid bounds.")
            return False

        current_x, current_y = None, None
        for i in range(self.width):
            for j in range(self.width):
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

        if (target_cell.name == "nCell" or target_cell.name == "gCell") and target_cell.is_empty():
            self.grid.put_stone(new_x, new_y, magnet)
            self.grid.grid[current_x][current_y].remove_stone()
            self.grid.moves -= 1

            if magnet.m_Type == "N":
                self.move_stones_around_for_n( new_x , new_y)
            else:
                self.move_stones_around_for_s(new_x , new_y)
        
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



    def move_stones_around_for_n1(self,x,y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            stones_to_move = []

            while 0 <= nx < self.width and 0 <= ny < self.width:
                neighbor_cell = self.grid.grid[nx][ny]

                if neighbor_cell.contain and neighbor_cell.contain.s_Type in ["iron", "magnet"]:
                    stones_to_move.append((nx, ny))
                elif neighbor_cell.is_empty():
                    stones_to_move.append((nx, ny))
                else:
                    break

                nx += dx
                ny += dy

            for i in range(len(stones_to_move) - 1, 0, -1):
                src_x, src_y = stones_to_move[i - 1]
                dest_x, dest_y = stones_to_move[i]

                if self.grid.grid[dest_x][dest_y].is_empty():
                    stone_to_move = self.grid.grid[src_x][src_y].contain
                    self.grid.grid[dest_x][dest_y].put_stone(stone_to_move)
                    self.grid.grid[src_x][src_y].remove_stone()


    def move_stones_around_for_s(self,x,y):

        # right
        for dy in range(y + 1, self.grid.width):
            current_cell = self.grid.grid[x][dy]
            if not current_cell.is_empty():
                next_y = dy -1

                if next_y >=0:
                    next_cell = self.grid.grid[x][next_y]
                    if next_cell.is_empty():
                        self.grid.put_stone(x,next_y,current_cell.contain)
                        current_cell.remove_stone()

        for dy in range(y - 1, -1, -1):
            current_cell = self.grid.grid[x][dy]
            if not current_cell.is_empty():
                next_y = dy + 1
                if next_y < self.grid.width:
                    next_cell = self.grid.grid[x][next_y]
                    if next_cell.is_empty():
                        self.grid.put_stone(x, next_y, current_cell.contain)
                        current_cell.remove_stone()

            # Up
        for dx in range(x - 1, -1, -1):
            current_cell = self.grid.grid[dx][y]
            if not current_cell.is_empty():
                next_x = dx + 1
                if next_x < self.grid.width:
                    next_cell = self.grid.grid[next_x][y]
                    if next_cell.is_empty():
                        self.grid.put_stone(next_x, y, current_cell.contain)
                        current_cell.remove_stone()

            # Down
        for dx in range(x + 1, self.grid.width):
            current_cell = self.grid.grid[dx][y]
            if not current_cell.is_empty():
                next_x = dx - 1
                if next_x >= 0:
                    next_cell = self.grid.grid[next_x][y]
                    if next_cell.is_empty():
                        self.grid.put_stone(next_x, y, current_cell.contain)
                        current_cell.remove_stone()

    # def move_magnet_for_solver(self, magnet, new_x, new_y):
    #     if not (0 <= new_x < self.width and 0 <= new_y < self.width):
    #         return False  # New position is out of grid bounds.
    #
    #     current_x, current_y = None, None
    #     for i in range(self.width):
    #         for j in range(self.width):
    #             cell = self.grid.grid[i][j]
    #             if cell.contain == magnet:
    #                 current_x, current_y = i, j
    #                 break
    #         if current_x is not None:
    #             break
    #
    #     if current_x is None or current_y is None:
    #         return False  # Magnet not found on the grid.
    #
    #     target_cell = self.grid.grid[new_x][new_y]
    #
    #     # Check if the target cell is a valid target (empty or goal)
    #     if (target_cell.name == "nCell" or target_cell.name == "gCell") and target_cell.is_empty():
    #         # Move magnet to the new position
    #         self.grid.put_stone(new_x, new_y, magnet)
    #         self.grid.grid[current_x][current_y].remove_stone()
    #
    #         # Move stones around if necessary
    #         if magnet.m_Type == "N":
    #             self.move_stones_around_for_n(new_x, new_y)
    #         else:
    #             self.move_stones_around_for_s(new_x, new_y)
    #
    #         return True
    #     else:
    #         return False  # Target cell is not empty or is blocked.
    #
    def check_win(self):
        for y in range(self.grid.width):
            for x in range(self.grid.width):
                cell = self.grid.grid[x][y]
                if (cell.name =="gCell") and cell.is_empty():
                    return False
        return True

    def check_win1(self):
        for i in range(self.width):
            for j in range(self.width):
                cell = self.grid.grid[i][j]
                if cell.name == "gCell" and not cell.is_empty():
                        return True
        return False

    def check_lose(self):
        if self.grid.moves <= 0:
            return True
        else:
            return False


    def get_all_magnets(self):
        magnets = []
        for y in range(self.grid.width):
            for x in range(self.grid.width):
                cell = self.grid.grid[x][y]
                if cell.contain and cell.contain.s_Type == "magnet":
                    magnets.append((cell, x, y))  # Store cell with its coordinates
        return magnets

    def play(self):
        while self.moves > 0 and not self.check_win():
            try:
                self.grid.display_grid()

                magnets = self.get_all_magnets()
                if not magnets:
                    print("There are no magnets.")
                    return

                print("Available Magnets:")
                for index, (cell, x, y) in enumerate(magnets):
                    magnet_type = cell.contain.m_Type  # Access the magnet's type
                    print(f"{index + 1}. Magnet at ({x}, {y}), type: {magnet_type}")

                magnet_choice = int(input("Enter the number of the magnet you want to move: ")) - 1
                if magnet_choice < 0 or magnet_choice >= len(magnets):
                    print("Invalid number. Try again.")
                    continue

                selected_magnet, current_x, current_y = magnets[magnet_choice]
                new_x = int(input("Enter the new X coordinate for the magnet: "))
                new_y = int(input("Enter the new Y coordinate for the magnet: "))
                self.move_magnet(selected_magnet.contain, new_x, new_y)

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def move_magnet_dfs(self, from_x, from_y, to_x, to_y):
        moves=[]
        if not (0 <= from_x < self.width and 0 <= from_y < self.width):
            print("Invalid source cell coordinates")
            return False
        if not (0 <= to_x < self.width and 0 <= to_y < self.width):
            print("Invalid destination cell coordinates")
            return False

        from_cell = self.grid.grid[from_x][from_y]
        to_cell = self.grid.grid[to_x][to_y]

        if from_cell.is_empty() or from_cell.contain.s_Type not in ["magnet"]:
            print("Only magnets can be moved.")
            return False

        if not to_cell.is_empty() and to_cell.name != "gCell":
            print("Destination cell is either occupied or blocked")
            return False

        stone = from_cell.contain
        if to_cell.put_stone(stone):
            from_cell.remove_stone()

            if stone.m_Type == "N":
                self.move_stones_around_for_n(to_x, to_y)

            elif stone.m_Type == "S":
                self.move_stones_around_for_s(to_x, to_y)

            moves.append(((from_x, from_y), (to_x, to_y)))  # Ensure this is a list

            if self.check_win():
                print("You won the level!")
                print("Moves you made:")
                for move in moves:
                    print(f"From {move[0]} to {move[1]}")
            return True
        else:
            print("Failed to move the stone.")
            return False




            # def ree(self, x, y):
    #     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #
    #     for dx, dy in directions:
    #         nx, ny = x + dx, y + dy
    #         stones_to_move = []
    #
    #         while 0 <= nx < self.width and 0 <= ny < self.width:
    #             neighbor_cell = self.grid.grid[nx][ny]
    #
    #             if neighbor_cell.contain and neighbor_cell.contain.s_Type in ["iron", "magnet"]:
    #                 stones_to_move.append((nx, ny))
    #             elif neighbor_cell.is_empty():
    #                 stones_to_move.append((nx, ny))
    #             else:
    #                 break
    #
    #             nx += dx
    #             ny += dy
    #
    #         for i in range(len(stones_to_move) - 1, 0, -1):
    #             src_x, src_y = stones_to_move[i - 1]
    #             dest_x, dest_y = stones_to_move[i]
    #
    #             if self.grid.grid[dest_x][dest_y].is_empty():
    #                 stone_to_move = self.grid.grid[src_x][src_y].contain
    #                 self.grid.grid[dest_x][dest_y].put_stone(stone_to_move)
    #                 self.grid.grid[src_x][src_y].remove_stone()



    def move_stones_around_for_n(self , x , y):
        directions = [
            (1, 0),  # down
            (-1, 0),  # up
            (0, 1),  # right
            (0, -1)  # left
        ]

        for dx, dy in directions:
            current_x, current_y = x + dx, y + dy
            if 0 <= current_x < self.grid.width and 0 <= current_y < self.grid.width:
                current_cell = self.grid.grid[current_x][current_y]

                if not current_cell.is_empty():
                    next_x, next_y = current_x + dx, current_y + dy
                    while 0 <= next_x < self.grid.width and 0 <= next_y < self.grid.width:
                        target_cell = self.grid.grid[next_x][next_y]

                        if target_cell.is_empty():
                            self.grid.put_stone(next_x, next_y, current_cell.contain)
                            current_cell.remove_stone()
                            break

                        elif not target_cell.is_empty():
                            next_next_x = next_x + dx
                            next_next_y = next_y + dy
                            if 0 <= next_next_x < self.grid.width and 0 <= next_next_y < self.grid.width:
                                next_target_cell = self.grid.grid[next_next_x][next_next_y]
                                if next_target_cell.is_empty():
                                    self.grid.put_stone(next_next_x, next_next_y, target_cell.contain)
                                    target_cell.remove_stone()

                                    self.grid.put_stone(next_x, next_y, current_cell.contain)
                                    current_cell.remove_stone()
                                    break
                            next_x += dx
                            next_y += dy

