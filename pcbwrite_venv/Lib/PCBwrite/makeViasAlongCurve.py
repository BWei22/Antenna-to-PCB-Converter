import numpy as np 

def makeViasAlongCurve(xv, yv, Pvia): 
    tmpViasX = []
    tmpViasY = []

    for m in range(len(xv) - 1):
        Dx = xv[m + 1] - xv[m]
        Dy = yv[m + 1] - yv[m]
        d = np.sqrt(Dx**2 + Dy**2)
        N = round(d / Pvia)
        if N > 0:
            tmpViasX.extend(xv[m] + np.arange(N + 1) * Dx / N)
            tmpViasY.extend(yv[m] + np.arange(N + 1) * Dy / N)

    tmpViasX = np.array(tmpViasX)
    tmpViasY = np.array(tmpViasY)
    
    to_delete = []
    for m in range(len(tmpViasX) - 1, 0, -1):
        dx = tmpViasX[m] - tmpViasX[m - 1]
        dy = tmpViasY[m] - tmpViasY[m - 1]
        d = np.sqrt(dx**2 + dy**2)
        if d < 0.2 * Pvia:
            to_delete.append(m - 1)

    tmpViasX = np.delete(tmpViasX, to_delete)
    tmpViasY = np.delete(tmpViasY, to_delete)

    return tmpViasX, tmpViasY


