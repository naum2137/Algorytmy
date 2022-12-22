from typing import Any
from typing import Dict, List
from typing import Optional
from typing import Callable
from fifo import Queue


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index: int):
        self.data = data
        self.index = index

    def __repr__(self):
        return str(self.data)


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]
    directed: bool

    def __init__(self, source: Vertex, destination: Vertex, directed: bool = False, weight: Optional[float] = None):
        self.source = source
        self.destination = destination
        self.weight = weight
        self.directed = directed

    def __repr__(self):
        return f"{self.source} -> {self.destination}"


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, adjacencies: Dict[Vertex, List[Edge]]):
        self.adjacencies = adjacencies

    def create_vertex(self, data: Any) -> Vertex:
        id_ver = 0
        for keys in self.adjacencies:
            if keys.index <= id_ver:
                id_ver = keys.index + 1
        temp = Vertex(data, id_ver)
        self.adjacencies[temp] = []
        return temp

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge = Edge(source, destination, True, weight)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge1 = Edge(source, destination, True, weight)
        edge2 = Edge(destination, source, True, weight)
        self.adjacencies[source].append(edge1)
        self.adjacencies[destination].append(edge2)

    def add(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self) -> None:
        kolejka = Queue()
        odwiedzone = []
        klucz = list(self.adjacencies.keys())[0]
        kant = list(self.adjacencies.values())[0]
        for x in kant:
            kolejka.enqueue(x.destination)




def main():
    abc = Graph({})
    abc.create_vertex(12)
    abc.create_vertex(10)
    abc.create_vertex(9)
    abc.add_undirected_edge(list(abc.adjacencies.keys())[0], list(abc.adjacencies.keys())[1])
    abc.add_undirected_edge(list(abc.adjacencies.keys())[0], list(abc.adjacencies.keys())[2])
    abc.traverse_breadth_first()


if __name__ == '__main__':
    main()
