from model.abstract_graph import AbstractGraph, Edge

def write_graph(file_path: str, graph: AbstractGraph) -> None:
    edges: list[Edge] = graph.get_edge_list()
    string: str = "from_node,to_node,cost\n"
    for edge in edges:
        string += edge_to_string(edge)
    with open(file_path, "w") as file:
        file.write(string)   

def edge_to_string(edge: Edge) -> str:
    return f"{edge.start},{edge.destination},{edge.cost}\n"