from dataType import point, couple, getDistance
from bruteForce import bruteForce
import numpy as np

def isNeed(p1: point, p2: point, d:float):
    for i in range(p1.dimensi):
        if (abs(p1.value[i] - p2.value[i]) > d):
            return False
    return True

def divideConquer(points : list[point]) -> couple:
    """
    points telah terurut berdasarkan x1
    Mengembalikan 2 titik terdekat dalam points
    menggunakan algoritma Divide and Conquer
    """
    n : int  = len(points)
    numEuclidean:int = 0
    if (n <= 2):
        numEuclidean += 1
        return couple(points[0], points[1]), numEuclidean
    
    elif (n <= 3):
        numEuclidean += 3
        Couple1 = couple(points[0], points[1])
        Couple2 = couple(points[1], points[2])
        Couple3 = couple(points[0], points[2])
        return min(Couple1, Couple2, Couple3), numEuclidean

    else:
        left_part = points[:n//2]
        right_part = points[n//2:]

        closest_left, tempNumLeft = divideConquer(left_part)
        closest_right, tempNumRight = divideConquer(right_part)
        numEuclidean += (tempNumLeft + tempNumRight)

        closestTemp:couple = min(closest_left, closest_right)
        mid:int = (left_part[-1].value[0] + right_part[0].value[0]) // 2

        for left_point in left_part:
            if (abs(mid-left_point.value[0]) <= closestTemp.distance) :
                for right_point in right_part :
                    if (abs(mid-right_point.value[0]) <= closestTemp.distance) :
                        if isNeed(left_point, right_point, closestTemp.distance):
                            numEuclidean += 1
                            newClosestTemp = couple(left_point, right_point)
                            if (closestTemp > newClosestTemp) :
                                closestTemp = newClosestTemp

        return closestTemp, numEuclidean

def driver() :
    A1 = point(3,[1,3,6])
    A2 = point(3,[8,1,2])
    A3 = point(3,[8,1,1])

    List = [A1, A2, A3]

    for titik in List:
        print(titik)
    
    sorted(List)
    nearestCouple = divideConquer(List)
    print("nearest by Divide n Conquer : ", nearestCouple)
