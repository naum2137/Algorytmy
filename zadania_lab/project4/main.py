from typing import Any, List, Callable
from queue import Queue

class TreeNode:
    value: Any
    children: List['TreeNode']
    fifo = Queue()

    def __init__(self, value: Any, child=None):
        if child is None:
            child = []
        self.value = value
        self.children = child

    def is_leaf(self) -> bool:
        if self.children is None:
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self) -> None:
        print(f"{self.value}", end=", ")
        for x in self.children:
            x.for_each_deep_first()

    def for_each_level_order(self) -> None:
        self.fifo.put(self)
        for x in self.children:
            self.fifo.put(x)
        while not self.fifo.empty():
            x = self.fifo.get()
            if len(x.children) <= 1:
                for y in x.children:
                    self.fifo.put(y)
            print(f"{x.value}", end=", ")


abc = TreeNode(12)
x1 = TreeNode(5)
x2 = TreeNode(7)
x3 = TreeNode(18)
x1.add(x2)
abc.add(x1)
abc.add(x3)
abc.for_each_deep_first()
print("\n")
print(abc.for_each_level_order())
