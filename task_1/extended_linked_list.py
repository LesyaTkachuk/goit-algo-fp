class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Linked List Data structure class realisation with a bunch of extended methods: search, insert, delete, sort, merge, reverse, print, etc.
class LinkedList:
    def __init__(self):
        self.head = None

    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur.next:
            if cur.data == data:
                return cur
            cur = cur.next
        if cur.data == data:
            return cur
        return None

    def search_before(self, data) -> Node | None:
        cur = self.head
        if data == self.head.data:
            return None
        cur = self.head
        while cur.next:
            if cur.next.data == data:
                return cur
            cur = cur.next
        return None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_at_beginning(self, data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur

    def insert_after(self, data, prev_node_data):
        prev_node = self.search_element(prev_node_data)

        if not prev_node or not prev_node_data:
            print(
                f"There is no previous node {prev_node_data} in the given linked list"
            )
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before(self, data, next_node_data):
        cur = self.head
        if cur and cur.data == next_node_data:
            self.insert_at_beginning(data)
        prev = None
        while cur and cur.data != next_node_data:
            prev = cur
            cur = cur.next
        if cur is None:
            print(f"There is no next node {next_node_data} in the given linked list")
            return
        new_node = Node(data)
        new_node.next = cur
        prev.next = new_node

    def delete(self, data):
        cur = self.head
        if cur and cur.data == data:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != data:
            prev = cur
            cur = cur.next
        if cur is None:
            print(f"There is no such node {data} in the given linked list")
            return
        prev.next = cur.next

    def print_list(self, message="Linked list: "):
        cur = self.head
        linked_list = list()
        while cur:
            linked_list.append(cur.data)
            cur = cur.next
        print(f"{message:<30} {linked_list}")

    def reverse(self):
        cur = self.head

        while cur and cur.next:
            next_to_cur = cur.next
            self.delete(cur.next.data)
            self.insert_at_beginning(next_to_cur.data)

    def merge(self, left, right):
        merged = []
        left_index = 0
        right_index = 0

        # compare and add smallest element to the merged array
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # check if there are still elements left in both parts
        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    def merge_sort(self, arr):
        arr = arr[:]
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        return self.merge(self.merge_sort(left_half), self.merge_sort(right_half))

    def make_simple_list(self, linked_list, clear_linked_list=True):
        cur = linked_list.head
        simple_list = list()
        while cur:
            simple_list.append(cur.data)
            if clear_linked_list:
                linked_list.delete(cur.data)
            cur = cur.next
        return simple_list

    def sort(self):
        linked_list = self.make_simple_list(self)

        sorted_list = self.merge_sort(linked_list)

        for el in sorted_list:
            self.insert_at_end(el)

    def merge_and_sort(
        self,
        initial_linked_list,
        second_linked_list,
        is_initialy_sorted=False,
        form_new_linked_list=True,
    ):
        clear_linked_list = not form_new_linked_list
        initial_simple_list = self.make_simple_list(
            initial_linked_list, clear_linked_list
        )
        second_simple_list = self.make_simple_list(
            second_linked_list, clear_linked_list
        )

        if is_initialy_sorted:
            sorted_simple_list = self.merge(initial_simple_list, second_simple_list)
        else:
            joined_simple_list = initial_simple_list + second_simple_list

            sorted_simple_list = self.merge_sort(joined_simple_list)

        result_linked_list = LinkedList() if form_new_linked_list else self

        for el in sorted_simple_list:
            result_linked_list.insert_at_end(el)

        return result_linked_list


if __name__ == "__main__":
    # linked list initialisation
    linked_list = LinkedList()

    # add nodes at the beginning and at the end
    linked_list.insert_at_beginning(8)
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(4)

    linked_list.insert_at_end(5)
    linked_list.insert_at_end(13)

    # print the linked list
    linked_list.print_list()

    # add nodes before and after some nodes
    linked_list.insert_before(5, 17)  # no 17 in the list
    linked_list.insert_before(17, 5)
    linked_list.insert_after(17, 7)  # no 7 in the list
    linked_list.insert_after(7, 17)
    linked_list.insert_after(7.5, 17)

    linked_list.print_list()

    # delete node
    linked_list.delete(7.5)
    linked_list.print_list()
    linked_list.delete(7.5)  # no 7.5 in the list

    # search
    linked_list.search_element(7.5)  # no 7.5 in the list
    linked_list.search_element(7)

    # reverse list
    linked_list.reverse()
    linked_list.print_list("After reverse: ")

    # sort
    linked_list.sort()
    linked_list.print_list("After sorting: ")

    # merge and sort
    new_linked_list = LinkedList()
    arr = [7, 12, 3, 5, 8, 11, 20, 1, 6, 14]
    for el in arr:
        new_linked_list.insert_at_end(el)
    new_linked_list.print_list("Second linked list: ")

    # not mutating merge_and_sort method, initial linked lists remains the same, new resulting linked list is created
    # the third parameter is_initialy_sorted=False appoints that initial linked lists are not sorted
    result_list = linked_list.merge_and_sort(linked_list, new_linked_list, False, True)
    print("After not mutating merge and sort: ")
    linked_list.print_list("Initial linked list: ")
    new_linked_list.print_list("Unsorted second linked list: ")
    result_list.print_list("Resulting linked list: ")

    # mutating merge_and_sort method, both linked lists are merged into one sorted linked list
    # the third parameter is_initialy_sorted=True appoints that initial linked lists are sorted
    new_linked_list.sort()
    new_linked_list.print_list("Sorted second linked list: ")
    result_list = linked_list.merge_and_sort(linked_list, new_linked_list, True, False)

    print("After mutating merge and sort: ")
    new_linked_list.print_list("Sorted second linked list: ")
    result_list.print_list("Resulting linked list: ")
    linked_list.print_list("Initial linked list: ")
