import math

simple_dict = dict()

def is_simple(a):
    if simple_dict.get(a) != None:
        return simple_dict.get(a)

    sqrta = int(math.sqrt(a))

    if a == 0:
        return 'Not prime or comosite'

    if a == 1:
        return 'Not prime or comosite'
    
    for i in range(2,sqrta):
        if a % i == 0:
            simple_dict[a] = 'Composite'
            return 'Composite' 
        
    simple_dict[a] = 'Prime'
    return 'Prime'
