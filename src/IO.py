import customtkinter
import random as rand
import numpy as np
import time as t

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from divideConquer import divideConquer, quicksort
from matplotlib.figure import Figure
from dataType import couple, point
from bruteForce import bruteForce

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Closest Pair Finder")
        self.geometry(f"{1295}x{720}")

        # configure grid layout (4x4)
        self.grid_columnconfigure((1,2,3,4,5,6,7), weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=480, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((4,7), weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="DIVIDE AND CONQUER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, columnspan=2, padx=0, pady=(20, 0))
        self.sub_label = customtkinter.CTkLabel(self.sidebar_frame, text="Rizky & Rizky 's", font=customtkinter.CTkFont(size=14, weight="normal"))
        self.sub_label.grid(row=1, column=0, columnspan=2, padx=0, pady=(0, 20))

        self.label_number = customtkinter.CTkLabel(self.sidebar_frame, text="Jumlah Titik :", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label_number.grid(row=2, column=0, padx=(20, 15), pady=(0, 5), sticky='e')
        
        self.label_dimensi = customtkinter.CTkLabel(self.sidebar_frame, text="Jumlah Dimensi :", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label_dimensi.grid(row=3, column=0, padx=(20, 15), pady=(0, 5), sticky='e')
        
        self.entry_number = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="0")
        self.entry_number.grid(row=2, column=1, padx=(0, 40), pady=(0, 5), sticky="nsew")

        self.entry_dimensi = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="3")
        self.entry_dimensi.grid(row=3, column=1, padx=(0, 40), pady=(0, 5), sticky="nsew")

        self.time_bf_label = customtkinter.CTkLabel(self.sidebar_frame, text="BF Time :", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.time_bf_label.grid(row=5, column=0, padx=(20, 15), pady=(0, 5), sticky='e')
        self.time_dnc_label = customtkinter.CTkLabel(self.sidebar_frame, text="DnC Time :", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.time_dnc_label.grid(row=6, column=0, padx=(20, 15), pady=(0, 5), sticky='e')

        self.timeRes_bf_label = customtkinter.CTkLabel(self.sidebar_frame, text="0 second", font=customtkinter.CTkFont(size=14, weight="normal"))
        self.timeRes_bf_label.grid(row=5, column=1, padx=(5, 10), pady=(0, 5), sticky='w')
        self.timeRes_dnc_label = customtkinter.CTkLabel(self.sidebar_frame, text="0 second", font=customtkinter.CTkFont(size=14, weight="normal"))
        self.timeRes_dnc_label.grid(row=6, column=1, padx=(5, 10), pady=(0, 5), sticky='w')

        self.run_button = customtkinter.CTkButton(self.sidebar_frame, text="Generate & Run", command=self.run)
        self.run_button.grid(row=8, column=0, columnspan=2, padx=20, pady=30, sticky="s")

        self.vis_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.vis_frame.grid(row=0, column=1, columnspan=6, pady=0)

        self.fig = Figure(figsize=(12,5), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Create a canvas to display plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.vis_frame)
        self.canvas.get_tk_widget().pack()

        self.terminal_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.terminal_frame.grid(row=1, column=1, columnspan=6, pady=0, sticky='nswe')
        self.terminal_frame.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1)
        self.terminal_frame.grid_rowconfigure((0,1,2), weight=1)

        self.bf_label = customtkinter.CTkLabel(self.terminal_frame,  text="Brute Force", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.bf_label.grid(row=0, column=0, columnspan=3, sticky='we', pady=5, padx=5)
        self.comp_label = customtkinter.CTkLabel(self.terminal_frame,  text="Efficiency", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.comp_label.grid(row=0, column=3, columnspan=2, sticky='we', pady=5, padx=5)
        self.dnc_label = customtkinter.CTkLabel(self.terminal_frame,  text="Divide & Conquer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.dnc_label.grid(row=0, column=5, columnspan=3, sticky='we', pady=5, padx=5)

        self.bf_frame = customtkinter.CTkFrame(self.terminal_frame, corner_radius=10, fg_color='#ebebeb')
        self.bf_frame.grid(row=1, column=0, columnspan=3, sticky='nswe', pady=5, padx=5)
        self.comp_frame = customtkinter.CTkFrame(self.terminal_frame, corner_radius=10, fg_color='#ebebeb')
        self.comp_frame.grid(row=1, column=3, columnspan=2, sticky='nswe', pady=5, padx=5)
        self.dnc_frame = customtkinter.CTkFrame(self.terminal_frame, corner_radius=10, fg_color='#ebebeb')
        self.dnc_frame.grid(row=1, column=5, columnspan=3, sticky='nswe', pady=5, padx=5)

        self.bf_frame.grid_rowconfigure((0), weight=1)
        self.bf_frame.grid_columnconfigure((1), weight=1)

        self.bf_result1 = customtkinter.CTkLabel(self.bf_frame, wraplength=300, text="", font=customtkinter.CTkFont(size=14, weight="normal"))
        self.bf_result1.grid(row=2, column=0, sticky='ne', pady=(0,10), padx=(15,0))
        self.bf_result1_value = customtkinter.CTkLabel(self.bf_frame, wraplength=300, text="",font=customtkinter.CTkFont(size=14, weight="normal"))
        self.bf_result1_value.grid(row=2, column=1, sticky='w', pady=(0,10), padx=(10,0))

        self.bf_result2 = customtkinter.CTkLabel(self.bf_frame, wraplength=300,text="", font=customtkinter.CTkFont(size=14, weight="normal"))
        self.bf_result2.grid(row=1, column=0, sticky='se', pady=0, padx=(15,0))
        self.bf_result2_value = customtkinter.CTkLabel(self.bf_frame, wraplength=300, text="",font=customtkinter.CTkFont(size=14, weight="normal"))
        self.bf_result2_value.grid(row=1, column=1, sticky='w', pady=0, padx=(10,0))

        self.bf_result3 = customtkinter.CTkLabel(self.bf_frame, wraplength=300, text="",font=customtkinter.CTkFont(size=12, weight="normal"))
        self.bf_result3.grid(row=0, columnspan = 2, sticky='s', pady=(0,10), padx=0)

        self.dnc_frame.grid_rowconfigure((0), weight=1)
        self.dnc_frame.grid_columnconfigure((1), weight=1)

        self.dnc_result1 = customtkinter.CTkLabel(self.dnc_frame, wraplength=300, text="", font=customtkinter.CTkFont(size=14, weight="normal"))
        self.dnc_result1.grid(row=2, column=0, sticky='ne', pady=(0,10), padx=(15, 0))
        self.dnc_result1_value = customtkinter.CTkLabel(self.dnc_frame, wraplength=300, text="",font=customtkinter.CTkFont(size=14, weight="normal"))
        self.dnc_result1_value.grid(row=2, column=1, sticky='w', pady=(0,10), padx=(10,0))

        self.dnc_result2 = customtkinter.CTkLabel(self.dnc_frame, wraplength=300,text="", font=customtkinter.CTkFont(size=14, weight="normal"))
        self.dnc_result2.grid(row=1, column=0, sticky='se', pady=0, padx=(15,0))
        self.dnc_result2_value = customtkinter.CTkLabel(self.dnc_frame, wraplength=300, text="",font=customtkinter.CTkFont(size=14, weight="normal"))
        self.dnc_result2_value.grid(row=1, column=1, sticky='w', pady=0, padx=(10,0))

        self.dnc_result3 = customtkinter.CTkLabel(self.dnc_frame, wraplength=300, text="",font=customtkinter.CTkFont(size=12, weight="normal"))
        self.dnc_result3.grid(row=0, columnspan = 2, sticky='s', pady=(0,10), padx=0)

        self.comp_frame.grid_rowconfigure((0), weight=1)
        self.comp_frame.grid_columnconfigure((1), weight=1)

        self.comp_result1 = customtkinter.CTkLabel(self.comp_frame, wraplength=200, text="", font=customtkinter.CTkFont(size=13, weight="normal"))
        self.comp_result1.grid(row=0, column=0, sticky='se', pady=(10,0), padx=(10,0))
        self.comp_result1_value = customtkinter.CTkLabel(self.comp_frame, wraplength=200, text="", font=customtkinter.CTkFont(size=13, weight="normal"))
        self.comp_result1_value.grid(row=0, column=1, sticky='sw', pady=(10,0), padx=(10,0))

        self.comp_result2 = customtkinter.CTkLabel(self.comp_frame, wraplength=200, text="", font=customtkinter.CTkFont(size=13, weight="normal"))
        self.comp_result2.grid(row=1, column=0, sticky='ne', pady=(0,30), padx=(10,0))
        self.comp_result2_value = customtkinter.CTkLabel(self.comp_frame, wraplength=200, text="", font=customtkinter.CTkFont(size=13, weight="normal"))
        self.comp_result2_value.grid(row=1, column=1, sticky='nw', pady=(0,30), padx=(10,0))


    def run(self):
        points = np.empty((0), dtype=point)

        for i in range(int(self.entry_number.get())):
            val = np.empty(int(self.entry_dimensi.get()), dtype=float)
            for j in range(int(self.entry_dimensi.get())):
                val[j] = rand.uniform(-1000, 1000)
            points = np.append(points, point(int(self.entry_dimensi.get()), val))

        startBF = t.perf_counter() 
        closestCoupleBF, numBF = bruteForce(points)
        stopBF = t.perf_counter()

        startDnC = t.perf_counter()
        closestCoupleDnC, numDnC = divideConquer(quicksort(points))
        stopDnC = t.perf_counter()

        timeDnC = stopDnC-startDnC
        self.timeRes_dnc_label.configure(text="{:.6f} detik".format(timeDnC))
        timeBF = stopBF-startBF
        self.timeRes_bf_label.configure(text="{:.6f} detik".format(timeBF))

        self.display(points, closestCoupleDnC)
        self.detailResult(closestCoupleDnC, closestCoupleBF, numDnC, numBF, timeDnC, timeBF)
    
    def display(self, arrayOfPoint : list[point], pair : couple):
        if (self.entry_dimensi.get() == "3"):
            self.ax.clear()
            self.ax = self.fig.add_subplot(111, projection='3d')
            for point in arrayOfPoint:
                xp = point.value[0]
                yp = point.value[1]
                zp = point.value[2]
                if (point == pair.point1 or point == pair.point2):
                    self.ax.scatter(xp,yp,zp, marker='o', c='red')
                else:
                    self.ax.scatter(xp,yp,zp, marker='o', c='blue')

            self.ax.set_xlabel('SUMBU-X')
            self.ax.set_ylabel('SUMBU-Y')
            self.ax.set_zlabel('SUMBU-Z')

            self.canvas.draw()
            
        elif (self.entry_dimensi.get() == "2"):
            self.ax.clear()
            self.ax = self.fig.add_subplot()
            for point in arrayOfPoint:
                xp = point.value[0]
                yp = point.value[1]
                if (point == pair.point1 or point == pair.point2):
                    self.ax.scatter(xp,yp, marker='o', c='red')
                else:
                    self.ax.scatter(xp,yp, marker='o', c='blue')
            self.ax.set_xlabel('SUMBU-X')
            self.ax.set_ylabel('SUMBU-Y')

            self.canvas.draw()

        elif (self.entry_dimensi.get() == "1"):
            self.ax.clear()
            self.ax = self.fig.add_subplot()
            static_y = 0
            for point in arrayOfPoint:
                xp = point.value[0]
                if (point == pair.point1 or point == pair.point2):
                    self.ax.scatter(xp, static_y, marker='o', c='red')
                else:
                    self.ax.scatter(xp, static_y, marker='o', c='blue')

            self.ax.set_xlabel('SUMBU-X')

            self.canvas.draw()
    
    def detailResult(self, dncPair: couple, bfPair: couple, numDnc: int, numBf: int, timeDnc: float, timeBf: float):
        self.bf_result3.configure(text="{0}".format(bfPair))
        self.bf_result2.configure(text="Euclidean Distance           :")
        self.bf_result1.configure(text="Number of Euclidean       :")
        self.bf_result2_value.configure(text="{0}".format(bfPair.distance))
        self.bf_result1_value.configure(text="{0}".format(numBf))

        self.dnc_result3.configure(text="{0}".format(dncPair))
        self.dnc_result2.configure(text="Euclidean Distance           :")
        self.dnc_result1.configure(text="Number of Euclidean       :")
        self.dnc_result2_value.configure(text="{0}".format(dncPair.distance))
        self.dnc_result1_value.configure(text="{0}".format(numDnc))

        self.comp_result1.configure(text="Operation Eff     :")
        self.comp_result1_value.configure(text="{0:.3f} %".format(((numBf-numDnc)/numBf)*100))

        self.comp_result2.configure(text="Time Eff             :")
        self.comp_result2_value.configure(text="{0:.3f} %".format(((timeBf-timeDnc)/timeBf)*100))