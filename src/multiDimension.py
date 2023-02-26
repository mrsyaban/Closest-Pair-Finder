import random
import math
import numpy as np

class vector:
    def __init__(self, dim : int, value : list[float]):
        self.dim = dim
        self.val = value

    def __str__(self):
        res:str = "" 
        for i in range(len(self.val)):
            if (i == 0):
                res += ("(" + str(self.val[i]) + ", ")
            elif (i == len(self.val) - 1) :
                res += (str(self.val[i]) + ")\n")
            else :
                res += (str(self.val[i]) + ", ")
        return res
    
    # def __sub__(self, other):
    #     return point(self.dim, [self.val[i]-other.val[i] for i in range(min(self.dim, other.dim))])
    
def generateRandom(dim, n) :
    vectorList:list = np.empty((0), dtype=vector)
    for i in range(n):
        tempValue:list = np.empty((0), dtype=float)
        for j in range(dim):
            x = random.uniform(-10**6, 10**6)
            tempValue = np.append(tempValue, x)
        vectorList = np.append(vectorList, vector(dim, tempValue))
    return vectorList

def getDistance(p1:vector, p2:vector) :
    if (p1.dim == p2.dim):
        sumSquare:float = 0
        for i in range(p1.dim):
            sumSquare += (p1.val[i] - p2.val[i])**2
        return math.sqrt(sumSquare)
    else : 
        print("dimensi vector tidak sama")
        return 0
        
def divCon(array):
    dump = [[0,0] for i in range(len(array))]
    for i in range(len(array)):
        dump[i][0] = ((array[0]**2 + array[1]**2))**0.5

tes = generateRandom(5, 10)
for i in tes:
    print(i)