import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, highlight_path=None, title="Network"):
    G = nx.Graph()
    for u, v, w in graph.edges():
        G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_weight="bold")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if highlight_path:
        edges = list(zip(highlight_path, highlight_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="r", width=3)

    plt.title(title)
    plt.show()
