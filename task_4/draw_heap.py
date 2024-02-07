import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # node color
        self.id = str(uuid.uuid4())  # unique node id


class Heap:
    def __init__(self):
        self.heap = []

    def push(self, elem):
        heapq.heappush(self.heap, elem)

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return not bool(self.heap)

    def make_tree(self):
        heap_arr = list(self.heap)

        # add root node to the given heap tree
        if not self.is_empty():
            root = Node(heap_arr[0])
        cur_node = root
        nodes_queue = Queue()

        # add elements to the heap tree using queue
        for el in heap_arr[1:]:
            if not cur_node.left:
                cur_node.left = Node(el)
                nodes_queue.put(cur_node.left)
            else:
                cur_node.right = Node(el)
                nodes_queue.put(cur_node.right)
                cur_node = nodes_queue.get()
        return root


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


def draw_heap(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(9, 6))
    plt.title("Heap tree")
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


if __name__ == "__main__":
    # Heap creation from array of numbers
    heap = Heap()
    array = [7, 12, 3, 5, 2, 15, 8, 11, 4, 20, 1, 6, 9, 14]
    for el in array:
        heap.push(el)
    print("Heap: ", heap.heap)

    # form heap tree
    root = heap.make_tree()

    # draw heap tree
    draw_heap(root)
