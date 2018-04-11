# dijkstra's algorithm to solve single source shortest path

from pq import PriorityQueue

def dijkstra(graph, start):
    prev = {}
    costs = {}
    costs[start] = 0

    pq = PriorityQueue()
    for node in graph.nodes():
        pq.insert(float('inf'), node)
    pq.insert(0, start)

    while not pq.is_empty():
        cost, ele = pq.delete_min()
        for successor, edge_cost in graph.get_successors(ele):
            new_cost = cost + edge_cost

            if successor not in costs or new_cost < costs[successor]:
                costs[successor] = new_cost
                prev[successor] = ele
                pq.update(new_cost, successor)
    return prev, costs


class Graph(object):
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        self.adjacency_list[node] = set()

    def add_edge(self, start, end, cost):
        self.adjacency_list[start].add((end, cost))

    def get_successors(self, start):
        return self.adjacency_list[start]

    def nodes(self):
        return self.adjacency_list.keys()

def test():
    file = open("dijkstraData.txt", "r")
    lst = file.readlines()
    lst = [l.strip('\n').split('\t') for l in lst]
    graph = Graph()
    for l in lst:
        graph.add_node(int(l[0]))
    for l in lst:
        start = int(l[0])
        for node in l[1: -1]:
            node_cost = node.split(",")
            to, cost = int(node_cost[0]), int(node_cost[1])
            graph.add_edge(start, to, cost)
    print(dijkstra(graph, 1))



if __name__ == '__main__':
    test()
