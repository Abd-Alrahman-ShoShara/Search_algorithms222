from networkx.classes import Graph

class Graph:
    def __init__(self, game):
        self.value = game
        self.children = []
        self.parent = None
        self.visited = False
        self.cost=0

    def __lt__(self, other):

        return self.cost < other.cost

    def add_child(self, child_node):
        if child_node not in self.children:
            self.children.append(child_node)
            child_node.parent = self

    # def create_graph1(self):
    #     magnets = self.value.get_all_magnets_al()
    #     if not magnets:
    #         return
    #     for magnet, current_x, current_y in magnets:
    #         for i in range(self.value.width):
    #             for j in range(self.value.width):
    #                 if self.value.grid[i][j].is_empty and self.value.grid[i][j].cell_type != "bCell":
    #                     # Use move_stone_for_al to generate new state
    #                     new_state = self.value.move_stone_for_al(current_x, current_y, i, j)
    #                     if new_state is not None:
    #                         child_node = Graph(new_state)
    #                         self.add_child(child_node)
    #                         child_node.create_graph()
    #     return self

    def create_graph(self):
        if self.value.grid.moves == 0:
            return
        magnets = self.value.get_all_magnets_al()
        if not magnets:
            return
        for magnet, current_x, current_y in magnets:
            for i in range(self.value.grid.width):
                for j in range(self.value.grid.width):
                    if self.value.grid.grid[i][j].is_empty and self.value.grid.grid[i][j].cell_type != "bCell":
                        new_state = self.value.move_stone_for_al(current_x, current_y, i, j)
                        if new_state is not None:

                            child_node = Graph(new_state)
                            self.add_child(child_node)
                            child_node.create_graph()

