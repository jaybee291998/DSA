import collections

class Graph:
    def __init__(self, size):
        self.size = size
        self.adjacency_matrix = [0] * (size * size)
    
    def __set_edge(self, node_one, node_two, value):
        assert node_one < self.size and node_two < self.size
        index_one = self.__calulate_index(node_one, node_two)
        index_two = self.__calulate_index(node_two, node_one)
        self.adjacency_matrix[index_one] = value
        self.adjacency_matrix[index_two] = value
    
    def add_edge(self, node_one, node_two):
        self.__set_edge(node_one, node_two, 1)
    
    def remove_edge(self, node_one, node_two):
        pass

    def get_edge(self, node_one, node_two):
        index = self.__calulate_index(node_one, node_two)
        return self.adjacency_matrix[index]

    def is_edge_present(self, node_one, node_two):
        return self.get_edge(node_one, node_two) == 1
    
    def get_adjacent_nodes(self, node):
        return [i for i in range(self.size) if self.is_edge_present(node, i)]

    def __calulate_index(self, node_one, node_two):
        return node_one * self.size + node_two
    
    def __len__(self):
        return self.size

def bfs(graph: Graph, node: int):
    dq = collections.deque([node])
    visited = [False] * len(graph)
    prev = [None] * len(graph)
    visited[node] = True
    while len(dq) > 0:
        current_node = dq.popleft()
        print(current_node)
        for next_node in graph.get_adjacent_nodes(current_node):
            if not visited[next_node]:
                dq.append(next_node)
                visited[next_node] = True
                prev[next_node] = current_node
    return prev

def least_node(graph: Graph, start_node: int, end_node: int) -> list[int]: 
    paths: list[int] = bfs(graph, start_node)
    return reconstruct_path(start_node, end_node, paths)


def reconstruct_path(start_node: int, end_node: int, path: list[int]) -> list[int]:
    traversed_path: list[int] = []
    current_node: int = end_node
    count = 0
    while current_node >= start_node:
        traversed_path.append(current_node)
        if current_node >= len(path) or current_node < 0:
            break
        current_node = path[current_node]
        if current_node is None:
            break
        count += 1
        # prevent infinite loop
        if count > len(path):
            break
    traversed_path.reverse()
    return traversed_path


if __name__ == '__main__':
    number_of_nodes = 9
    graph = Graph(number_of_nodes)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)

    graph.add_edge(1, 3)
    graph.add_edge(1, 6)

    graph.add_edge(6, 4)

    graph.add_edge(3, 4)
    graph.add_edge(3, 5)

    graph.add_edge(7, 7)

    graph.add_edge(8, 8)

    # additional node connecting 4 -> 5
    graph.add_edge(4, 5)

    # print(bfs(graph, 0))
    print(least_node(graph, 0, 5))