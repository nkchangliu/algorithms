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

def prim(graph, start):
# heap to have the vertex that are not added
# key is the cheapest edge
    edge = set()
    overall_cost = 0
    prev = {}
    prev[start] = start
    costs = {}
    costs[start] = 0
    pq = PriorityQueue()
    visited = set()

    for node in graph.nodes():
        pq.insert(float('inf'), node)
    pq.insert(0, start)

    while not pq.is_empty():
        cost, ele = pq.delete_min()
        edge.add((prev[ele], ele))
        overall_cost += cost
        visited.add(ele)
        for successor, edge_cost in graph.get_successors(ele):
            new_cost = edge_cost
            if successor not in visited and (successor not in costs or new_cost < costs[successor]):
                costs[successor] = new_cost
                prev[successor] = ele
                pq.update(new_cost, successor)
    return edge, overall_cost


def kruskal(graph):
    spanning_tree = set()
    edges_list = sort_edge(graph)
    parent = {}
    num = {}

    for node in graph.nodes():
        parent[node] = node
        num[node] = 0
    for vertice1, vertice2, weight in edges_list:
        if find(parent, num, vertice1) != find(parent, num, vertice2):
            union(parent, num, vertice1, vertice2)
            spanning_tree.add((vertice1, vertice2, weight))
    return spanning_tree

def sort_edge(graph):
    edge_list = []
    for start in graph.adjacency_list:
        for end, cost in graph.adjacency_list[start]:
            if end > start:
                edge_list.append((start, end, cost))
    return sorted(edge_list, key = lambda pair: pair[2])

def find(parent, num, vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent, num, parent[vertice])
    return parent[vertice]

def union(parent, num, vertice1, vertice2):
    parent1 = find(parent, num, vertice1)
    parent2 = find(parent, num, vertice2)
    if num[parent1] > num[parent2]:
        parent[parent2] = parent1
    elif num[parent1] < num[parent2]:
        parent[parent1] = parent2
    else:
        parent[parent1] = parent2
        num[parent2] += 1

class Graph(object):
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        self.adjacency_list[node] = set()

    def add_edge(self, start, end, cost):
        self.adjacency_list[start].add((end, cost))
        self.adjacency_list[end].add((start, cost))

    def get_successors(self, start):
        return self.adjacency_list[start]

    def nodes(self):
        return self.adjacency_list.keys()

def test_dijkstra():
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


def test_prim():
    file = open("prim.txt", "r")
    lst = file.readlines()
    lst = [l.strip('\n').split(' ') for l in lst]
    graph = Graph()
    num_nodes = lst[0][0]
    for i in range(1, int(num_nodes) + 1):
        graph.add_node(i)
    for l in lst[1:]:
        start = int(l[0])
        end = int(l[1])
        cost = int(l[2])
        graph.add_edge(start, end, cost)
    print(prim(graph, 1))


if __name__ == '__main__':
    test()
