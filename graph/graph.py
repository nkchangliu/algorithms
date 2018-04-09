class Graph(object):
    def __init__(self):
        self.adjacency_list = {}
        self.reversed_list = {}

    def add_node(self, node):
        self.adjacency_list[node] = set()
        self.reversed_list[node] = set()

    def add_edge(self, start, end):
        self.adjacency_list[start].add(end)
        self.reversed_list[end].add(start)

    def get_successors(self, start):
        return self.adjacency_list[start]

    def nodes(self):
        return self.adjacency_list.keys()

    def reversed_graph(self):
        graph = Graph()
        graph.adjacency_list, graph.reversed_list = self.reversed_list, self.adjacency_list
        return graph


