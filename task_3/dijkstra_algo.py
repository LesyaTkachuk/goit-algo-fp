import heapq
from constants import GRAPH, BLUE, RESET


def dijkstra_algo_heap(graph, start):
    # initialise dictionary with distances to the vertexes
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    # create list of unvisited vertexes
    unvisited = list(graph.keys())
    unvisited_vertexes_heap = [(0, start)]

    while len(unvisited_vertexes_heap) > 0:
        # update heap of unvisited vertexes with distances
        unvisited_vertexes_heap = [(distances[vertex], vertex) for vertex in unvisited]
        heapq.heapify(unvisited_vertexes_heap)

        # find the vertex with the shortest distance between unvisited vertexes
        current_vertex = heapq.heappop(unvisited_vertexes_heap)[1]

        # if new distance is shorter, update the shortest distance
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # delete current vertex from the unvisited list
        unvisited.remove(current_vertex)

    return dict(sorted(distances.items(), key=lambda x: x[1]))


if __name__ == "__main__":
    result = dijkstra_algo_heap(GRAPH, "A")
    print(BLUE + "Shortest path from 'A': " + RESET, result)
