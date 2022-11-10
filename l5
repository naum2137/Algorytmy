from typing import Any


class BinaryTree:
    root: 'BinaryNode'

    def __init__(self, root: 'BinaryNode'):
        self.root = root

    def traverse_in_order(self):
        self.root.traverse_in_order()

    def traverse_post_order(self):
        self.root.traverse_post_order()

    def traverse_pre_order(self):
        self.root.traverse_pre_order()

    def show(self):
        self.root.printree(self.root)


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return str(self.value)

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value: Any):
        temp = BinaryNode(value)
        self.left_child = temp

    def add_right_child(self, value: Any):
        temp = BinaryNode(value)
        self.right_child = temp

    def traverse_in_order(self):
        if self.left_child is not None:
            self.left_child.traverse_in_order()
        print(self.value)
        if self.right_child is not None:
            self.right_child.traverse_in_order()

    def traverse_post_order(self):
        if self.left_child is not None:
            self.left_child.traverse_post_order()
        if self.right_child is not None:
            self.right_child.traverse_post_order()
        print(self.value)

    def traverse_pre_order(self):
        print(self.value)
        if self.left_child is not None:
            self.left_child.traverse_pre_order()
        if self.right_child is not None:
            self.right_child.traverse_pre_order()

    @staticmethod
    def printree(node, level=0):
        if node is not None:
            node.printree(node.left_child, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.value))
            node.printree(node.right_child, level + 1)


abcdef = BinaryNode(10)
abcdef.add_left_child(9)
abcdef.add_right_child(2)
abcdef.left_child.add_left_child(1)
abcdef.left_child.add_right_child(3)
abcdef.right_child.add_left_child(4)
abcdef.right_child.add_right_child(6)
x = BinaryTree(abcdef)

x.show()
