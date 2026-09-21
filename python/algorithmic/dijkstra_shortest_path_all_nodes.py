def determine_shortest_paths(edges,
                             num_nodes,
                             starting_node):

    """
    Determine the shortest path from 'starting_node' to all nodes in the graph.
    The graph is assumed to be directed.
    Args:
        edges (list of lists(int)): One element per edge. Each element has from node, to node, and distance.
        num_nodes (int): total number of nodes in graph.
        starting_node (int): index of starting node in graph.

    Returns:
        distances (list of ints): distance from 'starting_node' for each node.
    """

    distance_matrix = [[float('inf') for x in range(num_nodes)] for y in range(num_nodes)]
    for edge in edges:
        start, end, distance = edge
        distance_matrix[start][end] = distance
    unvisited_nodes = set()
    for i in range(num_nodes):
        distance_matrix[i][i] = 0
        unvisited_nodes.add(i)

    def get_next_node():
        mindist = float('inf')
        chosennode = None
        for node in unvisited_nodes:
            if distance_matrix[starting_node][node] < mindist:
                mindist = distance_matrix[starting_node][node]
                chosennode = node
        if chosennode is not None:
            unvisited_nodes.remove(chosennode)
        return chosennode

    current_node = starting_node
    unvisited_nodes.remove(starting_node)
    while current_node:
        if distance_matrix[starting_node][current_node] == float('inf'):
            break
        for j in range(num_nodes):
            distance_matrix[starting_node][j] = \
               min(distance_matrix[starting_node][j],
                   distance_matrix[starting_node][current_node] + distance_matrix[current_node][j])
        current_node = get_next_node()

    return distance_matrix[starting_node]


if __name__ == '__main__':
    edges = [[3,1,3], [1,4,10], [4,2,1], [9,1,40],[6,4,3],[3,6,5]]
    shortest_paths = determine_shortest_paths(edges, 10, 3)
    print(shortest_paths)
