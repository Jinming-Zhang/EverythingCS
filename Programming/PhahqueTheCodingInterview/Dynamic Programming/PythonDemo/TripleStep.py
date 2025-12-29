from typing import *
from Utils import FuncTimeEval


def tripleStepNaive(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    return tripleStepNaive(n-1) + tripleStepNaive(n-2) + tripleStepNaive(n-3)


def tripleStepTopDown(n: int, cache: List[int]) -> int:
    if n < 0:
        return 0
    if n == 0:
        cache[n] = 1
        return 1
    if cache[n] == 0:
        cache[n] = tripleStepTopDown(
            n-1, cache) + tripleStepTopDown(n-2, cache) + tripleStepTopDown(n-3, cache)
    return cache[n]


def Demo():
    print("Triple Step Demo")
    tar = 10
    print(FuncTimeEval(lambda: print(tripleStepNaive(tar))))
    print(FuncTimeEval(lambda: print(
        tripleStepTopDown(tar, [0 for _ in range(0, tar+1)]))))
