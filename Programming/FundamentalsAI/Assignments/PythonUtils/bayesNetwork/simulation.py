from code import interact
import random


def simulation():

    Hungry = False
    Tired = False
    Crying = False
    Woken = False

    if random.random() < 0.3:
        Hungry = True
    if random.random() < 0.2:
        Tired = True

    if Hungry and Tired:
        if random.random() < 0.9:
            Crying = True
    elif Hungry and not Tired:
        if random.random() < 0.85:
            Crying = True
    elif not Hungry and Tired:
        if random.random() < 0.7:
            Crying = True
    else:
        if random.random() < 0.3:
            Crying = True

    if Crying:
        if random.random() < 0.9:
            Woken = True
    else:
        if random.random() < 0.2:
            Woken = True

    return [Hungry, Tired, Crying, Woken]


intercount = 1000000
interaction = range(intercount)
sims = []
for i in interaction:
    [h, y, c, w] = simulation()
    sims.append([h, y, c, w])

wcount = 0
hawCount = 0

for [h, y, c, w] in sims:
    if w:
        wcount += 1
    if h and w:
        hawCount += 1

pw = wcount/intercount
print(pw)
Phaw = hawCount/intercount
phgivenw = Phaw/pw
print(phgivenw)
