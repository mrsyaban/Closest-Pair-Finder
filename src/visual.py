import numpy as np
import matplotlib.pyplot as plt
from dataType import point, couple
from bruteForce import bruteForce

def display1D(arrayOfPoint : list[point], pair : couple):
    """
    display scatter plot 1D of arrayOfPoint with pair highlighted as red
    """
    fig = plt.figure()

    plot = fig.add_subplot()
    static_y = 0
    for point in arrayOfPoint:
        xp = point.value[0]
        if (point == pair.point1 or point == pair.point2):
            plot.scatter(xp, static_y, marker='o', c='red')
        else:
            plot.scatter(xp,static_y, marker='o', c='blue')

    plot.set_xlabel('SUMBU-X')
    plt.show()

def display2D(arrayOfPoint : list[point], pair : couple):
    """
    display scatter plot 2D of arrayOfPoint with pair highlighted as red
    """
    fig = plt.figure()

    plot = fig.add_subplot()
    
    for point in arrayOfPoint:
        xp = point.value[0]
        yp = point.value[1]
        if (point == pair.point1 or point == pair.point2):
            plot.scatter(xp,yp, marker='o', c='red')
        else:
            plot.scatter(xp,yp, marker='o', c='blue')

    plot.set_xlabel('SUMBU-X')
    plot.set_ylabel('SUMBU-Y')
    plt.show()


def display3D(arrayOfPoint : list[point], pair : couple):
    """
    display scatter plot 3D of arrayOfPoint with pair highlighted as red
    """
    fig = plt.figure()

    plot = fig.add_subplot(projection='3d')
    
    for point in arrayOfPoint:
        xp = point.value[0]
        yp = point.value[1]
        zp = point.value[2]
        if (point == pair.point1 or point == pair.point2):
            plot.scatter(xp,yp,zp, marker='o', c='red')
        else:
            plot.scatter(xp,yp,zp, marker='o', c='blue')

    plot.set_xlabel('SUMBU-X')
    plot.set_ylabel('SUMBU-Y')
    plot.set_zlabel('SUMBU-Z')
    plt.show()

def driver3D():
    A1 : point = point(3, [4,5,6])
    A2 : point = point(3, [4,6,6])
    A3 : point = point(3, [7,5,6])

    listP = [A1, A2, A3]

    display3D(listP, bruteForce(listP))