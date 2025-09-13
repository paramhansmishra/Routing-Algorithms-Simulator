def bellman_ford(graph, source):
    nodes = graph.nodes()
    dist = {n: float('inf') for n in nodes}
    prev = {n: None for n in nodes}
    dist[source] = 0
    edges = list(graph.edges())

    for _ in range(len(nodes) - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            break

    # detect negative cycle
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Negative-weight cycle detected")

    return dist, prev
