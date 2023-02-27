from dataType import point, couple
from bruteForce import bruteForce
from divideConquer import divideConquer

#debug
import time as t
import random as rand
import numpy as np

def generateRandom(n:int, dim:int):
    points = np.empty((n), dtype=point)

    for i in range(n):
        val = np.empty((dim), dtype=float)
        for j in range(dim):
            val[j] = rand.uniform(-10**6, 10**6)

        points[i] = point(dim,val)
    
    return points


def main():
    n:int = int(input("Masukkan jumlah titik : "))
    dim:int = int(input("Masukkan dimensi titik : "))

    points = generateRandom(n, dim)
    
    startBF = t.time() 
    closestCoupleBF, numBF = bruteForce(points)
    stopBF = t.time()
    print("Brute Force : ", closestCoupleBF)
    print("number of euclidean op : ", numBF)
    print("Waktu BF : ", stopBF-startBF, " detik\n")

    startDnC = t.time()
    closestCoupleDnC, numDnC = divideConquer(sorted(points))
    stopDnC = t.time()
    print("DnC : ", closestCoupleDnC)
    print("number of Euclidean : ", numDnC)
    print("Waktu DnC : ", stopDnC-startDnC, " detik")
