from math import sin, pi
import random
 
def MC_sin(n):

    count= 0

    for i in range(n):
        x = random.uniform(0, pi)
        y = random.random()

        if y <= sin(x) :
            count += 1

    return pi * count / n

print(MC_sin(1000000))
