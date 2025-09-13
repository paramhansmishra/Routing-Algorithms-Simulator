from .dijkstra import dijkstra

def link_state(graph):
    results = {}
    for node in graph.nodes():
        dist, prev = dijkstra(graph, node)
        results[node] = (dist, prev)
    return results
