import matplotlib.pyplot as plt
import numpy as np

class IO :

    number = 0; 

    # Konstruktor
    def __init__(self):
        self.number = 0
    
    # Method input jumlah titik & Skema validasi input
    def set_number(self):
        inValid = True
        while (inValid):
            try:
                self.number = int(input("Masukan Jumlah Titik : "))
            except ValueError:
                print("Masukan harus bertipe integer")
            else:
                inValid = False

    # print landing page
    def landing(self):
        print("LANDING PAGE")

    # menampilkan hasil
    # result = (n, arrayOfPoint, runtime, closestPair)
    def printResult(self, result): 
        print("HASIL")
        self.display3D(result[1])

    # visualisasi 3D 
    def display3D(self, arrayOfPoint):
        fig = plt.figure()
        plot = fig.add_subplot(projection='3d')

        for point in arrayOfPoint:
            xp = point[0]
            yp = point[1]
            zp = point[2]
            plot.scatter(xp,yp,zp, marker='o')
        
        plot.set_xlabel('SUMBU-X')
        plot.set_ylabel('SUMBU-Y')
        plot.set_zlabel('SUMBU-Z')

        plt.show()

if __name__ == "__main__":
    a = IO()
    a.landing()
    a.set_number()
    a.display3D([[3, 4, 5],[10 ,15 ,6],[9, 20, 23]])