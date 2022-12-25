import math
import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 100

def my_cos(x):

    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        x_pow *= x**2
        multiplier *= -1 / (2*n) / (2*n -1)
        partial_sum += x_pow * multiplier
        
    
    return partial_sum

print(math.cos(0.4))
print(my_cos(0.4))


vs = np.vectorize(my_cos)
print(my_cos, vs)
angles = np.r_[-16.25:16.25:0.01]
plt.plot(angles, np.cos(angles), linewidth=3.0, color='cyan')
plt.plot(angles, vs(angles), linewidth=1.0, color='black')
plt.show()
