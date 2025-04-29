import random


def simulation():

    A = False
    B = False
    C = False
    D = False

    # sim A
    if random.random() < 0.1:
        A = True

    # sim B
    if A:
        if random.random() < 0.3:
            B = True
    else:
        if random.random() < 0.7:
            B = True

    # sim C
    if A and B:
        if random.random() < 0.6:
            C = True
    elif A and not B:
        if random.random() < 0.1:
            C = True
    elif not A and B:
        if random.random() < 0.9:
            C = True
    else:
        if random.random() < 0.3:
            C = True

    # sim D
    if C:
        if random.random() < 0.8:
            D = True
    else:
        if random.random() < 0.1:
            D = True

    return [A, B, C, D]


intercount = 10000000
interaction = range(intercount)

sims = []
for i in interaction:
    [h, b, c, d] = simulation()
    sims.append([h, b, c, d])

acount = 0
bcount = 0
ccount = 0
dcount = 0
candacount = 0
dandacount = 0

for [a, b, c, d] in sims:
    if a:
        acount += 1
    if b:
        bcount += 1
    if c:
        ccount += 1
    if d:
        dcount += 1
    if c and a:
        candacount += 1
    if d and a:
        dandacount += 1

print('p(b):', bcount/len(sims))
print('p(c):', ccount/len(sims))
print('p(d):', dcount/len(sims))

print('p(c|a):', candacount/acount)
print('p(d|a):', dandacount/acount)
print('p(a|d):', dandacount/dcount)
