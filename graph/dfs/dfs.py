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
    
def dfs(graph, node, visited=None):
  if visited is None:
      visited = [False] * len(graph)
  if visited[node]:
      return
  visited[node] = True
  print(node)
  for adjacent_node in graph.get_adjacent_nodes(node):
      dfs(graph, adjacent_node, visited)

# visited_nodes = [False] * number_of_nodes
if __name__ == '__main__':
    number_of_nodes = 7
    graph = Graph(number_of_nodes)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)

    graph.add_edge(1, 3)
    graph.add_edge(1, 6)

    graph.add_edge(6, 4)

    graph.add_edge(3, 4)
    graph.add_edge(3, 5)

    dfs(graph, 0)