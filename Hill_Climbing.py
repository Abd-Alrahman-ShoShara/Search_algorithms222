from Graph import Graph
class HillClimbing:
    def __init__(self, game):
        self.game = game

    def start(self):
        initial_graph_node = Graph(self.game)
        initial_graph_node.create_graph()
        solution_node = HillClimbing.hill_climb(initial_graph_node)

        if solution_node is not None:
            print("Solution found:\n")
            solution_node.value.display_game()
        else:
            print("No solution found")

    @staticmethod
    def hill_climb(node: Graph):
        current_node = node
        while True:
            neighbors = current_node.children
            if not neighbors:
                return None
            best_neighbor = None
            for child in neighbors:
                if child.value.check_win():
                    return child
                if best_neighbor is None or HillClimbing.heuristic(child) < HillClimbing.heuristic(best_neighbor):
                    best_neighbor = child
            if HillClimbing.heuristic(best_neighbor) >= HillClimbing.heuristic(current_node):
                return None
            current_node = best_neighbor

    @staticmethod
    def heuristic(node: Graph):
        he = 0
        for x in range(node.value.grid.width):
            for y in range(node.value.grid.width):
                current = node.value.grid.grid[x][y]
                if current.contain in ["N", "S", "iron"]:
                    min_dist = float('inf')
                    for ix in range(node.value.grid.width):
                        for iy in range(node.value.grid.width):
                            current2 = node.value.grid.grid[ix][iy]
                            if current2.cell_type == "gCell":
                                dist = abs(x - ix) + abs(y - iy)
                                min_dist = min(min_dist, dist)
                    he += min_dist

        return he
