import numpy as np

def getPathLength(xs, ys):
    Lpath = 0
    for i in range(len(xs) - 1):
        Lpath += np.sqrt((xs[i + 1] - xs[i])**2 + (ys[i + 1] - ys[i])**2)
    return Lpath


