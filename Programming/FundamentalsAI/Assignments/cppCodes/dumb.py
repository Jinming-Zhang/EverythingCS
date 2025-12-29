import re
import sys


class judge:
    def __init__(self, code) -> None:
        self.code = code
        self.tryCount = 0

    def guess(self, guess):
        correctPos = 0
        wrongPos = 0
        self.tryCount += 1
        for i in range(len(self.code)):
            g = guess[i]
            c = code[i]
            if g in code and g == c:
                correctPos += 1
            elif g in code and g != c:
                wrongPos += 1
        return [correctPos, wrongPos]

    def getTryCount(self):
        return self.tryCount


def isValidCode(code):
    valids = ['a', 'b', 'c', 'd', 'e', 'f']
    for c in code:
        if not c in valids:
            return False
    return True


def guessColor(judge: judge, code):
    [try11, try12] = judge.guess('abdc')
    [try21, try22] = judge.guess('cdef')
    if (try11 == 2 and try21 == 4):
        return 'cdef'
    elif (try11 == 2 and try21 == 2):
        return 'abef'
    elif (try11 == 2 and try21 == 3):
        [try31, try32] = judge.guess('cdef')
        

    print(try11, try12)
    [try11, try12] = judge.guess('abef')
    print(try11, try12)
    return result


def case2(judge: judge, code):
    pass


def masterorder(judge: judge, code):
    pass


def mastermind(judge: judge):
    print('masterminding ', judge.code)
    colors = guessColor(judge)
    answer = masterorder(colors)
    return answer


def mastermindAll():
    print('masterminding ', 'all')


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) == 2:
        code = argv[1]
        if isValidCode(code):
            if (len(code) == 4):
                mastermind(judge(code))
            else:
                mastermindAll()

    else:
        print('invalid input')
