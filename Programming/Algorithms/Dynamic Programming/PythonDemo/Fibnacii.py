from typing import *
from Utils import FuncTimeEval


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


def fibTopDownDict(n: int, cached: Dict[int, int]) -> int:
    if n == 0 or n == 1:
        cached[n] = n
        return n
    if (((n-1) in cached) and ((n-2) in cached)):
        cached[n] = cached[n-1] + cached[n-2]
        return cached[n]
    else:
        cached[n-1] = fibTopDownDict(n-1, cached)
        cached[n-2] = fibTopDownDict(n-2, cached)
        cached[n] = cached[n-1] + cached[n-2]
        return cached[n]


def fibTopDownList(n: int, memo: List[int]) -> int:
    if n == 0 or n == 1:
        memo[n] = n
        return n
    if memo[n-1] == 0:
        memo[n-1] = fibTopDownList(n-1, memo)
    if memo[n-2] == 0:
        memo[n-2] = fibTopDownList(n-2, memo)
    memo[n] = memo[n-1] + memo[n-2]
    return memo[n]


def fibBottomUp(n: int) -> int:
    if n == 0 or n == 1:
        return n
    cached: List[int] = []
    cached.append(0)
    cached.append(1)
    for i in range(2, n+1):
        cached.append(cached[i-1] + cached[i-2])
    return cached[n]


def Demo():
    print("Fib Demo")
    tar: int = 330
    # print(FuncTimeEval(lambda: print(fib(30))))
    print("generating fib ", tar)
    print(FuncTimeEval(lambda: print(fibTopDownDict(tar, {}))))
    print(FuncTimeEval(lambda: print(
        fibTopDownList(tar, [0 for _ in range(0, tar+1)]))))
    print(FuncTimeEval(lambda: print(fibBottomUp(tar))))
