import heapq  # For priority queue (min-heap)
from Graph import Graph

class UCS:
    def __init__(self, game):
        self.game = game

    def start(self):
        initial_graph_node = Graph(self.game)
        initial_graph_node.create_graph()

        solution_node = UCS.ucs(initial_graph_node)

        if solution_node is not None:
            path = []
            path.append(solution_node)

            while path[-1].parent is not None:
                path.append(path[-1].parent)

            print("Solution (with costs):\n")
            while path:
                top_element = path[-1]
                path.pop()
                top_element.value.display_game()
                print(f"Cost to reach this state: {top_element.cost}")
                print("\n")
        else:
            print("No solution found")

    @staticmethod
    def ucs(node: Graph):
        priority_queue = []
        heapq.heappush(priority_queue, node)
        visited = set()

        visited.add(node)

        while priority_queue:
            #here we take the lowest board cost
            current_node = heapq.heappop(priority_queue)

            if current_node.value.check_win():
                return current_node
            for child in current_node.children:
                if child not in visited:
                    visited.add(child)
                    child.cost = current_node.cost + 1
                    heapq.heappush(priority_queue, child)

        return None
