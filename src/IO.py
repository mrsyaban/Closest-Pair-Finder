import numpy as np
import matplotlib.pyplot as plt
import random
import time

from visual import display3D
from dataType import point, couple
from bruteForce import bruteForce
from divideConquer import divideConquer

class IO :

    number = 0
    dimensi = 0
    mode = 0

    # Konstruktor
    def __init__(self):
        inValid = True
        while (inValid):
            print("1. Generate titik terdekat")
            print("0. Akhiri Program")
            self.mode = int(input("Pilih untuk melanjutkan program : "))
            if (0 <= self.mode <= 1):
                inValid = False
            else:
                print("Masukan salah silakan masukkan ulang!")
    
    # Method input jumlah titik & Skema validasi input
    def set_number(self):
        inValid = True
        while (inValid):
            try:
                self.number = int(input("Masukan Jumlah Titik  : "))
            except ValueError:
                print("Masukan harus bertipe integer")
            else:
                inValid = False
                
    def set_dimensi(self):
        inValid = True
        while (inValid):
            try:
                self.dimensi = int(input("Masukan Dimensi Titik : "))
            except ValueError:
                print("Masukan harus bertipe integer")
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
            val = np.empty((self.dimensi), dtype=int)
            for j in range(self.dimensi):
                val[j] = random.uniform(-1000, 1000)
            points = np.append(points, point(self.dimensi, val))
        print("\n\nHASIL GENERATE : ")
        startBF = time.time() 
        print("Brute Force : ", bruteForce(points))
        stopBF = time.time()
        print("Waktu BF : ", stopBF-startBF, "\n")

        startDnC = time.time()
        print("DnC : ", divideConquer(sorted(points)))
        stopDnC = time.time()
        print("Waktu DnC : ", stopDnC-startDnC)

        print("\n")

        if (self.dimensi == 3):
            self.visualComp1 = points
            self.visualComp2 = divideConquer(sorted(points))

    def ask_next(self):
        inValid = True
        while (inValid):
            if (self.dimensi == 3):
                print("1. Generate titik terdekat")
                print("2. Visualisasi titik dalam bidang 3D")
                print("0. Akhiri Program")
            else:
                print("1. Generate titik terdekat")
                print("0. Akhiri Program")
            self.mode = int(input("Pilih untuk melanjutkan program : "))
            if (self.dimensi == 3 and 0 <= self.mode <= 2):
                inValid = False
            elif (0 <= self.mode <= 1):
                inValid = False
            else:
                print("Masukan salah silakan masukkan ulang!")
    
    def visual(self):
        display3D(self.visualComp1, self.visualComp2)