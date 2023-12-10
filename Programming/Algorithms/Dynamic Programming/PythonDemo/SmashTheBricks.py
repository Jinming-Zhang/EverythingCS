from typing import *


def smashTheBricks(bigHits: int, newtons: List[int]) -> List[List[int]]:
    tuples: List[Tuple[int, int]] = []
    for i in range(0, len(newtons)):
        tuples.append((newtons[i], i+1))
    tuples.sort(key=lambda x: x[0], reverse=True)
    print(tuples)
    totalHits = 0
    bigHammerHits = []
    smallHammerHits = []
    for i in range(0, len(tuples)):
        if bigHits > 0:
            bigHits -= 1
            bigHammerHits.append(tuples[i][1])
            totalHits += 1
        else:
            smallHammerHits.append(tuples[i][1])
            totalHits += tuples[i][0]

    if len(smallHammerHits) == 0:
        smallHammerHits.append(-1)
    if len(bigHammerHits) == 0:
        bigHammerHits.append(-1)
    bigHammerHits.sort()
    smallHammerHits.sort()

    return [[totalHits], [bigHammerHits], [smallHammerHits]]


if __name__ == '__main__':
    [totaoHits, bigHits, smallHits] = smashTheBricks(4, [3, 2, 5, 4, 6, 7, 9])
    print(totaoHits, bigHits, smallHits)
