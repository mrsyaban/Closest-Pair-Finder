from dataType import point, couple 

def bruteForce(points : list[point]) -> couple:
    closePair : couple = couple(points[0], points[1])

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (closePair > couple(points[i], points[j])):
                closePair = couple(points[i], points[j])

    return closePair

def driver():
    A1 = point(3,[1,3,6])
    A2 = point(3,[8,1,2])
    A3 = point(3,[8,1,1])
    List = [A3, A2, A1]
    C1 = couple(A1,A2)
    C2 = couple(A3,A2)

    C3 = min(C1,C2)
    
    pair = bruteForce(List)

    print(C3)

# driver()