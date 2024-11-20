
from abc import ABC, abstractmethod
from typing import Set
from dataclasses import dataclass
from rustworkx import PyGraph

class Operation(ABC):
    @abstractmethod
    def __call__(self) -> Set[int]:
        pass

class N(Operation):
    def __init__(self, node_index: int, data_graph: PyGraph) -> None:
        super().__init__()
        self.node_index = node_index
        self.data_graph = data_graph

    def __call__(self) -> Set[int]:
        """Given a node find all the 
        neighboors of node in data_graph"""
        return set(self.data_graph.neighbors(self.node_index))

class Intersection(Operation):
    def __init__(self, left: Operation, right: Operation) -> None:
        super().__init__()
        self.left = left
        self.right = right

    def __call__(self) -> Set[int]:
        return self.left().intersection(self.right())

class Difference(Operation):
    def __init__(self, left: Operation, right: Operation) -> None:
        super().__init__()
        self.left = left
        self.right = right

    def __call__(self) -> Set[int]:
        return self.left().difference(self.right())
    

        


@dataclass
class ComputationalNode:
    compound_operation: Operation
    id: str


def main() -> None:
    pass

if '__name__' == '__main__':
    main()



def test_compound_operations():
    g = PyGraph()

# Create this graph:
# 0 -- 1 -- 2
#  \     /  \
#    3     4
    nodes = [g.add_node(i) for i in range(5)]
    edges = [(0,1), (1,2), (0,3), (2,3), (2,4)]
    for e in edges:
        g.add_edge(e[0], e[1], None)

# Test compound operation: (N(1) ∩ N(2)) - N(0)
# Should find vertices connected to both 1 and 2, but not to 0
    n0 = N(0, g)
    n1 = N(1, g)
    n2 = N(2, g)

    print(n0(), n1(), n2())

    intersection_0_2 = Intersection(n0, n2)
    compound = Difference(intersection_0_2, n0)
    assert compound() == set()

