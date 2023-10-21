class ListNode:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node

    def __str__(self):
        return str(self._data)

class LinkedList:
    def __init__(self, limit=None):
        self._first = None
        self._limit = limit

    def is_empty(self):
        return self._first is None

    def is_full(self):
        if self._limit is None:
            return False
        # Check if the number of nodes in the list exceeds the limit
        return self._count_nodes() >= self._limit

    def _count_nodes(self):
        current = self._first
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def __str__(self):
        if self.is_empty():
            return "Empty Linked List"

        current = self._first
        linked_list_str = ""
        while current is not None:
            linked_list_str += str(current) + " -> "
            current = current.get_next()
        return linked_list_str + "None"
    
    def search(self, data):
        return self._search(data)

    def _search(self, data):
        current = self._first
        while current is not None:
            if current.get_data() == data:
                return True
            current = current.get_next()
        return False

    def insert(self, data):
        if self.is_full():
            return  # Cannot insert when the list is full
        new_node = ListNode(data)
        new_node.set_next(self._first)
        self._first = new_node

    def delete(self, data):
        self._delete(data)

    def _delete(self, data):
        current = self._first
        previous = None
        found = False
        while not found and current is not None:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous is None:
                self._first = current.get_next()
            else:
                previous.set_next(current.get_next())

    def traverse(self):
        result = []
        current = self._first
        while current is not None:
            result.append(current.get_data())
            current = current.get_next()
        return result
