import collections

def get_neighbors(node_x: int, node_y, rows: int, cols: int) -> tuple:
    assert 0 <= node_x < rows and 0 <= node_y < cols
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    neighbors_x: list[int] = []
    neighbors_y: list[int] = []
    for i in range(len(dx)):
        new_x = node_x + dx[i]
        new_y = node_y + dy[i]
        if new_x < 0 or new_x >= rows: continue
        if new_y < 0 or new_y >= cols: continue
        neighbors_x.append(new_x)
        neighbors_y.append(new_y)
    return neighbors_x, neighbors_y

def bfs(start_x: int, start_y: int, rows: int, cols: int, visited: list[list[int]] = None) -> list[list[tuple]]:
    assert 0 <= start_x < rows and 0 <= start_y < cols
    if visited is None:
        visited = [[False] * cols for _ in range(rows)]
    dq_x: collections.deque = collections.deque([node_x])
    dq_y: collections.deque = collections.deque([node_y])
    prev: list[list[int]] = [[None] * cols for _ in range(rows)]
    visited[start_x][start_y] = True
    while len(dq_x) > 0:
        current_x: int = dq_x.popleft()
        current_y: int = dq_y.popleft()
        neighbors_x, neighbors_y = get_neighbors(current_x, current_y, rows, cols)
        for i in range(len(neighbors_x)):
            next_x: int = neighbors_x[i]
            next_y: int = neighbors_y[i]
            if not visited[next_x][next_y]:
               visited[next_x][next_y] = True
               dq_x.append(next_x)
               dq_y.append(next_y)
               prev[next_x][next_y] = (current_x, current_y)
    return prev

def reconstruct_path(start_node: tuple, end_node: tuple, path: list[list[tuple]]) -> list[tuple]:
    traversed_path: list[tuple] = []
    current_node_x, current_node_y = end_node
    rows: int = len(path)
    cols: int = len(path[0])
    max_iter: int = rows * cols
    iter_count: int = 0
    while 0 <= current_node_x < rows and 0 <= current_node_y < cols and iter_count < max_iter:
        # print(f'({current_node_x}, {current_node_y})')
        current_node = path[current_node_x][current_node_y]
        if current_node is None:
            break
        current_node_x, current_node_y = current_node
        if current_node_x is None or current_node_y is None:
            break
        # print(path[current_node_x][current_node_y])
        traversed_path.append(current_node)
        iter_count += 1
    traversed_path.reverse()
    if len(traversed_path) >= 1 and traversed_path[0] != start_node:
        return []
    return traversed_path

def block_nodes_line(start_node: tuple, end_node: tuple, visited: list[list[bool]]):
    assert visited is not None and len(visited) >= 1 and len(visited[0]) >= 1
    assert start_node is not None and end_node is not None
    rows: int = len(visited)
    cols: int = len(visited[0])

    start_node_x, start_node_y = start_node

    assert 0 <= start_node_x < rows and 0 <= start_node_y < cols

    end_node_x, end_node_y = end_node

    assert 0 <= end_node_x < rows and 0 <= end_node_y < cols

    assert start_node != end_node

    assert end_node_x >= start_node_x and end_node_y >= start_node_y

    for row in range(start_node_x, end_node_x + 1):
        for col in range(start_node_y, end_node_y + 1):
            visited[row][col] = True

if __name__ == '__main__':
    rows: int = 10
    cols: int = 10

    visited: list[list[bool]] = [[False] * cols for _ in range(rows)]

    # block_nodes_line((1, 0), (1, 2), visited)

    # ob1
    block_nodes_line((3, 0), (3, 3), visited)

    # ob2
    block_nodes_line((5, 1), (5, 4), visited)

    # ob3
    block_nodes_line((7, 0), (7, 1), visited)

    # ob4
    block_nodes_line((6, 3), (8, 3), visited)

    # ob5
    block_nodes_line((1, 5), (7, 5), visited)

    # ob6
    block_nodes_line((0, 7), (8, 7), visited)

    visited[4][8] = True
    visited[6][9] = True
    visited[8][8] = True

    # for row in visited:
    #     print(['#' if e else ' ' for e in row])

    node_x: int = 0
    node_y: int = 9

    target_x: int = 0
    target_y: int = 0

    prev = bfs(node_x, node_y, rows, cols, visited)

    traversed_path: list[tuple] = reconstruct_path((node_x, node_y), (target_x, target_y), prev)
    print(traversed_path)
    print(len(traversed_path))