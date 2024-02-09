import sys

class Edge:
    def __init__(self, start: int, destination: int, cost: int):
        self.start = start
        self.destination = destination
        self.cost = cost

class Graph:
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self._edges: list[Edge] = []
    
    def add_edge(self, start: int, destination: int, cost: int):
        assert start < self.number_of_vertices
        assert destination < self.number_of_vertices
        self._edges.append(Edge(start, destination, cost))
    
    def get_edges(self) -> list[Edge]:
        return self._edges


def bellmanford(start_node: int, graph: Graph) -> tuple:
    distances: list[int] = [float('inf')] * graph.number_of_vertices
    prev: list[int] = [None] * graph.number_of_vertices
    distances[start_node] = 0
    for _ in range(graph.number_of_vertices - 1):
        for edge in graph.get_edges():
            if distances[edge.start] != float('inf') and (distances[edge.start] + edge.cost) < distances[edge.destination]:
                distances[edge.destination] = distances[edge.start] + edge.cost
                prev[edge.destination] = edge.start
    
    for _ in range(graph.number_of_vertices):
        for edge in graph.get_edges():
            if distances[edge.start] != float('inf') and (distances[edge.start] == float('-inf') or (distances[edge.start] + edge.cost) < distances[edge.destination]):
                distances[edge.destination] = float('-inf')
    
    return distances, prev


def bellmanford_main():
    g = Graph(5)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)

    g.add_edge(1, 3, 2)
    g.add_edge(1, 2, -3)
    g.add_edge(1, 4, 3)

    g.add_edge(2, 1, 1)
    g.add_edge(2, 3, 4)
    g.add_edge(2, 4, 5)

    g.add_edge(4, 3, -5)
    distances, prev = bellmanford(0, g)
    print(distances)
    print(prev)