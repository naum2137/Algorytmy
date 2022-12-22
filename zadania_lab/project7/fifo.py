from typing import Any


class Node:
    value: Any
    next: 'Node' or None

    def __init__(self, value: Any, nextt: 'Node' = None):
        self.value = value
        self.next = nextt


class LinkedList:
    head: Node or None
    tail: Node or None

    def __init__(self, value: Any):
        temp = Node(value)
        self.head = temp
        self.tail = temp

    def __repr__(self):
        if self.head is None:
            return "pusto"
        wynik = ""
        temp = self.head
        wynik += f"{temp.value}"
        while temp != self.tail:
            temp = temp.next
            wynik += f" -> {temp.value}"
        return wynik

    def __len__(self) -> int:
        if self.head is None:
            return 0
        temp = self.head
        wynik = 1
        while temp != self.tail:
            temp = temp.next
            wynik += 1
        return wynik

    def push(self, value: Any) -> None:
        temp = Node(value, self.head)
        self.head = temp

    def append(self, value: Any) -> None:
        temp = Node(value)
        self.tail.next = temp
        self.tail = temp

    def node(self, at: int) -> 'Node':
        temp = self.head
        while at > 0:
            temp = temp.next
            at -= 1
        return temp

    def insert(self, value: Any, after: Node) -> None:
        temp = self.head
        node = Node(value)
        while temp != after:
            temp = temp.next
            if temp == self.tail:
                print(f"brak wezla {after.value} w liscie")
                return
        if temp != self.tail:
            node.next = temp.next
            temp.next = node
        else:
            temp.next = node
            self.tail = node

    def pop(self) -> 'Node':
        temp = self.head
        self.head = self.head.next
        return temp

    def remove_last(self) -> 'Node':
        wynik = self.tail
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return temp
        else:
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
            return wynik

    def remove(self, after: Node) -> 'Node':
        temp = self.head
        while temp != after:
            temp = temp.next
        if temp.next == self.tail:
            wynik = temp.next
            temp.next = None
            self.tail = temp
        else:
            wynik = temp.next
            temp.next = temp.next.next
        return wynik
