import random
 
def MC_pi(n):

    count = 0
    
    for i in range(n):
        x = random.random()
        y = random.random()

        if x ** 2 + y ** 2 <= 1:
            count += 1

    return 4 * (count / n)
 
pi = MC_pi(1000000)

print(pi)
