A = ['pee', 'not pee', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Q: 10 locations, with the last one being the correct location to pee
Q = {}
for i in range(1, 11):
    for a in A:
        Q[i, a] = 0

Q[10, 'pee'] = 20
for i in range(1, 10):
    Q[i, 'pee'] = -5

alpha = 0.1
gamma = 0.5


def R(s, a, n):
    if s != 10 and n == 10:
        return 1
    else:
        return -1


def cpQ(Q):
    C = {}
    for i in range(1, 11):
        for a in A:
            C[i, a] = Q[i, a]
    return C


def converged(Qbefore, Qafter, threshold):
    for i in range(1, 11):
        for a in A:
            if(abs(Qbefore[i, a] - Qafter[i, a]) > threshold):
                return False
    return True


t = 1000
for k in range(t):
    # print("The ", k+1, "th time that the puppy wants to pee")
    q_cp = cpQ(Q)
    for s in range(1, 11):
        for a in A:
            current = Q[s, a]
            # possible next states
            if a == A[0] or a == A[1]:
                n = s
            else:
                n = a
            # reward
            reward = R(s, a, n)
            # find optimal successor qvalues
            maxQ = -99999999
            for a in A:
                if Q[n, a] > maxQ:
                    maxQ = Q[n, a]
            sample = reward + gamma*maxQ
            # update
            updated = (1-alpha)*current+alpha*sample
            q_cp[s, a] = updated
    if converged(Q, q_cp, 0.001):
        print("Puppy learned to pee after ", k+1, "tries!")
        break
    Q = cpQ(q_cp)
