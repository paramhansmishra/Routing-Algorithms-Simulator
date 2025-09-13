from demo_graph import build_demo_graph
from algorithms.dijkstra import dijkstra, reconstruct_path
from algorithms.bellman_ford import bellman_ford
from algorithms.distance_vector import distance_vector
from algorithms.link_state import link_state
from visualization.plot import draw_graph

def pretty_print(dist, prev):
    for dst in dist:
        path = reconstruct_path(prev, dst) if prev[dst] or dst in prev else [dst]
        print(f"{dst}: cost {dist[dst]} via path {path}")

def main():
    g = build_demo_graph()

    print("\n--- Dijkstra from A ---")
    dist, prev = dijkstra(g, 'A')
    pretty_print(dist, prev)
    draw_graph(g, reconstruct_path(prev, 'Z'), "Dijkstra A->Z")

    print("\n--- Bellman-Ford from A ---")
    dist_bf, prev_bf = bellman_ford(g, 'A')
    pretty_print(dist_bf, prev_bf)
    draw_graph(g, reconstruct_path(prev_bf, 'Z'), "Bellman-Ford A->Z")

    print("\n--- Distance-Vector Simulation ---")
    tables = distance_vector(g)
    for node, table in tables.items():
        print(f"Routing table for {node}: {table}")

    print("\n--- Link-State Simulation ---")
    ls = link_state(g)
    for node, (distls, prevls) in ls.items():
        print(f"\nFrom {node}:")
        pretty_print(distls, prevls)

if __name__ == "__main__":
    main()
