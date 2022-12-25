def egcd(a, b, ls):
    if a == 0:
        ls[0] = 0; ls[1] = 1
        return b
    list = [0,0]
    d = egcd(b % a, a, list)
    ls[0] = list[1] - b // a * list[0]
    ls[1] = list[0]
    return d
lis = [0,0]
print(egcd(20,12,lis))
print(lis)
