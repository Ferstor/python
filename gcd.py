def gcd (a, b):
    if b == 0: 
        return a
    else:
        return gcd(b, a % b)
GCD = gcd(100, 10)
print(GCD)
