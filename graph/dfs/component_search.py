from dfs import Graph

def dfs(graph, node, current_group, visited, component):
  assert visited is not None and component is not None
  if visited[node]:
      return
  visited[node] = True
  component[node] = current_group
  for adjacent_node in graph.get_adjacent_nodes(node):
      dfs(graph, adjacent_node, current_group, visited, component)

def count_component(graph):
    n = len(graph)
    visited = [False] * n
    component = [-1] * n
    current_group = 0
    for i in range(n):
        if not visited[i]:
           current_group+=1
           dfs(graph, i, current_group, visited=visited, component=component)
    return (current_group, component)


if __name__ == '__main__':
    number_of_nodes = 9
    graph = Graph(number_of_nodes)
    # graph.add_edge(0, 1)
    graph.add_edge(0, 2)

    graph.add_edge(1, 3)
    graph.add_edge(1, 6)

    graph.add_edge(6, 4)

    graph.add_edge(3, 4)
    graph.add_edge(3, 5)

    graph.add_edge(7, 7)

    graph.add_edge(8, 8)

    # dfs(graph, 0)
    print(count_component(graph))

