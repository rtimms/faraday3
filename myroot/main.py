import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


# whatever the function should be
def f(x):
    return x


# def mybisection(f, a, b, epsilon):
#    return x

root = optimize.newton(f, 1.5)

print(root)
