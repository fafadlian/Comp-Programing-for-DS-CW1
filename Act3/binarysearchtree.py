class TreeNode:
    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_left(self):
        return self._left

    def set_left(self, left):
        self._left = left

    def get_right(self):
        return self._right

    def set_right(self, right):
        self._right = right

class BinarySearchTree:
    def __init__(self, limit=None):
        self._root = None
        self._limit = limit

    def __init__(self, limit=None):
        self._root = None
        self._limit = limit

    def is_empty(self):
        return self._root is None

    def is_full(self):
        if self._limit is None:
            return False
        # Check if the number of nodes in the tree exceeds the limit
        return self._count_nodes(self._root) >= self._limit

    def _count_nodes(self, node):
        if node is None:
            return 0
        left_count = self._count_nodes(node.get_left())
        right_count = self._count_nodes(node.get_right())
        return 1 + left_count + right_count

    def get_root(self):
        return self._root

    def set_root(self, root):
        self._root = root

    def get_limit(self):
        return self._limit

    def set_limit(self, limit):
        self._limit = limit
    def search(self, data):
        return self._search(self._root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if data == node.get_data():
            return True
        elif data < node.get_data():
            return self._search(node.get_left(), data)
        else:
            return self._search(node.get_right(), data)

    def insert(self, data):
        if self.is_full():
            return  # Cannot insert when the tree is full
        self._root = self._insert(self._root, data)

    def _insert(self, node, data):
        if node is None:
            return TreeNode(data)
        if data <= node.get_data():
            node.set_left(self._insert(node.get_left(), data))
        else:
            node.set_right(self._insert(node.get_right(), data))
        return node

    def delete(self, data):
        self._root = self._delete(self._root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        if data < node.get_data():
            node.set_left(self._delete(node.get_left(), data))
        elif data > node.get_data():
            node.set_right(self._delete(node.get_right(), data))
        else:
            if node.get_left() is None:
                return node.get_right()
            elif node.get_right() is None:
                return node.get_left()
            node.set_data(self._min_value(node.get_right()))
            node.set_right(self._delete(node.get_right(), node.get_data()))
        return node

    def _min_value(self, node):
        while node.get_left() is not None:
            node = node.get_left()
        return node.get_data()

    def traverse(self):
        result = []
        self._inorder_traversal(self._root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.get_left(), result)
            result.append(node.get_data())
            self._inorder_traversal(node.get_right(), result)

    def print_tree(self):
        self._print_tree(self._root, 0)

    def _print_tree(self, node, depth):
        if node is not None:
            self._print_tree(node.get_right(), depth + 1)
            print("  " * depth + str(node.get_data()))
            self._print_tree(node.get_left(), depth + 1)
