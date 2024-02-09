from model.abstract_graph import AbstractGraph, Edge

class GraphAdjList(AbstractGraph):
    def __init__(self):
        pass

    def add_edge(self, from_node: int, to_node: int, cost: int) -> None:
        pass

    def get_neighbors(self, node: int) -> list[tuple]:
        pass

    def get_number_of_vertices(self) -> int:
        pass

    def get_edge_list(self) -> list[Edge]:
        pass