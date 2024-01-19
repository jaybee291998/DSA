import collections

def get_neighbors(node: int, widht: int, height: int) -> list[int]:
    assert node < widht * height
    x: int = node // widht
    y: int = node % widht
    # direction vectors
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    neighbors: list[int] = []
    for i in range(len(dx)):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= height: continue
        if yy < 0 or yy >= widht: continue
        neighbor_node = xx * widht + yy
        neighbors.append(neighbor_node)
    return neighbors

def bfs(start_node: int, widht: int, height: int, visited: list[int]) -> list[int]:
    dq: collections.deque = collections.deque([start_node])
    visited[start_node] = True
    prev: int = [None] * (widht * height)
    while len(dq) > 0:
        current_node = dq.popleft()
        for next_node in get_neighbors(current_node, widht, height):
            if not visited[next_node]:
                dq.append(next_node)
                visited[next_node] = True
                prev[next_node] = current_node
    return prev

def dfs(start_node: int, widht: int, height: int, visited: list[int], path: list[int]) -> None:
    if visited[start_node]:
        return
    visited[start_node] = True
    path.append(start_node)
    for next_node in get_neighbors(start_node, widht, height):
        dfs(next_node, widht, height, visited, path)

def reconstruct_path(start_node: int, end_node: int, path: list[int]) -> list[int]:
    current_node: int = end_node
    traversed_path: list[int] = [current_node]
    count: int = 0
    while current_node > 0 or current_node >= len(path):
        if count > len(path):
            break
        current_node: int = path[current_node]
        if current_node is None:
            break
        traversed_path.append(current_node)
        count += 1
    # print(traversed_path)
    traversed_path.reverse()
    if traversed_path[0] != start_node:
        return []
    return traversed_path

def block_nodes(nodes: list[int], visited: list[bool]) -> None:
    for node in nodes:
        visited[node] = True
        

if __name__ == '__main__':
    rows: int = 10
    cols: int = 10
    number_of_nodes: int = rows * cols
    visited: list[bool] = [False] * number_of_nodes

    blocked_nodes = [
        26, 36, 46, 56,
        52, 53, 54, 55,
        38, 48, 58, 68, 78,
        74, 75, 76, 77
    ]
    block_nodes(blocked_nodes, visited)
    start_node = 0
    end_node = 85
    path: list[int] = []
    dfs(start_node, cols, rows, visited, path)
    print(path)
    print(len(path))
    # print(get_neighbors(0, cols, rows))
    # traversed_path: list[int] = reconstruct_path(start_node, end_node, path)
    # print(traversed_path)
    