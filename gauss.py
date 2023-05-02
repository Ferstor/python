import numpy as np

def gauss(a, b):

    a = a.copy()
    b = b.copy()
    n = len(b)

    def forward(a, b):
        for k in range(n-1):
            for i in range(k+1, n):
                m = a[i,k] / a[k,k]
                a[i,k:] = a[i,k:] - m * a[k,k:]
                b[i] = b[i] - m * b[k]
        return a, b
    
    forward(a, b)
    print(a)

    def backward(a, b):
        x = np.zeros(n, dtype = float)
        for i in range(n-1, -1, -1):
            x[i] = (b[i] - np.dot(a[i,i+1:], x[i+1:])) / a[i,i]
        return x
    

    x = backward(a, b)
    return x

a = np.array([[1.5, 2, 1.5, 2],
    [3, 2, 4, 1],
    [1, 6, 0, 4],
    [2, 1, 4, 3]], dtype=float)
b = np.array([5, 6, 7, 8], dtype=float)
x = gauss(a, b)

print(x)