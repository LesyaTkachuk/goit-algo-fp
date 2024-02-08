import uuid

import networkx as nx
import matplotlib.colors as mplt_colors
import matplotlib.pyplot as plt

from deep_first_search import deep_first_search
from breadth_first_search import breadth_first_search


COLORS = [
    "#041259",
    "#051775",
    "#0721a8",
    "#122fc7",
    "#2743d6",
    "#405ade",
    "#4886db",
    "#6396db",
    "#82aae0",
    "#a9c9f5",
]


class Node:
    def __init__(
        self,
        key,
        # color=mplt_colors.to_hex([0.47, 0.0, 1.0, 0.5]),
        color="#7800ff",
    ):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_binary_tree(tree_root, search_func=None, title="Binary Tree Visualisation"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if search_func:
        visited_nodes = search_func(tree_root)
        colors = list()
        for node in tree.nodes(data=True):
            node_label = node[1]["label"]
            node_index = visited_nodes.index(node_label)
            colors.append(COLORS[node_index])
    else:
        colors = [node[1]["color"] for node in tree.nodes(data=True)]

    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(9, 6))
    plt.title(title)
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


# Binary Tree creation
root = Node(7)
root.left = Node(4)
root.left.left = Node(3)
root.left.right = Node(10)
root.right = Node(11)
root.right.left = Node(5)
root.right.right = Node(13)
root.left.left.left = Node(1)
root.right.left.left = Node(2)
root.right.right.right = Node(15)

result = deep_first_search(root)
print("Deep first search: ", result)

result = breadth_first_search(root)
print("Breadth first search: ", result)

# Draw Binary Tree
draw_binary_tree(root)

# Deep First Search Visualisation
draw_binary_tree(root, deep_first_search, "Deep First Search Visualisation")

# Breadth First Search Visualisation
draw_binary_tree(root, breadth_first_search, "Breadth First Search Visualisation")
