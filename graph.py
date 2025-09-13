from collections import defaultdict
import copy

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(dict)  # u -> {v: weight}
        self.directed = directed

    def add_edge(self, u, v, w=1):
        self.adj[u][v] = w
        if not self.directed:
            self.adj[v][u] = w

    def nodes(self):
        s = set(self.adj.keys())
        for u in self.adj:
            s |= set(self.adj[u].keys())
        return sorted(s)

    def neighbors(self, u):
        return self.adj.get(u, {}).items()

    def edges(self):
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u].items():
                if self.directed or (u, v) not in seen and (v, u) not in seen:
                    seen.add((u, v))
                    yield (u, v, w)

    def copy(self):
        g = Graph(directed=self.directed)
        g.adj = copy.deepcopy(self.adj)
        return g
