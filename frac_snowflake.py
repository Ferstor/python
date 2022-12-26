import turtle as tl

l= 500
n = 5
tl.speed(100)
tl.up()
tl.goto(-250,100)
tl.down()

def k(l, n):
    if n == 0:
        tl.forward(l)
    else:
        k(l / 3, n - 1)
        tl.left(60)
        k(l / 3, n - 1)
        tl.right(120)
        k(l / 3, n - 1)
        tl.left(60)
        k(l / 3, n - 1)
 
def s(l, n):
    for i in range(3):
        k(l, n)
        tl.right(120)

s(l, n)
