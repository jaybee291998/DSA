from abc import ABC, abstractmethod

class Edge:
    def __init__(self, start: int, destination: int, cost: int):
        self.start = start
        self.destination = destination
        self.cost = cost

class AbstractGraph(ABC):
    @abstractmethod
    def add_edge(self, from_node: int, to_node: int, cost: int) -> None:
        pass

    @abstractmethod
    def get_neighbors(self, node: int) -> list[int]:
        pass

    @abstractmethod
    def get_edge_cost(self, from_node: int, to_node: int) -> int:
        pass

    @abstractmethod
    def get_number_of_vertices(self) -> int:
        pass

    @abstractmethod
    def get_edge_list(self) -> list[Edge]:
        pass

