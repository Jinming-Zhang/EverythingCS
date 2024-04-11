import time


def FuncTimeEval(fn) -> float:
    start = time.time()
    fn()
    end = time.time()
    return end-start
