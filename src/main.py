# if __name__ == "__main__":
#     l = [1,2,3]

#     print(l**2)

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
    # n = 2**10
    points = generateRandom(n, dim)
    
    startBF = t.time() 
    print("Brute Force : ", bruteForce(points))
    stopBF = t.time()
    print("Waktu BF : ", stopBF-startBF, " detik\n")

    startDnC = t.time()
    print("DnC : ", divideConquer(sorted(points)))
    stopDnC = t.time()
    print("Waktu DnC : ", stopDnC-startDnC, " detik")
    # pair = divideConquer(List)

    # print(pair)

main()