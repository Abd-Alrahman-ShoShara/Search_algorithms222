from Graph import Graph


class DFS:
    def __init__(self, game):
        self.game = game

    def start(self):

        initial_graph_node = Graph(self.game)
        initial_graph_node.create_graph()
        solution_node = DFS.dfs(initial_graph_node)

        if solution_node is not None:
            stack = []
            stack.append(solution_node)

            while stack[-1].parent is not None:
                stack.append(stack[-1].parent)

            print("Solution:\n")
            while stack:
                top_element = stack[-1]
                stack.pop().value.display_game()
                print("\n")
        else:
            print("No solution found")
    @staticmethod
    def dfs(node: Graph):
        stack = [node]
        visited = set()
        visited.add(node)

        while stack:
            node = stack.pop()
            if node.value.check_win():
                return node

            for child in node.children:
                if child not in visited:
                    stack.append(child)
                    visited.add(child)
                    if child.value.check_win():
                        return child
