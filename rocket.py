import math
import matplotlib.pyplot as mpp

MODEL_G = 9.81
MODEL_DT = 0.001
MODEL_M = 0.01


class Body:
    def __init__(self, x, y, vx, vy):

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
        self.trajectory_x = []
        self.trajectory_y = []
        

    def advance(self):
        
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT


class Rocket(Body):

    def __init__(self, x, y, vx, vy, m, a, v):
        super().__init__(x, y, vx, vy)

        self.m = m
        self.a = a
        self.v = v


    def advance(self):
        super().advance()

        if self.m > 10:
            F = MODEL_M * self.v / MODEL_DT
            self.a = F / self.m
            self.vy -= MODEL_G * MODEL_DT - self.a * MODEL_DT
        else:
            self.vy -= MODEL_G * MODEL_DT

        self.m -= MODEL_M      

        
R = Rocket(0, 0, 5, 0, 30, 0, 80)
B = Body(0, 0, 5, 0)
bodies = [B, R]

for a in range(6000):
    for b in bodies:
        b.advance()
        mpp.plot(b.trajectory_x, b.trajectory_y)
