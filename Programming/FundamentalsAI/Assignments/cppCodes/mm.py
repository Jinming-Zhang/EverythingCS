import sys
import itertools


class judge:
    ''' 
    a judge holds the secret code and gives responses based on the guess
    Also holds a history of distinct guesses and the corresponding result
    '''

    def __init__(self, code) -> None:
        self.code = code
        self.guessHis = {}
        self.tryCount = 0
        self.verbose = True

    def guess(self, guess):
        correctPos = 0
        wrongPos = 0
        self.tryCount += 1
        for i in range(len(self.code)):
            g = guess[i]
            c = self.code[i]
            if g in self.code and g == c:
                correctPos += 1
            elif g in self.code and g != c:
                wrongPos += 1
        result = [correctPos, wrongPos, correctPos+wrongPos]
        self.guessHis[guess] = result
        if self.verbose:
            print('Guess is %s, \t%d Red, %d White' %
                  (guess, correctPos, wrongPos))
            if (correctPos == 4):
                print('Solved in %d guesses!@!@!@!' % (self.getTryCount()))
        return result

    def getTryCount(self):
        return self.tryCount

    def guessHis(self):
        return self.guessHis

    def filterByHis(self, guesses):
        '''
        guesses: list of guesses
          i.e. ['abcd', 'cdef',...]

        return a filtered guesses that satisfy all the guess history 
        '''
        res = []
        for guess in guesses:
            satisfyall = True
            for oldGuess in self.guessHis:
                posMatchCount = 0
                charMatchCount = 0
                [correctpos, wrongpos, total] = self.guessHis[oldGuess]
                for i in range(len(guess)):
                    if oldGuess[i] == guess[i]:
                        posMatchCount += 1
                    if guess[i] in oldGuess:
                        charMatchCount += 1
                satisfyOrder = posMatchCount == correctpos
                satisfyColor = charMatchCount >= wrongpos
                satisfyall = satisfyall and satisfyOrder and satisfyColor
            if satisfyall:
                res.append(guess)
        return res


def allPermu(code):
    '''
    get all permutations of a string
    i.e. 'abc' -> ['abc','acb','bac','bca','cab','cba']
    '''
    if len(code) == 1:
        return [code]
    permu = []
    head = code[0]
    tail = code[1:]
    subperms = allPermu(tail)
    for subperm in subperms:
        for i in range(len(subperm)):
            digin = subperm[0:i]+head+subperm[i:]
            permu.append(digin)
        permu.append(subperm+head)

    return permu


def allCombo(code, n):
    '''
    get all combinations and permutations of length n from code
    '''
    combins = []
    allcombi = itertools.combinations(code, n)
    for combination in allcombi:
        strC = ''
        for c in combination:
            strC += c
        combins.append(strC)
    allcombos = []
    for combination in combins:
        allcombos += allPermu(combination)
    return allcombos


def masterColor(judge: judge):
    '''
    exhaustive search to get the correct color
    also tries to use different code at different position at the same time to add more info to the guess history
    '''
    [try11, try12, total1] = judge.guess('abcd')
    if (total1 == 4):
        return 'abcd'
    [try21, try22, total2] = judge.guess('cdef')
    if (total2) == 4:
        return 'cdef'

    if (total1 == 2 and total2 == 4):
        return 'cdef'
    elif (total1 == 2 and total2 == 2):
        return 'abef'
    elif (total1 == 2 and total2 == 3):
        [try31, try32, total3] = judge.guess('dcae')
        if total3 == 2:
            #  bef[c|d]
            [try41, try42, total4] = judge.guess('befc')
            if (total4 == 3):
                return 'befd'
            else:
                return 'befc'
        if total3 == 3:
            # aef[c|d]
            [try41, try42, total4] = judge.guess('faec')
            if (total4 == 3):
                return 'aefd'
            else:
                return 'aefc'
    elif (total1 == 3):
        [try21, try22, total2] = judge.guess('edcf')
        if total2 == 2:
            # ab[c|d][e|f]
            [try31, try32, total3] = judge.guess('bedc')
            if (total3 == 3):
                # abe[c|d]
                [try41, try42, total4] = judge.guess('cabe')
                if (total4 == 3):
                    return 'abed'
                else:
                    return 'abec'
            else:
                # abf[c|d]
                [try41, try42, total4] = judge.guess('bafc')
                if (total4 == 3):
                    return 'abfd'
                else:
                    return 'abfc'
        else:
            # cd[e|f][a|b]
            [try31, try32, total3] = judge.guess('ceab')
            if total3 == 3:
                # cde[a|b]
                [try41, try42, total4] = judge.guess('ecda')
                if total4 == 3:
                    return 'cdeb'
                else:
                    return 'cdea'
            else:
                # cdf[a|b]
                [try41, try42, total4] = judge.guess('fdca')
                if total4 == 3:
                    return 'cdfb'
                else:
                    return 'cdfa'
    else:
        return 'abcd'


def masterOrder(judge: judge, code):
    '''
    guess the order of the code given they are all correct color
    '''
    chances = allPermu(code)

    filtered = judge.filterByHis(chances)
    if (len(filtered) == 1):
        judge.guess(filtered[0])
        return filtered[0]
    current = filtered[0]
    [correctpos, _, _] = judge.guess(current)
    while (correctpos != 4):
        # same code as before the loop
        filtered = judge.filterByHis(chances)
        if (len(filtered) == 1):
            judge.guess(filtered[0])
            return filtered[0]
        current = filtered[0]
        [correctpos, _, _] = judge.guess(current)
    return current


def masterAll(judge: judge):
    '''
    guess color and position all at once without exhausive search for colors
    alternative to guessColor -> guessOrder

    no need to check, copied code from masterOrder() except first line
    '''
    chances = allCombo('abcdef', 4)  # only difference

    filtered = judge.filterByHis(chances)
    if (len(filtered) == 1):
        judge.guess(filtered[0])
        return filtered[0]
    current = filtered[0]
    [correctpos, _, _] = judge.guess(current)
    while (correctpos != 4):
        filtered = judge.filterByHis(chances)
        if (len(filtered) == 1):
            judge.guess(filtered[0])
            return filtered[0]
        current = filtered[0]
        [correctpos, _, _] = judge.guess(current)
    return current


def mastermind(judge: judge):
    '''
    given a judge and play by myself
    '''
    # approach with exhausive search for colors
    colors = masterColor(judge)
    answer = masterOrder(judge, colors)

    # approach to guess colors and orders all at once, takes more guesses on averate
    # answer = masterAll(judge)
    return answer


def mastermindAll():
    '''
    play on all possible length-4 code
    '''
    print('masterminding ', 'all')
    allcodes = allCombo('abcdef', 4)
    high = 0
    low = 999
    for code in allcodes:
        goddy = judge(code)
        print('new game...', code)
        result = mastermind(goddy)
        trials = goddy.getTryCount()
        high = max(trials, high)
        low = min(trials, low)
        # print('guessed %s, total trial: %d' % (result, trials))
    print('high: %d, low: %d' % (high, low))


if __name__ == '__main__':
    # please give me a valid code
    # all lower case
    # please give me a valid code
    # all lower case
    # please give me a valid code
    # all lower case
    # please give me a valid code
    # all lower case
    # please give me a valid code
    # all lower case
    # please give me a valid code
    # all lower case
    argv = sys.argv
    if len(argv) == 2:
        code = argv[1]
        if (len(code) == 4):
            myJudge = judge(code)
            res = mastermind(myJudge)
            print('result: %s, guessed %d times!' %
                  (res, myJudge.getTryCount()))
    else:
        mastermindAll()
