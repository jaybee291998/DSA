class Graph:
    def __init__(self, size, directed: bool = False):
        self.size = size
        self.is_directed = directed
        self.adjacency_matrix = [None] * (size * size)
    
    def __set_edge(self, node_one, node_two, value):
        assert node_one < self.size and node_two < self.size
        index_one = self.__calulate_index(node_one, node_two)
        self.adjacency_matrix[index_one] = value
        if not self.is_directed:
            index_two = self.__calulate_index(node_two, node_one)
            self.adjacency_matrix[index_two] = value
    
    def add_edge(self, node_one, node_two, value: int = 1):
        self.__set_edge(node_one, node_two, value)
    
    def remove_edge(self, node_one, node_two):
        pass

    def get_edge(self, node_one, node_two):
        if node_one == node_two:
            return 0
        index = self.__calulate_index(node_one, node_two)
        return self.adjacency_matrix[index]

    def is_edge_present(self, node_one, node_two):
        return self.get_edge(node_one, node_two) is not None
    
    def get_adjacent_nodes(self, node: int) -> list[int]:
        return [i for i in range(self.size) if self.is_edge_present(node, i) and i != node]

    def __calulate_index(self, node_one, node_two):
        return node_one * self.size + node_two
    
    def __len__(self):
        return self.size