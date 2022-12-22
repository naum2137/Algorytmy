from typing import Any


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any, left_child: 'BinaryNode' = None, right_child: 'BinaryNode' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def min(self) -> 'BinaryNode':
        wynik = self
        while wynik.left_child is not None:
            wynik = wynik.left_child
        return wynik


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root: 'BinaryNode'):
        self.root = root

    def __contains__(self, item) -> bool:
        node = self.root
        while node is not None:
            if item == node.value:
                return True
            if item > node.value:
                node = node.right_child
            if item < node.value:
                node = node.left_child
        return False

    def _insert(self, fro: BinaryNode, value: Any):
        if value > fro.value:
            if fro.right_child is None:
                fro.right_child = BinaryNode(value)
            else:
                self._insert(fro.right_child, value)
        elif value < fro.value:
            if fro.left_child is None:
                fro.left_child = BinaryNode(value)
            else:
                self._insert(fro.left_child, value)

    def insert(self, value: Any) -> None:
        self._insert(self.root, value)

    def insert_list(self, list_: list[Any]) -> None:
        for x in list_:
            self._insert(self.root, x)

    def show(self):
        self._show(self.root)

    def _show(self, node: 'BinaryNode', level=0):
        if node is not None:
            self._show(node.left_child, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.value))
            self._show(node.right_child, level + 1)

    def _remove(self, node: BinaryNode, value: Any):
        item = node

    def remove(self, value: Any):
        item = self.root
        while item is not None:
            if value == item.value:
                break
            elif value > item.value:
                item = item.right_child
            elif value < item.value:
                item = item.left_child
        if item.left_child is None and item.right_child is None:
            print(item.value)


binar = BinarySearchTree(BinaryNode(8))
binar.insert_list([3, 10, 1, 6, 4, 7, 14, 13])

binar.show()
binar.remove(13)
binar.show()
