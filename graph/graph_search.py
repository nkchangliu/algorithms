import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

from graph import Graph

def find_shortest_path_unweighted(graph, start):
    queue = []
    visited = set()
    prev_node = {}
    queue.append(start)
    prev_node[start] = start
    while queue != []:
        node = queue.pop(0)
        visited.add(node)
        for successor in graph.get_successors(node):
            if successor not in visited and successor not in queue:
                queue.append(successor)
                prev_node[successor] = node

    paths = {}
    for node in graph.nodes():
        paths[node] = [node]
        paths[node].append(prev_node[node])
        prev = prev_node[node]
        while prev != start:
            paths[node].append(prev_node[prev])
            prev = prev_node[prev]

    reversed_paths = {}
    for path in paths:
        reversed_paths[path] = [i for i in reversed(paths[path])]
    return reversed_paths

def connect_parts_undirected(graph):
    # return groups of nodes that are connected in an undirected graph
    visited = set()
    groups = []
    for node in graph.nodes():
        if node not in visited:
            group = set()
            BFS(graph, node, group, visited)
            groups.append(group)
    return groups

def BFS(graph, start, group, visited):
    queue = []
    queue.append(start)
    while queue != []:
        node = queue.pop(0)
        visited.add(node)
        group.add(node)
        for successor in graph.get_successors(node):
            if successor not in visited and successor not in queue:
                queue.append(successor)


def topological_sort(graph):
    # topologial sort of a DAG using DFS
    visited = set()
    order = []
    for node in graph.nodes():
        if node not in visited:
            DFS(graph, node, visited, order)

    return [i for i in reversed(order)]

def DFS(graph, start, visited, order):
    print("start" + str(start))
    visited.add(start)
    for successor in graph.get_successors(start):
        if successor not in visited:
            visited.add(successor)
            DFS(graph, successor, visited, order)
    print("end" + str(start))
    order.append(start)

def kosaraju(graph):
    # kosaraju's algorithm of finding stringly connected components in direct graph
    reversed_graph = graph.reversed_graph()
    _, order = kosaraju_DFS(reversed_graph, reversed(list(graph.nodes())))
    leader, _ = kosaraju_DFS(graph, order)
    for node in leader:
        while leader[node] in leader:
            leader[node] = leader[leader[node]]
    res = {}
    for node in leader:
        value = leader[node]
        if value not in res:
            res[value] = set()
            res[value].add(value)
        res[value].add(node)
    sort_res = sorted(res.keys(), key=lambda s: len(res.get(s)))

    size = []
    for i in range(1,6):
        if i <= len(sort_res):
           size.append(len(res.get(sort_res[-i])))
    return size

def kosaraju_DFS(graph, graph_order):
    # topologial sort of a DAG using DFS
    visited = set()
    order = []
    leader = {}
    for node in graph_order:
        if node not in visited:
            kosaraju_DFS_helper(graph, node, visited, order, leader)
    return leader, [i for i in reversed(order)]

def kosaraju_DFS_helper(graph, start, visited, order, leader):
    visited.add(start)
    for successor in graph.get_successors(start):
        if successor not in visited:
            leader[successor] = start
            visited.add(successor)
            kosaraju_DFS_helper(graph, successor, visited, order, leader)
    order.append(start)



def main():
    file = open("scc.txt", "r")
    lst = file.readlines()
    res = [i.rstrip(' \n').split(" ") for i in lst]
    int_res = []
    for r in res:
       int_res.append([int(i) for i in r])
    graph = Graph()
    for r in int_res:
        graph.add_node(r[0])
        graph.add_node(r[1])
    for r in int_res:
        graph.add_edge(r[0], r[1])
    print(kosaraju(graph))


thread = threading.Thread(target = main)
thread.start()
