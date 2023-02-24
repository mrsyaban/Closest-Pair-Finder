
def euclidDist(point1, point2):
    return (((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2) + ((point1[2]-point2[2])**2))**0.5

def divCon(array):
    dump = [[0,0] for i in range(len(array))]
    for i in range(len(array)):
        dump[i][0] = ((array[0]**2 + array[1]**2))**0.5


array = [[3,4,5], [1,9,2], [7,6,5], [1, 5, 4]]

for i in range(len(array)):
    for j in range(i+1,len(array)):
        print(i,j, euclidDist(array[i], array[j]))


