import numpy as np


def arr():
    # generamos un array random hasta el 80, y le damos la dimension de 4x3
    a = np.random.randint(81, size=(4, 3))
    print(a)
    #  le damos la vuelta al array
    b = a[::-1]
    return b

