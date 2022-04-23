# Towers of Hanoi algorithm - Recursive

from typing import List
from enum import Enum

class Stack(Enum):
    SRC = 0
    TGT = 1
    AUX = 2


class Stacks:
    """Source, target, and auxiliary stacks. Printed in order of smallest -> largest disc."""
    def __init__(self, n: int) -> None:
        self.size = n
        self.src: List[int] = [*range(n, 0, -1)]
        self.tgt: List[int] = []
        self.aux: List[int] = []

    def move(self, src: Stack, tgt: Stack):
        """Moves topmost disc from `src` stack to `tgt` stack."""
        match (src, tgt):
            case (Stack.SRC, Stack.TGT):
                self.tgt.append(self.src.pop())
            case (Stack.SRC, Stack.AUX):
                self.aux.append(self.src.pop())
            case (Stack.AUX, Stack.SRC):
                self.src.append(self.aux.pop())
            case (Stack.AUX, Stack.TGT):
                self.tgt.append(self.aux.pop())
            case (Stack.TGT, Stack.AUX):
                self.aux.append(self.tgt.pop())
            case (Stack.TGT, Stack.SRC):
                self.src.append(self.tgt.pop())

        print(self)

    def __repr__(self) -> str:
        res = [
            f'{"".join(f"{n}" for n in reversed(self.src)):>{self.size}}',
            f'{"".join(f"{n}" for n in reversed(self.tgt)):>{self.size}}',
            f'{"".join(f"{n}" for n in reversed(self.aux)):>{self.size}}',
        ]
        return " ".join(res)


def towers_of_hanoi(n: int) -> Stacks:
    """Recursive algorithm for the Towers of Hanoi problem.
    
    - Recursively move all discs above bottom (n-1) from src -> tgt stack via aux
    - Move bottommost disc (n) from src -> tgt
    - Recursively move all discs above bottom (n-1) from aux -> tgt stack via src
    """
    towers = Stacks(n)
    print(towers)

    def inner(n: int, src: Stack, tgt: Stack, aux: Stack, s: Stacks):
        
        if n == 1:
            s.move(src, tgt)
            return

        inner(n-1, src, aux, tgt, s)
        s.move(src, tgt)
        inner(n-1, aux, tgt, src, s)

    inner(n, Stack.SRC, Stack.TGT, Stack.AUX, towers)

    return towers
       

def test_towers():
    # Final target (tgt) stack should equal starting source (src) stack.
    for size in range(1, 10):
        start = Stacks(size).src
        finish = towers_of_hanoi(size).tgt
        assert start == finish


if __name__ == "__main__":
    print("--- Towers of Hanoi ---")

    towers_of_hanoi(3)
