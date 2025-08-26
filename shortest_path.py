# Graph represented as an adjacency list
# Each node has a list of tuples: (neighbor, edge_weight)
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    # Step 1: Keep track of unvisited nodes
    unvisited = list(graph)   # initially, all nodes are unvisited
    
    # Step 2: Set up distance dictionary
    # Distance to start = 0, all others = infinity
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Step 3: Set up paths dictionary
    # Each node has an initially empty path
    paths = {node: [] for node in graph}
    paths[start].append(start)  # path to start node is just itself
    
    # Step 4: Dijkstra's algorithm loop
    while unvisited:
        # Pick the unvisited node with the smallest distance
        current = min(unvisited, key=distances.get)
        
        # Check all neighbors of current node
        for node, distance in graph[current]:
            # If a shorter path to neighbor is found:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]  # update distance
                
                # Update path
                if paths[node] and paths[node][-1] == node:
                    # If this node already had a path ending in itself, reset it
                    paths[node] = paths[current][:]
                else:
                    # Otherwise extend from the current path
                    paths[node].extend(paths[current])
                # Add this node at the end of the path
                paths[node].append(node)
        
        # Mark the current node as visited (remove from unvisited list)
        unvisited.remove(current)
    
    # Step 5: Decide which targets to print
    # If a specific target is given, only show that one
    # Otherwise, show shortest path from start to all nodes
    targets_to_print = [target] if target else graph
    
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths

# Example run: shortest path from A to F
shortest_path(my_graph, 'A', 'F')
