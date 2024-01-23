import sys
import heapq
from model.graph import Graph

class Node:
    '''
        node: node number
        distance: current distance from the start node
    '''
    def __init__(self, node: int, distance: int):
        self.node = node
        self.distance = distance
    
    def __lt__(self, other) -> bool:
        return self.distance < other.distance
    
    def __eq__(self, other) -> bool:
        return self.distance == other.distance
    
    def __repr__(self) -> str:
        return f'Node(node={self.node}, distance={self.distance})'

def dijktras(graph: Graph, start_node: int) -> list[int]:
    distances: list[int] = [sys.maxsize] * len(graph)
    priority_queue: list[Node] = []
    prev: list[int] = [None] * len(graph)
    distances[start_node] = 0
    heapq.heappush(priority_queue, Node(start_node, 0))
    while len(priority_queue) > 0:
        current_node: Node = heapq.heappop(priority_queue)
        for neighbor in graph.get_adjacent_nodes(current_node.node):
            new_distance: int = current_node.distance + graph.get_edge(current_node.node, neighbor)
            if new_distance < distances[neighbor]:
                heapq.heappush(priority_queue, Node(neighbor, new_distance))
                distances[neighbor] = new_distance
                prev[neighbor] = current_node.node
    return distances, prev