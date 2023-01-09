def gcd (a,b: int) -> int:
    if b == 0: 
        return a
    else:
        return gcd(b, a % b)
GCD = gcd(100, 10.1)
print(GCD)