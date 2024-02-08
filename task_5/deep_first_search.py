def deep_first_search(root):
    root_vertex = root
    visited = list()

    # use stack to store the vertexes
    stack = [root_vertex]

    while stack:
        # get vertex from the stack
        vertex = stack.pop()

        if vertex.val not in visited:
            # add vertex to the visited
            visited.append(vertex.val)

            # add vertexes to the stack
            if vertex.right:
                stack.append(vertex.right)
            if vertex.left:
                stack.append(vertex.left)

    return visited
