from dataType import point, couple
from bruteForce import bruteForce
import numpy as np


def divideConquer(points : list[point]) -> couple:
    """
    points telah terurut berdasarkan x1
    Mengembalikan 2 titik terdekat dalam points
    menggunakan algoritma Divide and Conquer
    """
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

        closest_left:couple = divideConquer(left_part)
        closest_right:couple = divideConquer(right_part)

        closestTemp:couple = min(closest_left, closest_right)

        mid:int = (left_part[-1].value[0] + right_part[0].value[0]) // 2

        # Masukkan semua titik yang berada di jarak +-closestTemp.distance 
        # dari garis antara left_part dan right part 
        strip = np.empty((0),dtype=point)
        for i in range(n):
            if (mid - closestTemp.distance <= points[i].value[0] <= mid + closestTemp.distance):
                strip = np.append(strip, points[i])
        
        # cari couple terdekat dalam strip dengan bruteForce
        if (len(strip) > 1):
            dStrip = bruteForce(strip)
            if (dStrip < closestTemp):
                closestTemp = dStrip

        return closestTemp

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
