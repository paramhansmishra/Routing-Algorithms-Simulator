import heapq

def dijkstra(graph, source):
    dist = {n: float('inf') for n in graph.nodes()}
    prev = {n: None for n in graph.nodes()}
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph.neighbors(u):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev

def reconstruct_path(prev, target):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    return list(reversed(path))
