import sys
from model.graph import Graph
from model.graph_adj_matrix import GraphAdjMatrix
from model.abstract_graph import AbstractGraph
from dfs.topsort.topsort import top_sort
from bfs.grid_path_find import reconstruct_path
from dijktras.dijktras import dijktras
'''
    single source shortest path of an directed acyclic graph
'''
def sssp(graph: Graph) -> list[int]:
    distances: list[int] = [sys.maxsize] * len(graph)
    sorted_node: list[int] = top_sort(graph)
    prev: list[int] = [None] * len(graph)
    distances[sorted_node[0]] = 0
    for node in sorted_node:
        for neighbor in graph.get_adjacent_nodes(node):
            current_distance = distances[node] + graph.get_edge(node, neighbor)
            if distances[neighbor] > current_distance:
                distances[neighbor] = current_distance
                prev[neighbor] = node

    return distances, prev
'''
    single source longest path of a directed acyclic graph
'''
def sslp(graph: Graph) -> list[int]:
    distances: list[int] = [sys.maxsize] * len(graph)
    sorted_node: list[int] = top_sort(graph)
    prev: list[int] = [None] * len(graph)
    distances[sorted_node[0]] = 0
    for node in sorted_node:
        for neighbor in graph.get_adjacent_nodes(node):
            current_distance: int = distances[node] + (-1 * graph.get_edge(node, neighbor))
            if current_distance < distances[neighbor]:
                prev[neighbor] = node
                distances[neighbor] = current_distance
    return [-1 * d for d in distances], prev

def get_graph() -> Graph:
    graph: Graph = Graph(8, True)

    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 2, 6)

    graph.add_edge(1, 2, 4)
    graph.add_edge(1, 3, 4)
    graph.add_edge(1, 4, 11)

    graph.add_edge(2, 3, 8)
    graph.add_edge(2, 6, 11)

    graph.add_edge(3, 4, -4)
    graph.add_edge(3, 5, 5)
    graph.add_edge(3, 6, 2)

    graph.add_edge(4 ,7, 9)

    graph.add_edge(5, 7, 1)

    graph.add_edge(6, 7, 2)

    return graph

def get_graph_new() -> AbstractGraph:
    graph: AbstractGraph = GraphAdjMatrix(8, True)

    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 2, 6)

    graph.add_edge(1, 2, 4)
    graph.add_edge(1, 3, 4)
    graph.add_edge(1, 4, 11)

    graph.add_edge(2, 3, 8)
    graph.add_edge(2, 6, 11)

    graph.add_edge(3, 4, -4)
    graph.add_edge(3, 5, 5)
    graph.add_edge(3, 6, 2)

    graph.add_edge(4 ,7, 9)

    graph.add_edge(5, 7, 1)

    graph.add_edge(6, 7, 2)

    return graph

def sssp_main():
    print("_________________________________________________________")
    print("SSSP")
    node_label: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    graph: Graph = get_graph()

    distances, prev = sssp(graph)
    for i in range(len(distances)):
        print(f'{node_label[i]} -> {distances[i]}')
    
    print_traversed_paths(prev, node_label)

def sslp_main():
    node_label: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    graph: Graph = get_graph()

    distances, prev = sslp(graph)
    for i in range(len(distances)):
        print(f'{node_label[i]} -> {distances[i]}')
    
    print_traversed_paths(prev, node_label)


def dijktras_main():
    print("_________________________________________________________")
    print("Dijkstras")
    node_label: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    graph: Graph = get_graph()

    distances, prev = dijktras(graph, 0)
    for i in range(len(distances)):
        print(f'{node_label[i]} -> {distances[i]}')
    
    print_traversed_paths(prev, node_label)

def print_traversed_paths(prev_path: list[int], label: list[str] = None) -> None:
    traversed_paths: list[list[int]] = paths(prev_path)
    for trav_path in traversed_paths:
        path_str: str = ''
        for p in trav_path:
            if label is not None:
                path_str += f'{label[p]} -> '
            else:
                path_str += f'{p} -> '
        print(path_str)

def paths(prev_path: list[int]) -> list[list[int]]:
    traversed_paths: list[list[int]] = []
    for i in range(len(prev_path)):
        trav_path: list[int] = reconstruct_path(0, i, prev_path)
        traversed_paths.append(trav_path)
    return traversed_paths

def test_graph_main():
    graph_adj_mat_old: Graph = get_graph()
    graph_adj_mat_new: AbstractGraph = get_graph_new()

    for node in range(len(graph_adj_mat_old)):
        print(f'neighbors of node: {node}')
        print(f'new: {graph_adj_mat_new.get_neighbors(node)}')
        print(f'old: {graph_adj_mat_old.get_adjacent_nodes(node)}')
        print("-------------------------------------")
    node: int = 3
    print(f'neigbor cost of node: {node}')
    for neighbor in graph_adj_mat_new.get_neighbors(node):
        print(f'new: {node} -> {neighbor} = {graph_adj_mat_new.get_edge_cost(node, neighbor)}')
        print(f'old: {node} -> {neighbor} = {graph_adj_mat_old.get_edge(node, neighbor)}')