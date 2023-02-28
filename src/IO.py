import time as t
import numpy as np
import matplotlib.pyplot as plt
import random as rand

from visual import display3D, display1D, display2D
from dataType import point
from bruteForce import bruteForce
from divideConquer import divideConquer, quicksort

class IO :

    number = 0
    dimensi = 0
    mode = 0

    # Konstruktor
    def __init__(self):
        inValid = True
        while (inValid):
            print("""\n
        ===========================================
        0. End Program
        1. Generate Closest Pair
        ===========================================""")
            self.mode = int(input("        Enter Command : "))
            if (0 <= self.mode <= 1):
                inValid = False
            else:
                print("        Masukan salah silakan masukkan ulang!")
    
    # Method input jumlah titik & Skema validasi input
    def set_number(self):
        inValid = True
        while (inValid):
            try:
                self.number = int(input("\n        Number Of Points  : "))
            except ValueError:
                print("        Masukan harus bertipe integer")
            else:
                inValid = False
                
    def set_dimensi(self):
        inValid = True
        while (inValid):
            try:
                self.dimensi = int(input("        Dimension         : "))
            except ValueError:
                print("        Masukan harus bertipe integer")
            else:
                inValid = False

    # print landing page
    def landing(self):
        print("""
        (             )    (   (       )     )     )  
          )\ )       ( /(    )\ ))\ ) ( /(  ( /(  ( /(  
         (()/(    (  )\())  (()/(()/( )\()) )\()) )\()) 
          /(_))   )\((_)\    /(_))(_)|(_)\|((_)\ ((_)\  
         (_))_ _ ((_) ((_)  (_))(_))  _((_)_ ((_)_ ((_) 
        |   \| | | |/ _ \  | _ \_ _||_  /| |/ /\ \ / / 
        | |) | |_| | (_) | |   /| |  / /   ' <  \ V /  
        |___/ \___/ \___/  |_|_\___|/___| _|\_\  |_|   
        CLOSEST PAIR FINDER==========================""")

    # menampilkan hasil
    # result = (n, arrayOfPoint, runtime, closestPair)
    def printResult(self):
        # n = 2**10
        points = np.empty((0), dtype=point)

        for i in range(self.number):
            val = np.empty((self.dimensi), dtype=float)
            for j in range(self.dimensi):
                val[j] = rand.uniform(-10000, 10000)
            points = np.append(points, point(self.dimensi, val))

        startBF = t.perf_counter() 
        closestCoupleBF, numBF = bruteForce(points)
        stopBF = t.perf_counter()
       
        startDnC = t.perf_counter()
        closestCoupleDnC, numDnC = divideConquer(quicksort(points))
        stopDnC = t.perf_counter()

        
        

        print(f"""
                         BRUTE FORCE 
        ===========================================
        Closest Pair           : {closestCoupleBF}
        Distance               : {closestCoupleBF.distance}  
        Number of Euclidean op : {numBF}
        Execution Time  (perf) : {stopBF-startBF} detik\n
        """)

        print(f"""
                      DIVIDE AND CONQUER 
        ===========================================
        Closest Pair           : {closestCoupleDnC}
        Distance               : {closestCoupleDnC.distance}
        Number of Euclidean op : {numDnC}
        Execution Time (perf)  : {stopDnC-startDnC} detik\n
        """)

        if (self.dimensi == 3):
            self.visualComp1 = points
            self.visualComp2= closestCoupleDnC

    def ask_next(self):
        inValid = True
        while (inValid):
            print("\n        ===========================================")
            if (self.dimensi <= 3):
                print("        0. End Program")
                print("        1. Generate Closest Pair")
                print("        2. Visualize points in Scatter Diagram")
            else:
                print("        0. End Program")
                print("        1. Generate Closest Pair")
            print("        ===========================================")
            self.mode = int(input("        Pilih untuk melanjutkan program : "))
            if (self.dimensi <= 3 and 0 <= self.mode <= 2):
                inValid = False
            elif (0 <= self.mode <= 1):
                inValid = False
            else:
                print("        Masukan salah silakan masukkan ulang!")
    
    def visual(self):
        if (self.dimensi == 3):
            display3D(self.visualComp1, self.visualComp2)
        elif(self.dimensi == 2):
            display2D(self.visualComp1, self.visualComp2)
        else:
            display1D(self.visualComp1, self.visualComp2)