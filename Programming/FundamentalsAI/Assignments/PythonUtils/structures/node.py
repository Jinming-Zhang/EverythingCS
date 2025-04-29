from typing import List, Tuple


class node:
    def __init__(self, id=None, value=None, neighbours=None) -> None:
        self.id = id
        self.value = value
        self.neighbours: List[Tuple[node, float]] = neighbours
