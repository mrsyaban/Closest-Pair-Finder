class point:
    def __init__(self, dim : int, value : list[int]):
        self.dim = dim
        self.val = value

    def __str__(self):
        return "{0} - {1}".format(self.dim, self.val)
    
    def __sub__(self, other):
        return point(self.dim, [self.val[i]-other.val[i] for i in range(min(self.dim, other.dim))])


def euclidDist(p1 : point, p2 : point) -> float:
    res : int = 0
    for i in  range(p1.dim):
        res += ()**2

def divCon(array):
    dump = [[0,0] for i in range(len(array))]
    for i in range(len(array)):
        dump[i][0] = ((array[0]**2 + array[1]**2))**0.5


array = [[3,4,5], [1,9,2], [7,6,5], [1, 5, 4]]

A = point(3, [1,3,4])
B = point(3, [2,5,0])
C = A - B
D = C - A
print(C, D)