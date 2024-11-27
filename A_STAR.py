import heapq
from Graph import Graph

class AStar:
    def __init__(self, game):
        self.game = game

    def start(self):
        initial_graph_node = Graph(self.game)
        initial_graph_node.create_graph()
        solution_node = AStar.a_star_search(initial_graph_node)

        if solution_node is not None:

            path = []
            while solution_node is not None:
                path.append(solution_node)
                solution_node = solution_node.parent


            path.reverse()
            print("Solution found:\n")
            for node in path:
                node.value.display_game()
                print("\n")
        else:
            print("No solution found")

    @staticmethod
    def a_star_search(start_node: Graph):

        open_list = []
        heapq.heappush(open_list, (0, start_node))
        closed_list = set()

        while open_list:
            _, current_node = heapq.heappop(open_list)
            if current_node.value.check_win():
                return current_node

            closed_list.add(current_node)

            for child in current_node.children:
                if child in closed_list:
                    continue
                g = current_node.cost + 1
                h = AStar.heuristic(child)


                f = g + h

                if child not in [node[1] for node in open_list]:
                    heapq.heappush(open_list, (f, child))
                    child.cost = g
                    child.parent = current_node
                else:

                    for index, (score, node) in enumerate(open_list):
                        if node == child and g < node.cost:
                            open_list[index] = (f, child)
                            heapq.heapify(open_list)
                            child.cost = g
                            child.parent = current_node
                            break

        return None

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
                                # print(dist)
                                min_dist = min(min_dist, dist)
                    he += min_dist

        return he

