import random


def keygen(n):
    s=""
    for i in range(n):
        s+=str(random.randint(0,1))
    return s