# Closest Pair Finder

> Composed to fulfill Tucil 2 IF2211 Strategi Algoritma

## Program Description

<p align="center">
    <img src="https://github.com/mrsyaban/Tucil2_13521109-13521119/blob/main/image/splash_screen.jpg" width="600">
</p>

This program is used for find closest pair from random points generated. Program retrieve number of random points to generate and number of dimension of its points from users. Technically program use `Divide and Conquer` algorithm to find the closest pair, but program use `Brute-Force` algorithm as well as a benchmark. Program use two factor to compare the efficiency of the algorithm: Execution time and number of euclidean operation operated. If number of dimension inputed is lower or equal by three, program can visualize the scattering diagram as well.

## Result

<p align="center">
    <img src="https://github.com/mrsyaban/Tucil2_13521109-13521119/blob/main/image/result.jpg" width="600">
</p>

## Program Structure
* [bin/](.\Tucil2_13521109-13521119\bin)
  * [.gitignore](.\Tucil2_13521109-13521119\bin\.gitignore)
* [doc/](.\Tucil2_13521109-13521119\doc)
* [image/](.\Tucil2_13521109-13521119\image)
  * [result.jpg](.\Tucil2_13521109-13521119\image\result.jpg)
  * [splash_screen.jpg](.\Tucil2_13521109-13521119\image\splash_screen.jpg)
* [src/](.\Tucil2_13521109-13521119\src)
  * [bruteForce.py](.\Tucil2_13521109-13521119\src\bruteForce.py)
  * [dataType.py](.\Tucil2_13521109-13521119\src\dataType.py)
  * [divideConquer.py](.\Tucil2_13521109-13521119\src\divideConquer.py)
  * [IO.py](.\Tucil2_13521109-13521119\src\IO.py)
  * [main.py](.\Tucil2_13521109-13521119\src\main.py)
  * [visual.py](.\Tucil2_13521109-13521119\src\visual.py)
* [README.md](.\Tucil2_13521109-13521119\README.md)

## Requirement

- python3
- customtkinter

## How To Run

1. install customtkinter using `pip install customtkinter` in windows terminal 
2. type `python3 main.py` in `..\Tucil2_13521109-13521119` directory

## Author
| NIM      | Name                   |
| -------- | ---------------------- |
| 13521109 | Rizky Abdillah Rasyid  |
| 13521119 | Muhammad Rizky Sya'ban |
