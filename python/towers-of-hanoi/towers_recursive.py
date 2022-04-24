# Towers of Hanoi algorithm - Recursive

from typing import List
from enum import Enum
import sys


class Stack(Enum):
    SRC = 0
    TGT = 1
    AUX = 2

    def __str__(self) -> str:
        match self:
            case Stack.SRC:
                return "SRC"
            case self.TGT:
                return "TGT"
            case self.AUX:
                return "AUX"


class Towers:
    """Source, target, and auxiliary stacks. Printed in order of smallest -> largest disc."""
    def __init__(self, n: int) -> None:
        self.size = n
        self.src: List[int] = [*range(n, 0, -1)]
        self.tgt: List[int] = []
        self.aux: List[int] = []

    def move(self, src: Stack, tgt: Stack):
        """Moves topmost disc from `src` stack to `tgt` stack and return disc moved."""
        d = -1
        to = []

        match (src, tgt):
            case (Stack.SRC, Stack.TGT):
                to = self.tgt
                d = self.src.pop()
            case (Stack.SRC, Stack.AUX):
                to = self.aux
                d = self.src.pop()
            case (Stack.AUX, Stack.SRC):
                to = self.src
                d = self.aux.pop()
            case (Stack.AUX, Stack.TGT):
                to = self.tgt
                d = self.aux.pop()
            case (Stack.TGT, Stack.AUX):
                to = self.aux
                d = self.tgt.pop()
            case (Stack.TGT, Stack.SRC):
                to = self.src
                d = self.tgt.pop()   

        to.append(d)

        return d

    def __repr__(self) -> str:
        res = [
            f'{"".join(f"{n}" for n in reversed(self.src)):>{self.size}}',
            f'{"".join(f"{n}" for n in reversed(self.tgt)):>{self.size}}',
            f'{"".join(f"{n}" for n in reversed(self.aux)):>{self.size}}',
        ]
        return " ".join(res)


def towers_of_hanoi(n: int, verbose: bool) -> Towers:
    """Recursive algorithm for the Towers of Hanoi problem.
    
    - Recursively move all discs above bottom (n-1) from src -> tgt stack via aux
    - Move bottommost disc (n) from src -> tgt
    - Recursively move all discs above bottom (n-1) from aux -> tgt stack via src
    """
    towers = Towers(n)
    if verbose: 
        print("--- Towers of Hanoi ---")
        print(f"{'S':^{n}} {'T':^{n}} {'A':^{n}}")
        print(f"{towers}\tstart")

    def inner(n: int, src: Stack, tgt: Stack, aux: Stack, s: Towers):        
        if n == 1:
            d = s.move(src, tgt)

            if verbose: 
                print(f"{towers}\tdisc {d} {src} -> {tgt}")

            return

        inner(n-1, src, aux, tgt, s)        
        d = s.move(src, tgt)

        if verbose: 
            print(f"{towers}\tdisc {d} {src} -> {tgt}")

        inner(n-1, aux, tgt, src, s)

    inner(n, Stack.SRC, Stack.TGT, Stack.AUX, towers)

    return towers 
           

def test_towers():
    # Final target (tgt) stack should equal starting source (src) stack.
    for size in range(1, 10):
        start = Towers(size).src
        finish = towers_of_hanoi(size, False).tgt
        assert start == finish


if __name__ == "__main__":
    try:
        arg1 = int(sys.argv[1])
    except (IndexError, ValueError):
        raise SystemExit(f"Usage: {sys.argv[0]} <#discs>")

    towers_of_hanoi(arg1, True)
