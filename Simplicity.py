import math

simple_dict = dict()

def is_simple(a):
    if simple_dict.get(a) != None:
        return simple_dict.get(a)

    sqrta = int(math.sqrt(a))
    for i in range(2,sqrta):
        if a % i == 0:
            simple_dict[a] = False
            return False
    simple_dict[a] = True
    return True

print(is_simple(100))