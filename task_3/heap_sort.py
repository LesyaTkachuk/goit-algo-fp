import heapq


def heap_sort(iterable, descending=False):
    # define the sigh regarding sorting order (ascending or descending)
    sign = -1 if descending else 1

    # create heap and add elements to it
    heap = []
    for el in iterable:
        heapq.heappush(heap, el * sign)

    # get elements from the heap with updated values and form sorted array
    return [sign * heapq.heappop(h) for _ in range(len(heap))]
