def distance_vector(graph, max_iters=100, debug=False):
    nodes = graph.nodes()
    INF = float('inf')

    routing = {n: {d: (INF, None) for d in nodes} for n in nodes}
    for n in nodes:
        routing[n][n] = (0, n)

    neighbors = {n: {v: w for v, w in graph.neighbors(n)} for n in nodes}

    for it in range(max_iters):
        changed = False
        for u in nodes:
            for v, w_uv in neighbors[u].items():
                for dest, (cost, _) in routing[u].items():
                    new_cost = cost + w_uv
                    if new_cost < routing[v][dest][0]:
                        routing[v][dest] = (new_cost, u)
                        changed = True
                        if debug:
                            print(f"iter {it}: {v} updates {dest} via {u} cost {new_cost}")
        if not changed:
            break

    return routing
