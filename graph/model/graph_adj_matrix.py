from model.abstract_graph import AbstractGraph, Edge

class GraphAdjMatrix(AbstractGraph):
    def __init__(self, number_of_vertices: int, is_directed: bool = False):
        self.is_directed = is_directed
        self.adjacency_matrix = [None] * (number_of_vertices * number_of_vertices)
        self.number_of_vertices = number_of_vertices

    def add_edge(self, from_node: int, to_node: int, cost: int) -> None:
        self.__set_edge(from_node, to_node, cost)

    def get_neighbors(self, node: int) -> list[int]:
        return [i for i in range(self.number_of_vertices) if self.__is_edge_present(node, i) and node != i]

    def get_number_of_vertices(self) -> int:
        return self.number_of_vertices

    def get_edge_list(self) -> list[Edge]:
        edges: list[Edge] = []
        for x in range(self.number_of_vertices):
            for y in range(self.number_of_vertices):
                if self.__is_edge_present(x, y):
                    edges.append(Edge(x, y, self.get_edge_cost(x, y)))
        return edges

    def get_edge_cost(self, from_node: int, to_node: int) -> int:
        if from_node == to_node:
            return 0
        index = self.__calulate_index(from_node, to_node)
        return self.adjacency_matrix[index]

    def __set_edge(self, node_one: int, node_two: int, value: int) -> None:
        assert node_one < self.number_of_vertices and node_two < self.number_of_vertices
        index_one = self.__calulate_index(node_one, node_two)
        self.adjacency_matrix[index_one] = value
        if not self.is_directed:
            index_two = self.__calulate_index(node_two, node_one)
            self.adjacency_matrix[index_two] = value

    def __calulate_index(self, node_one, node_two):
        return node_one * self.number_of_vertices + node_two
    
    def __is_edge_present(self, node_one, node_two):
        return self.get_edge_cost(node_one, node_two) is not None