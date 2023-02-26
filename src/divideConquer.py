from dataType import point, couple
from bruteForce import bruteForce
import numpy as np

#debug
import time as t
import random as rand

def divideConquer(points : list[point]) -> couple:
    n : int  = len(points)

    if (n <= 2):
        return couple(points[0], points[1])
    
    elif (n <= 3):
        Couple1 = couple(points[0], points[1])
        Couple2 = couple(points[1], points[2])
        Couple3 = couple(points[0], points[2])
        return min(Couple1, Couple2, Couple3)

    else:
        left_part = points[:n//2]
        right_part = points[n//2:]

        close1 : couple = divideConquer(left_part)
        close2 : couple = divideConquer(right_part)

        closeTemp : couple = min(close1, close2)

        mid : int = (left_part[-1].value[0] + right_part[0].value[0]) // 2

        strip = np.empty((0),dtype=point)
        for i in range(n):
            if (mid - closeTemp.distance < points[i].value[0] < mid + closeTemp.distance):
                strip = np.append(strip, points[i])
        if (len(strip) > 1):
            dStrip = bruteForce(strip)
            if (dStrip < closeTemp):
                closeTemp = dStrip

        return closeTemp

def driver():
    n = int(input("Masukkan jumlah titik  : "))
    m = int(input("Masukkan dimensi titik : "))
    # n = 2**10
    points = np.empty((0), dtype=point)

    for i in range(n):
        val = np.empty((m), dtype=int)
        for j in range(m):
            val[j] = rand.randint(-1000, 1000)

        points = np.append(points, point(m,val))
    
    startBF = t.time() 
    print("Brute Force : ", bruteForce(points))
    stopBF = t.time()
    print("Waktu BF : ", stopBF-startBF, "\n")

    startDnC = t.time()
    print("DnC : ", divideConquer(sorted(points)))
    stopDnC = t.time()
    print("Waktu DnC : ", stopDnC-startDnC)
    # pair = divideConquer(List)

    # print(pair)

driver()

