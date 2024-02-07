import heapq


def dijkstra_algo(graph, start):
    # initialise dictionary with distances to the vertexes
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    print("distances", distances)

    # create list of unvisited vertexes
    unvisited = list(graph.keys())

    while unvisited:
        print("unvisited", unvisited)

        # find the vertex with the shortest distance between unvisited
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        print("current vertex", current_vertex)

        if distances[current_vertex] == float("infinity"):
            break

        # if new distance is shorter, update the shortest distance
        for neighbor, weight in graph[current_vertex].items():
            print("graph[current_vertex].items()", graph[current_vertex].items())
            distance = distances[current_vertex] + weight
            print(
                "distances[current_vertex]", current_vertex, distances[current_vertex]
            )
            print("distance", distance)
            print("distances[neighbor]", neighbor, distances[neighbor])
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # delete current vertex from the unvisited list
        unvisited.remove(current_vertex)

    return distances


def dijkstra_algo_heap(graph, start):
    # initialise dictionary with distances to the vertexes
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    # create list of unvisited vertexes
    unvisited = list(graph.keys())
    # initialise heap of unvisited vertexes distances
    unvisited_vertexes_heap = []
    # unvisited_vertexes_heap = [el for el in distances.]
    heapq.heapify()
    # for vertex in graph:
    #     heap_element = ((0, start) if vertex == start else (float("infinity", vertex)),)
    #     heapq.heappush(unvisited_vertexes_heap, heap_element)

    while unvisited_vertexes_heap:

        print("distances", distances)
        print("unvisited_vertexes_heap", unvisited_vertexes_heap)

        # find the vertex with the shortest distance between unvisited
        current_vertex = heapq.heappop(unvisited_vertexes_heap)[1]

        print("current vertex", current_vertex)

        # if new distance is shorter, update the shortest distance
        for neighbor, weight in graph[current_vertex].items():
            print("graph[current_vertex].items()", graph[current_vertex].items())
            distance = distances[current_vertex] + weight
            print(
                "distances[current_vertex]", current_vertex, distances[current_vertex]
            )
            print("distance", distance)
            print("distances[neighbor]", neighbor, distances[neighbor])
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # delete current vertex from the unvisited list
        unvisited.remove(current_vertex)

    return distances


if __name__ == "__main__":
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        "D": {"B": 3, "C": 2, "E": 4},
        "E": {"D": 4},
    }

    result = dijkstra_algo(graph, "A")
    print("Shortest path from 'A': ", result)

    result = dijkstra_algo_heap(graph, "A")
    print("Shortest path from 'A': ", result)
