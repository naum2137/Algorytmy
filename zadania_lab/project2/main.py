from typing import Any


class Node:
    wartosc: Any
    nastepny = None

    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.nastepny = None


class LinkedList:
    def __init__(self):
        self.glowa = Node
        self.ogon = Node

    def __str__(self):
        temp = self.glowa
        wynik = str(temp.wartosc)
        while temp.nastepny:
            temp = temp.nastepny
            wynik += " -> " + str(temp.wartosc)
        return wynik

    def __len__(self):
        dlugosc = 1
        temp = self.glowa
        while temp.nastepny:
            temp = temp.nastepny
            dlugosc += 1
        return dlugosc

    def push(self, wartosc: Any) -> None:
        nowe = Node(wartosc)
        nowe.nastepny = self.glowa
        self.glowa = nowe

    def append(self, wartosc: Any) -> None:
        nowe = Node(wartosc)
        if self.glowa is None:
            self.glowa = nowe
        else:
            temp = self.glowa
            while temp.nastepny:
                temp = temp.nastepny
            temp.nastepny = nowe
            self.ogon = nowe

    def node(self, na: int) -> Any:
        licznik = 1
        temp = self.glowa
        while temp.nastepny:
            if licznik == na:
                break
            temp = temp.nastepny
            licznik += 1
        if licznik == na:
            return temp
        else:
            return "blad"

    def insert(self, value: Any, after: Node) -> None:
        temp = self.glowa
        while temp.nastepny:
            if temp.wartosc == after.wartosc and temp.nastepny == after.nastepny:
                break
            temp = temp.nastepny
        tym = Node(value)
        tym.nastepny = temp.nastepny
        temp.nastepny = tym

    def pop(self) -> Any:
        temp = self.glowa
        self.glowa = temp.nastepny
        return temp.wartosc

    def remove_last(self) -> Any:
        temp = self.glowa
        while temp.nastepny.nastepny:
            temp = temp.nastepny
        tym = temp.nastepny
        temp.nastepny = None
        return tym.wartosc

    def remove(self, after: Node) -> Any:
        temp = self.glowa
        while temp.nastepny:
            if temp.nastepny.wartosc == after.wartosc and temp.nastepny.nastepny == after.nastepny:
                break
            temp = temp.nastepny
        temp.nastepny = temp.nastepny.nastepny


class Stack:
    _storage: LinkedList
    stack: list

    def __init__(self):
        self.stack = []

    def __str__(self):
        wynik = ""
        numer = 1
        for x in self.stack:
            wynik += f"{numer}: {x}\n"
        return wynik

    def __len__(self):
        return len(self.stack)

    def push(self, element: Any) -> None:
        self.stack.append(element)

    def pop(self) -> Any:
        x = self.stack[-1]
        self.stack.pop()
        return x


class Queue:
    _storage: LinkedList

    def __init__(self):
        self.fifo = []

    def __str__(self):
        wynik = ""
        for x in self.fifo:
            wynik += f"{x}, "
        return wynik

    def __len__(self):
        return len(self.fifo)

    def peek(self) -> Any:
        return self.fifo[0]

    def enqueue(self, element: Any) -> None:
        self.fifo.append(element)

    def dequeue(self) -> Any:
        x = self.fifo[0]
        self.fifo.pop(0)
        return x
