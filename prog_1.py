#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import matplotlib.pyplot as mpp
import numpy

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.arange(0, 200, 0.1)
    mpp.plot(
        arguments,
        [math.sin(a)/a**0.5 for a in arguments]
    )
    mpp.show()
