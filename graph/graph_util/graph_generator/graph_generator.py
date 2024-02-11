import random
from model.abstract_graph import AbstractGraph
from model.graph_adj_matrix import GraphAdjMatrix
from graph_util.graph_writer.graph_writer import write_graph

def generate_graph(graph: AbstractGraph, min_number_of_edge_per_node: int, max_number_of_edge_per_node: int) -> None:
    nodes: list[int] = [i for i in range(graph.get_number_of_vertices())]
    for node in nodes:
        number_of_edges: int = random.randint(min_number_of_edge_per_node, max_number_of_edge_per_node)
        for i in range(number_of_edges):
            chosen_node: int = random.choice(nodes)
            if node == chosen_node:
                continue
            graph.add_edge(node, chosen_node, random.randint(-100, 100))

def test_graph_generator_main():
    graph: AbstractGraph = GraphAdjMatrix(10, True)
    generate_graph(graph, 3, 7)
    write_graph("graph.csv", graph)
    for i in range(graph.get_number_of_vertices()):
        print(f'{i}: {graph.get_neighbors(i)}')