import itertools
from numbers import Number

class Complex:
    
    def __init__(self, arg):
        
        if isinstance(arg, Number):
            self.b = arg
        elif isinstance(arg, list):
            self.b = arg[0]
            self.i = arg[1]
        elif isinstance(arg, Complex):
            self.b = arg.b
            self.i = arg.i         
 

    def __str__(self):
        a = str(self.b)
        if self.i >= 0:
            a += " + "
        else:
            a += " - "
        a += str(abs(self.i)) + "i"
        return a   
    

    def __lshift__(self, deg):
        return Complex([ self.b << deg, self.i << deg])


    def __rshift__(self, deg):
        return Complex([ self.b >> deg, self.i >> deg])
    

    def __add__(self, other):
        if isinstance(other, Number):
            return Complex([self.b + other, self.i])   
        return Complex([self.b + other.b, self.i + other.i])


    def __radd__(self, other):
        return self.__add__(other)

    
    def __neg__(self):
        return Complex([self.b * -1, self.i * -1])

    
    def __sub__(self, other):
        if isinstance(other, Number):
            other = Complex(other)
        return self.__add__(other.__neg__())

    
    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    
    def __mul__(self, other):  
        b = self.b * other.b - self.i * other.i
        i = self.b * other.i + self.i * other.b
        return Complex([b,i])
        
        
    def __rmul__(self, other):
        return self.__mul__(other)

    
    def __truediv__(self,other):
        b = (self.b * other.b + self.i * other.i) / (other.i ** 2 + other.b ** 2)
        i = (other.b * self.i - self.b * other.i) / (other.i ** 2 + other.b ** 2)
        return Complex([b,i])


    def __pow__(self,other):
        x = Complex(self)
        for i in range(other - 1):
            x = self.__mul__(x) 
        return x


    def __float__(self):
        return float(self.b)
        

    def __int__(self) -> int:
        return int(self.b)


i = Complex([2,1])
g = Complex([6,-1])
print(i)
print(g)
print(i ** 4)
print(i * g)
print(i - g)
print(i + g)
print(g / i)
print(i >> 5)
print(i - i)
print(-g + g)
