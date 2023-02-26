import math

class point:
    def __init__(self, dim : int, val : list[int]):
        self.dimensi = dim
        self.value = val

    def __str__(self):
        return "{0}".format(self.value)
    
    def __lt__(self, other):
        return self.value[0] < other.value[0]

    def __gt__(self, other):
        return self.value[0] > other.value[0]
    
    def getDimensi(self) -> int:
        return self.dimensi


class couple:
    def __init__(self, p1: point, p2: point):
        self.point1 = p1
        self.point2 = p2
        self.distance = getDistance(p1,p2,p1.dimensi)
    
    def __gt__(self, other):
        return self.distance > other.distance
    
    def __lt__(self, other):
        return self.distance < other.distance

    def __str__(self):
        return "pair : {0} - {1}, dist : {2}".format(self.point1.value, self.point2.value, self.distance)
        
def getDistance(p : point, q : point, dim : int) -> float:
    temp : float = 0
    for i in range(dim):
        temp += (p.value[i] - q.value[i])**2
    return math.sqrt(temp)