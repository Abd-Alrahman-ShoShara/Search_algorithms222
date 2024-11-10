from collections import deque
import copy

from Stone import Stone

class Solver:
    def __init__(self, game):
        self.game = game
        self.initial_state = copy.deepcopy(game.grid)
        self.moves = []

    def BFS(self):

        queue = deque([(self, [])])
        visited = set()
        solved = False

        while queue:
            if solved:
                break
            current_board, path = queue.popleft()

            if current_board.game.check_win():
                if not solved:
                    solved = True
                    print("\nthe game was solved :")
                    print("the moves need :")
                    for move in path:
                        print(f"From {move[0]} to {move[1]}")

                    print("\nthe grid States :")

                    solution_board = self
                    solution_board.game.display_game()
                    print("//////////////////////////////////////////////////////////////////////////////")

                    for move in path:
                        x, y = move[0]
                        new_x, new_y = move[1]
                        solution_board.game.move_stone_for_al(x, y, new_x, new_y)
                        solution_board.game.display_game()
                        print("//////////////////////////////////////////////////////////////////////////////")

                break

            serialized_state = tuple(
                tuple(cell.contain.s_Type if cell.contain else None for cell in row) for row in current_board.game.grid.grid
            )

            if serialized_state in visited:
                continue

            visited.add(serialized_state)

            for x in range(current_board.game.width):
                for y in range(current_board.game.width):
                    cell = current_board.game.grid.grid[x][y]

                    if cell.contain and cell.contain.m_Type in ["N", "S"]:
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < current_board.game.width and 0 <= new_y < current_board.game.width:

                                new_board = copy.deepcopy(current_board)
                                new_board.game.move_stone_for_al(x, y, new_x, new_y)

                                new_serialized_state = tuple(
                                    tuple(cell.contain.s_Type if cell.contain else None for cell in row) for row in
                                    new_board.game.grid.grid
                                )

                                if new_serialized_state not in visited:
                                    queue.append((new_board, path + [((x, y), (new_x, new_y))]))

        if not solved:
            print("No solution .")



    # def DFS(self):
    #     stack = [self.game]
    #     visited=set()
    #     game=self.game
    #     visited.add(game)
    #     return self.complete(visited,stack)
    #
    # def complete(self,visited, stack):
    #     if self.game.grid.moves == 0:
    #         return
    #     print(self.game.grid.moves)
    #     game=stack.pop()
    #     game.grid.display_grid()
    #     if game.check_win():
    #         return game
    #
    #     for i in range(game.grid.width):
    #         for j in range(game.grid.width):
    #             the_magnet=game.grid.get_mag()
    #             print(the_magnet)
    #             current_game=game.move_magnet(the_magnet,i,j)
    #             print(current_game)
    #             if not current_game in visited:
    #                 visited.add(current_game)
    #                 stack.append(current_game)
    #                 if current_game.check_win():
    #                     return current_game
    #
    #     return self.complete(visited,stack)
    #

    def DFS(self):

        stack = [(self, [])]
        visited = set()
        solved = False

        while stack:
            if solved:
                break

            current_board, path = stack.pop()
            if current_board.game.check_win():
                if not solved:
                    solved = True
                    print("\nthe game was solved :")
                    print("the moves need :")
                    for move in path:
                        print(f"From {move[0]} to {move[1]}")
                    print("\nthe grid States :")
                    solution_board = self
                    solution_board.game.display_game()
                    print("///////////////////////////////////////////////////////////////////////////////////")
                    for move in path:
                        x, y = move[0]
                        new_x, new_y = move[1]
                        solution_board.game.move_stone_for_al(x, y, new_x, new_y)
                        solution_board.game.display_game()
                        print("///////////////////////////////////////////////////////////////////////////////////")
                break
            serialized_state = tuple(
                            tuple(cell.contain.s_Type if cell.contain else None for cell in row) for row in current_board.game.grid.grid
                        )
            if serialized_state in visited:
                continue
            visited.add(serialized_state)
            for x in range(current_board.game.width):
                for y in range(current_board.game.width):
                    cell = current_board.game.grid.grid[x][y]
                    if cell.contain and cell.contain.m_Type in ["N", "S"]:
                         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                             new_x, new_y = x + dx, y + dy
                             if 0 <= new_x < current_board.game.width and 0 <= new_y < current_board.game.width:
                                new_board = copy.deepcopy(current_board)
                                new_board.game.move_stone_for_al(x, y, new_x, new_y)
                                new_serialized_state = tuple(
                                    tuple(cell.contain.s_Type if cell.contain else None for cell in row) for row in new_board.game.grid.grid
                                )
                                if new_serialized_state not in visited:
                                    stack.append((new_board, path + [((x, y), (new_x, new_y))]))
        if not solved:
            print("No solution .")

