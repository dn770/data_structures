import unittest


class BinaryNode:

    def __init__(self,value):
        self.__value = value
        self.__left = None
        self.__right = None



    def __str__(self):
        return self.__value


class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def __insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BinaryNode(value)
            else:
                self.__insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryNode(value)
            else:
                self.__insert_recursive(node.right, value)

    def insert_node(self, value):
        node = BinaryNode(value)
        if self.__root is None:
            self.__root = node
        else:
            self.__insert_recursive(self.__root, value)

    def __order_arr(self, node, arr):
        if node is None:
            return arr
        self.__order_arr(node.left, arr)
        arr.append(node.value)
        self.__order_arr(node.right, arr)
        return arr

    def to_order_array(self):
        return self.__order_arr(self.root, [])

    def __print_by_order(self, node):
        if node is None:
            return
        self.__print_by_order(node.left)
        print(node.value)
        self.__print_by_order(node.right)

    def print_inorder(self):
        self.__print_by_order(self.root)

    def get_min(self, node):
        if node.left is None:
            return node.__value
        return self.__get_min(node.left)

    def get_minimum(self):
        if self.__root.left is None:
            return self.__root.value
        return self.__get_min(self.__root.left)

    def __get_max(self, node):
        if node.right is None:
            return node.value
        return self.__get_max(node.right)

    def get_maximum(self):
        if self.__root.right is None:
            return self.__root.value
        return self.__get_max(self.__root.right)

    def __recursive_find(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif node.value > value:
            return self.__recursive_find(node.left, value)
        else:  # node.value < value
            return self.__recursive_find(node.right, value)

    def find(self, value):
        if self.__root is None:
            return False
        else:
            return self.__recursive_find(self.__root, value)


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
        # Insert nodes into the tree for testing
        self.bst.insert_node(5)
        self.bst.insert_node(3)
        self.bst.insert_node(8)
        self.bst.insert_node(2)
        self.bst.insert_node(4)
        self.bst.insert_node(7)
        self.bst.insert_node(9)

    def test_get_minimum(self):
        self.assertEqual(self.bst.get_minimum(), 2)

    def test_get_maximum(self):
        self.assertEqual(self.bst.get_maximum(), 9)

    def test_to_order_array(self):
        expected_array = [2, 3, 4, 5, 7, 8, 9]
        self.assertEqual(self.bst.to_order_array(), expected_array)

    def test_find(self):
        self.assertTrue(self.bst.find(7))
        self.assertFalse(self.bst.find(1))
