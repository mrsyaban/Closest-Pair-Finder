import numpy as np
import random
import math
import time

class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __lt__(self, other):
        return self.x < other.x

    def getDistance(p, q):
        return math.sqrt((q.x-p.x)**2 + (q.y - p.y)**2 + (q.z - p.z)**2)



def nearestPoints(points: list[point]):

    n:int = len(points)
    if (n <= 2):
        return point.getDistance(points[0], points[1])
    
    elif (n <= 3):
        distance1 = point.getDistance(points[0], points[1])
        distance2 = point.getDistance(points[1], points[2])
        distance3 = point.getDistance(points[0], points[2])

        return min(distance3, distance2, distance1)

    else :
        left_part = points[:n//2]
        right_part = points[n//2:]

        d1: float = nearestPoints(left_part)
        d2: float = nearestPoints(right_part)

        d: float = min(d1, d2)

        mid: int = (left_part[-1].x + right_part[0].x) // 2

        strip = np.empty((0), dtype=point)
        for i in range(n):
            if ( mid-d <= points[i].x <= mid+d ):
                strip = np.append(strip, points[i])

        if (len(strip)> 1):
            dStrip = nearestBruteForce(strip)
            if (dStrip < d):
                d = dStrip

        # for left_point in left_part:
        #     if (abs(mid-left_point.x) <= d) :
        #         for right_point in right_part :
        #             if (abs(mid-right_point.x) <= d) :
        #                 if not(abs(left_point.x - right_point.x) > d or abs(left_point.y - right_point.y) > d or abs(left_point.z - right_point.z) > d )  :
        #                     newD = point.getDistance(left_point, right_point)
        #                     if (d > newD) :
        #                         d = newD


        return d

# points

def nearestBruteForce(points: list[point]):
    minDis:float = point.getDistance(points[0], points[1])

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (minDis > point.getDistance(points[i], points[j])):
                minDis = point.getDistance(points[i], points[j])

    return minDis

def D3main():
    n = int(input("Masukkan jumlah titik : "))
    # n = 2**10
    points = np.empty((0), dtype=point)

    for i in range(n):
        x = random.uniform(-10**6, 10**6)
        y = random.uniform(-10**6, 10**6)
        z = random.uniform(-10**6, 10**6)

        points = np.append(points, point(x,y,z))

    startBF = time.time() 
    print("Brute Force : ", nearestBruteForce(points))
    stopBF = time.time()
    print("Waktu BF : ", stopBF-startBF, "\n")

    startDnC = time.time()
    print("DnC : ",nearestPoints(sorted(points)))
    stopDnC = time.time()
    print("Waktu DnC : ", stopDnC-startDnC)


# # Show the plot
# # plt.show()
# for i in range(len(points)):
#     print(points[i])
