import networkx as nx
import itertools


def complete_graph(hub_list) -> nx.Graph:
    result = nx.Graph()

    all_pairs = itertools.permutations(hub_list, 2)
    distances = []
    for pair in all_pairs:
        x1 = pair[0][1][0]
        y1 = pair[0][1][1]
        x2 = pair[1][1][0]
        y2 = pair[1][1][1]
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

        if pair[0][0][4] == "S":
            if (pair[1][0][4] == "S" or pair[1][0][4] == "M") and distance < 150:
                distances.append((pair[0][0], pair[1][0], distance))
        if pair[0][0][4] == "M":
            if distance < 250:
                distances.append((pair[0][0], pair[1][0], distance))
        if pair[0][0][4] == "L":
            if (pair[1][0][4] == "M" or pair[1][0][4] == "L") and distance < 500:
                distances.append((pair[0][0], pair[1][0], distance))

    for hub in hub_list:
        result.add_node(hub[0], pos=hub[1])

    result.add_weighted_edges_from(distances)
    return result
