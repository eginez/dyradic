
from abc import ABC, abstractmethod
from typing import Callable
from dataclasses import dataclass

class Operation(ABC):
    @abstractmethod
    def __call__() -> list[str]:
        pass

class N(Operation):
    def __init__(self, node: Node, data_graph: ) -> None:
        super().__init__()
        self.node = node

    def __call__() -> list[str]:
        """Given a node find all the 
        neighboors of node in data_graph"""
    

        


@dataclass
class ComputationalNode:
    compound_operations: Callable
    id: str


def main() -> None:
    pass

if '__name__' == '__main__':
    main()
