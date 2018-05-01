from graph import Graph
from bellman_ford import bellman_ford
from pq import PriorityQueue

def johnson(graph):
    form_graph(graph)
    weight = get_weight(graph)
    if not weight:
        return None
    reform_graph(graph, weight)
    costs = run_dijkstra(graph)
    res = recover(costs, weight)
    return min(res.items(), key=lambda x: x[1]) 

def form_graph(graph):
    start = -1
    nodes = graph.nodes()
    graph.add_node(start)
    for node in nodes:
        graph.add_edge(start, node, 0)
    return graph

def get_weight(graph):
    weight, _ = bellman_ford(graph, -1)
    return weight

def reform_graph(graph, weight):
    for start, end in graph.edges():
        if start != -1:
            cost = graph.get_cost(start, end)
            new_cost = cost + weight[start] - weight[end]
            graph.update_edge(start, end, new_cost)
    return graph

def run_dijkstra(graph):
    res = {}
    for node in graph.nodes():
        if node != -1:
            cost = dijkstra(graph, node)
            res.update(cost)
    return res

def recover(costs, weight):
    res = {}
    for (start, end) in costs:
        res[(start, end)] = costs[(start, end)] + weight[(end)] - weight[(start)]
    return res

def dijkstra(graph, start):
    prev = {}
    costs = {}
    costs[start] = 0
    visited = set()

    pq = PriorityQueue()

    for node in graph.nodes():
        if node != -1:
            pq.insert(float('inf'), node)
        pq.insert(0, start)

    while not pq.is_empty():
        cost, ele = pq.delete_min()
        visited.add(ele)
        for successor in graph.get_successors(ele):
            new_cost = cost + graph.get_cost(ele, successor)
            if successor not in visited and (successor not in costs or new_cost < costs[successor]):
                costs[successor] = new_cost
                prev[successor] = ele
                pq.update(new_cost, successor)
    res = {}
    for key in costs:
        res[(start, key)] = costs[key]
    return res


def test():
    g = Graph()
    file = open("graph3.txt", "r")
    lst = file.readlines()
    lst = [l.strip('\n').split(' ') for l in lst]
    nodes = lst[0][0]
    for i in range(1, int(nodes) + 1):
        g.add_node(i)
    for start, end, cost in lst[1:]:
        g.add_edge(int(start), int(end), int(cost))
    print(johnson(g))

test()
