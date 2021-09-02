import random

def randomize(l):
    for i in range(len(l)//2):
        j = random.randrange(0, len(l))
        k = random.randrange(0, len(l))
        l[j], l[k] = l[k],l[j]