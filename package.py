import networkx as nx


class Package:
    def __init__(self, start_hub, destination_hub, graph):
        self.weight = None
        self.start_hub = start_hub
        self.destination_hub = destination_hub
        self.graph = graph
        self.path = None
        self.current_hub_idx = 0
        self.set_path()
        self.is_delivered = False

    def get_next_hub(self):
        if not self.path:
            return
        if self.is_delivered:
            return self.path[-1]
        return self.path[self.current_hub_idx + 1]

    def set_path(self):
        predecessors, _ = nx.floyd_warshall_predecessor_and_distance(self.graph)
        self.path = nx.reconstruct_path(self.start_hub[0], self.destination_hub[0], predecessors)

    def change_current_hub_to_next(self):
        self.current_hub_idx += 1
        if self.current_hub_idx > len(self.path):
            self.is_delivered = True
