# Closest Pair Finder

> Composed to fulfill Tucil 2 IF2211 Strategi Algoritma

## Program Description

<p align="center">
    <img src="https://github.com/mrsyaban/Tucil2_13521109-13521119/blob/main/image/splash_screen.jpg" width="600">
</p>
<p align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/Line-00C300?style=for-the-badge&logo=line&logoColor=white">
</p>

This program is used for find closest pair from random points generated. Program retrieve number of random points to generate and number of dimension of its points from users. Technically program use `Divide and Conquer` algorithm to find the closest pair, but program use `Brute-Force` algorithm as well as a benchmark. Program use two factor to compare the efficiency of the algorithm: Execution time and number of euclidean operation operated. If number of dimension inputed is lower or equal by three, program can visualize the scattering diagram as well.

## Result

<p align="center">
    <img src="https://github.com/mrsyaban/Tucil2_13521109-13521119/blob/main/image/result.jpg" width="600">
</p>

## Program Structure
```
│   README.md
│
├───bin
│       .gitignore
│
├───doc
│       Tucil2_13521109_13521119.pdf
│
├───image
│       result.jpg
│       splash_screen.jpg
│
└───src
        bruteForce.py
        dataType.py
        divideConquer.py
        IO.py
        main.py
        visual.py
```
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
