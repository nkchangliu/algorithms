class Graph(object):
    def __init__(self):
        self.adjacency_list = {}
        self.reversed_list = {}
        self.cost = {}

    def add_node(self, node):
        self.adjacency_list[node] = set()
        self.reversed_list[node] = set()

    def add_edge(self, start, end, cost = 0):
        self.adjacency_list[start].add(end)
        self.reversed_list[end].add(start)
        self.cost[(start, end)] = cost

    def get_successors(self, start):
        return self.adjacency_list[start]

    def get_predecessor(self, end):
        return self.reversed_list[end]

    def nodes(self):
        return self.adjacency_list.keys()

    def node_size(self):
        return len(self.adjacency_list)

    def reversed_graph(self):
        graph = Graph()
        graph.adjacency_list, graph.reversed_list = self.reversed_list, self.adjacency_list
        return graph

    def get_cost(self, start, end):
        return self.cost[(start, end)]

    def update_edge(self, start, end, new_cost):
        self.cost[(start, end)] = new_cost

    def edges(self):
        return self.cost.keys()



