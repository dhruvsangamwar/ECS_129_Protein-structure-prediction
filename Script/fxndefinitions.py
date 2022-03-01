import numpy as np


def findG(array, N):
    G = [0, 0, 0]
    for i in range(0, N):
        G += array[i]

    G = np.true_divide(G, N)
    return G
