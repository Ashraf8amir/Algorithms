import heapq
from collections import defaultdict

def build_adjacency_list(edges):
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight)) 
    return graph

def prim_algorithm(graph, start):
    pq = []
    heapq.heappush(pq, (0, start, None))  
    
    visited = set()
    mst = []
    total_cost = 0

    while pq:
        weight, current, parent = heapq.heappop(pq)
        
        if current in visited:
            continue

        visited.add(current)
        if parent is not None:  
            mst.append((parent, current, weight))
            total_cost += weight

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, current))

    return mst, total_cost

if __name__ == "__main__":

    edges = [
        ("A", "B", 4), ("A", "H", 8), ("B", "H", 11), ("B", "C", 8),
        ("H", "G", 1), ("H", "I", 7), ("C", "I", 2), ("C", "F", 4),
        ("C", "D", 7), ("D", "F", 14), ("D", "E", 9), ("F", "E", 10),
        ("G", "F", 2), ("G", "I", 6)
    ]

    graph = build_adjacency_list(edges)

    start_node = "A"
    mst, cost = prim_algorithm(graph, start_node)

    print("Minimum Spanning Tree (MST):", mst)
    print("Total Cost of MST:", cost)
