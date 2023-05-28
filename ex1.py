import numpy as np


def ndarray():
    # generamos un array lleno de 0 hasta 51 0s
    arr = np.zeros((51, 51))
    # generamos un array de 0 al 51 elementos
    val = np.arange(51)
    np.fill_diagonal(arr, val)
    return arr


print(ndarray())
