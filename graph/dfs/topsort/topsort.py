from model.graph import Graph

def top_sort(graph: Graph) -> list[int]:
    sorted_list = []
    visited: list[bool] = [False] * len(graph)
    for i in range(len(graph)):
        dfs(graph, i, sorted_list, visited)
    sorted_list.reverse()
    return sorted_list

def dfs(graph: Graph, node: int, sorted_list: list[int], visited: list[bool]):
    if visited[node]:
        return
    visited[node] = True
    for neighbor_node in graph.get_adjacent_nodes(node):
        if not visited[neighbor_node]:
            dfs(graph, neighbor_node, sorted_list, visited)
    sorted_list.append(node)

def top_sort_main():
    subjects: list[str] = [
        'arithmetic',
        'pre algebra',
        'alegebra',
        'geometry',
        'trigonometry',
        'plane trig',
        'spherical trig',
        'advanced trig',
        'pre-calc',
        'cal1',
        'calc2',
        'calc3',
        'dfe',
        'pde'
    ]
    graph: Graph = Graph(13, True)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 8)
    graph.add_edge(8, 9)
    graph.add_edge(2, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)
    graph.add_edge(7, 12)
    graph.add_edge(9, 10)
    graph.add_edge(10, 11)
    graph.add_edge(11, 12)

    sorted_list: list[int] = top_sort(graph)

    print([subjects[i] for i in sorted_list])