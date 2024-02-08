from queue import Queue


def breadth_first_search(root):
    root_vertex = root
    # initialise list of visited vertexes
    visited = list()

    # initialise queue and add root vertex to it
    vertexes_queue = Queue()
    vertexes_queue.put(root_vertex)

    # move between vertexes untill queue is not empty
    while not vertexes_queue.empty():
        # get first vertex from the queue
        vertex = vertexes_queue.get()

        # check is this vertex in visited
        if vertex.val not in visited:
            # add this vertex to the visited
            visited.append(vertex.val)
            # add unvisited child nodes to the queue
            if vertex.left:
                vertexes_queue.put(vertex.left)
            if vertex.right:
                vertexes_queue.put(vertex.right)

    return visited
