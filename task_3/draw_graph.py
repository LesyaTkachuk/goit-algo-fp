import networkx as nx
import matplotlib.pyplot as plt

from constants import GRAPH, BLUE, RESET


def draw_graph(graph, calc_shortest_path=False):
    # graph creation from an object
    G = nx.Graph(graph)

    graph_edges = G.edges()
    # add weight to the correspondent edges
    for node, neigbours in GRAPH.items():
        for n_node, weight in neigbours.items():
            if (node, n_node) in graph_edges:
                G[node][n_node]["weight"] = weight

    if calc_shortest_path:
        shortest_paths = nx.single_source_dijkstra_path_length(G, source="A")
        print(BLUE + "Shortest paths networkx: " + RESET, shortest_paths)

    plt.figure(figsize=(8, 8))
    plt.title("Weighted Graph")
    pos = nx.spring_layout(G, seed=42)
    # to draw a graph
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        node_size=900,
        node_color="lightblue",
        edge_color="darkblue",
        font_size=16,
        linewidths=3,
        width=3,
        with_labels=True,
    )

    # create dictionary with edge labels
    labels = {(edge[0], edge[1]): edge[2]["weight"] for edge in G.edges(data=True)}

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=labels,
        font_color="purple",
        font_size=16,
    )

    plt.show()


if __name__ == "__main__":
    draw_graph(GRAPH, True)
