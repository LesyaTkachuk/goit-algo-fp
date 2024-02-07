import heapq


def heap_sort(iterable, descending=False):
    # define the sigh regarding sorting order (ascending or descending)
    sign = -1 if descending else 1

    # create heap and add elements to it
    heap = []
    for el in iterable:
        heapq.heappush(heap, el * sign)

    # get elements from the heap with updated values and form sorted array
    return [sign * heapq.heappop(heap) for _ in range(len(heap))]

if __name__=="__main__":
    result=heap_sort([4,13,2,14,7,10,5])
    print(result)