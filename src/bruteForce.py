from dataType import point, couple 

def bruteForce(points : list[point]) -> couple:
    """
    Mengembalikan 2 titik terdekat dalam points
    menggunakan algoritma brute force
    """
    closestPair : couple = couple(points[0], points[1])

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (closestPair > couple(points[i], points[j])):
                closestPair = couple(points[i], points[j])

    return closestPair

def driver():
    A1 = point(3,[1,3,6])
    A2 = point(3,[8,1,2])
    A3 = point(3,[8,1,1])

    List = [A1, A2, A3]

    for titik in List:
        print(titik)
    
    nearestCouple = bruteForce(List)
    print("nearest by BruteForce : ", nearestCouple)
