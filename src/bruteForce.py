import numpy as np
import random as rand
from dataType import point, couple 

def bruteForce(points : list[point]) -> couple:
    """
    return 2 closest point as a couple in points
    and number of euclidean distance calculation
    using brute force algorithm
    """
    closestPair:couple = couple(points[0], points[1])
    numEuclidean:int = 0 
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            tempCouple = couple(points[i], points[j])
            numEuclidean += 1
            if (closestPair > tempCouple):
                closestPair = tempCouple

    return closestPair, numEuclidean

def driver():
    # 100 titik 
    # 3 dimensi
    points = np.empty((0), dtype=point)

    for i in range(100):
        val = np.empty((3), dtype=float)
        for j in range(3):
            val[j] = rand.uniform(-1000, 1000)
            print(val[j], end=" ")
        points = np.append(points, point(3, val))

    for titik in points:
        print(titik)
    
    nearestCouple, _ = bruteForce(points)
    print("nearest by BruteForce : ", nearestCouple)
