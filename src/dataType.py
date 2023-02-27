import math
class point:
    def __init__(self, dim : int, val : list[int]):
        self.dimensi = dim # dimensi titik
        self.value = val # koordinat titik
    
    def getDimensi(self) -> int:
        return self.dimensi
    
    def __lt__(self, other):
        # less than
        return self.value[0] < other.value[0]

    def __gt__(self, other):
        # greater than
        return self.value[0] > other.value[0]
    
    def __str__(self):
        # print point
        res:str = "" 
        for i in range(len(self.value)):
            if (i == 0):
                res += ("(" + str(self.value[i]) + ", ")
            elif (i == len(self.value) - 1) :
                res += (str(self.value[i]) + ")")
            else :
                res += (str(self.value[i]) + ", ")
        return res


class couple:
    def __init__(self, p1: point, p2: point):
        self.point1 = p1 # titik pertama
        self.point2 = p2 # titik kedua
        self.distance = getDistance(p1,p2,p1.dimensi) 
        # jarak antara titik pertama dan kedua
    
    def __gt__(self, other):
        # greater than
        return self.distance > other.distance
    
    def __lt__(self, other):
        # less than
        return self.distance < other.distance

    def __str__(self):
        # print couple
        res:str = ""
        for i in range(len(self.point1.value)):
            if (i == 0):
                res += "({:.3f}, ".format( self.point1.value[i])
            elif (i == len(self.point1.value) - 1) :
                res += "{:.3f})".format(self.point1.value[i])
            else :
                res += "{:.3f}, ".format(self.point1.value[i])
        res += " - "
        for i in range(len(self.point2.value)):
            if (i == 0):
                res += "({:.3f}, ".format(self.point2.value[i])
            elif (i == len(self.point2.value) - 1) :
                res += "{:.3f})".format(self.point2.value[i])
            else :
                res += "{:.3f}, ".format(self.point2.value[i])
        return res
    
def getDistance(p : point, q : point, dim : int) -> float:
    """
    Return Euclidean distance between point p and point q
    """
    temp : float = 0
    for i in range(dim):
        temp += (p.value[i] - q.value[i])**2
    return math.sqrt(temp)

