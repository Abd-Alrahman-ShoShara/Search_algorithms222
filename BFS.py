from Graph import Graph
from collections import deque  # For queue

class BFS:
    def __init__(self, game):
        self.game = game

    def start(self):

        initial_graph_node = Graph(self.game)
        initial_graph_node.create_graph()
        solution_node = BFS.bfs(initial_graph_node)

        if solution_node is not None:
            queue = []
            queue.append(solution_node)

            while queue[-1].parent is not None:
                queue.append(queue[-1].parent)

            print("Solution:\n")
            while queue:
                top_element = queue[-1]
                queue.pop().value.display_game()
                print("\n")
        else:
            print("No solution found")

    @staticmethod
    def bfs(node: Graph):
        queue = deque([node])
        visited = set()

        visited.add(node)

        while queue:
            current_node = queue.popleft()
            if current_node.value.check_win():
                return current_node
            for child in current_node.children:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
        return None
