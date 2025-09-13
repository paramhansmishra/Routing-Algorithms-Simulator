from graph import Graph

def build_demo_graph():
    g = Graph()
    g.add_edge('A','B',4)
    g.add_edge('A','C',2)
    g.add_edge('B','C',1)
    g.add_edge('B','D',5)
    g.add_edge('C','D',8)
    g.add_edge('C','E',10)
    g.add_edge('D','E',2)
    g.add_edge('D','Z',6)
    g.add_edge('E','Z',3)
    return g
