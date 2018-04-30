from graph import Graph


# bellman_ford alg for single source shortest path for graph with negative edge cost

def bellman_ford(graph, start):
    prev_solution = {}
    for node in graph.nodes():
        prev_solution[node] = float("inf")
    prev_solution[start] = 0

    predecessor = {}
    for node in graph.nodes():
        predecessor[node] = None
    predecessor[start] = start

    for i in range(1, graph.node_size()):
        prev_solution = update_prev(prev_solution, predecessor, graph, start)

    curr_solution = update_prev(prev_solution, predecessor, graph, start)

    if curr_solution == prev_solution:
        return prev_solution, predecessor
    else:
        return None, None


def update_prev(prev_solution, predecessor, graph, start):
    curr_solution = {}
    curr_solution[start] = 0
    for node in graph.nodes():
        prev_value = prev_solution[node]
        curr_min_value = float("inf")
        curr_min_pred = None
        for pred in graph.get_predecessor(node):
            curr_value = prev_solution[pred] + graph.get_cost(pred, node)
            if curr_value < curr_min_value:
                curr_min_value = curr_value
                curr_min_pred = pred
        if curr_min_value < prev_value:
            curr_solution[node] = curr_min_value
            predecessor[node] = curr_min_pred
        else:
            curr_solution[node] = prev_value
    return curr_solution

