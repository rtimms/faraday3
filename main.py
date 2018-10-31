import numpy as np
from scipy import optimize


# whatever the function should be
def f(x):
    return (x**3 - 1)


root = optimize.newton(f, 1.5)

