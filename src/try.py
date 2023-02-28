import tkinter
import tkinter.messagebox
import customtkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from IO import IO, t, np, rand, bruteForce, divideConquer, display3D, display1D, display2D
from dataType import couple, point

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1295}x{720}")

        # configure grid layout (4x4)
        self.grid_columnconfigure((1,2,3,4,5,6,7), weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=480, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((4,7), weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="DUO RIZKY", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, columnspan=2, padx=0, pady=(20, 0))
        self.sub_label = customtkinter.CTkLabel(self.sidebar_frame, text="Closest Pair Finder", font=customtkinter.CTkFont(size=14, weight="normal"))
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



        # self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        # self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.run_button = customtkinter.CTkButton(self.sidebar_frame, text="Generate & Run", command=self.run)
        self.run_button.grid(row=8, column=0, columnspan=2, padx=20, pady=30, sticky="s")
        # self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        # self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        # self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
        #                                                                command=self.change_appearance_mode_event)
        # self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        # self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        # self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.vis_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.vis_frame.grid(row=0, column=1, columnspan=6, pady=0)

        self.fig = Figure(figsize=(12,5), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Create a canvas to display the plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.vis_frame)
        self.canvas.get_tk_widget().pack()

        self.terminal_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.terminal_frame.grid(row=1, column=1, columnspan=6, pady=0, sticky='nswe')
        self.terminal_frame.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1)
        self.terminal_frame.grid_rowconfigure((0,1,2), weight=1)

        self.bf_label = customtkinter.CTkLabel(self.terminal_frame,  text="Brute Force", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.bf_label.grid(row=0, column=0, columnspan=3, sticky='we', pady=5, padx=5)
        self.comp_label = customtkinter.CTkLabel(self.terminal_frame,  text="Comparison", font=customtkinter.CTkFont(size=20, weight="bold"))
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
        self.bf_frame.grid_columnconfigure((0), weight=1)
        self.bf_result = customtkinter.CTkLabel(self.bf_frame, wraplength=300, text='Hasil Brute Force', font=customtkinter.CTkFont(size=12, weight="normal"))
        self.bf_result.grid(row=0, column=0, sticky='', pady=10, padx=5)

        self.dnc_frame.grid_rowconfigure((0), weight=1)
        self.dnc_frame.grid_columnconfigure((0), weight=1)
        self.dnc_result = customtkinter.CTkLabel(self.dnc_frame, wraplength=300, text='Hasil Divide & Conquer', font=customtkinter.CTkFont(size=12, weight="normal"))
        self.dnc_result.grid(row=0, column=0, sticky='', pady=10, padx=5)

        self.comp_frame.grid_rowconfigure((0), weight=1)
        self.comp_frame.grid_columnconfigure((0), weight=1)
        self.comp_result = customtkinter.CTkLabel(self.comp_frame, wraplength=200, text='Hasil Comparison', font=customtkinter.CTkFont(size=12, weight="normal"))
        self.comp_result.grid(row=0, column=0, sticky='', pady=10, padx=5)


    def run(self):
        points = np.empty((0), dtype=point)

        for i in range(int(self.entry_number.get())):
            val = np.empty(int(self.entry_dimensi.get()), dtype=float)
            for j in range(int(self.entry_dimensi.get())):
                val[j] = rand.uniform(-1000, 1000)
            points = np.append(points, point(int(self.entry_dimensi.get()), val))

        startBF = t.time() 
        closestCoupleBF, numBF = bruteForce(points)
        stopBF = t.time()
        print("Brute Force : ", closestCoupleBF)
        print("number of euclidean op : ", numBF)
        print("Waktu BF : ", stopBF-startBF, " detik\n")

        startDnC = t.time()
        closestCoupleDnC, numDnC = divideConquer(sorted(points))
        stopDnC = t.time()
        print("DnC : ", closestCoupleDnC)
        print("number of Euclidean : ", numDnC)
        print("Waktu DnC : ", stopDnC-startDnC, " detik")

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
        self.bf_result.configure(text="Pair : {0}\nNumber of Euclidean : {1}\nEuclidean distance : {2}".format(bfPair, numBf, bfPair.distance))
        self.dnc_result.configure(text="Pair : {0}\nNumber of Euclidean : {1}\nEuclidean distance : {2}".format(dncPair, numDnc, dncPair.distance))
        self.comp_result.configure(text="Operation Efficiency : {0} %".format(((numBf-numDnc)/numDnc)*100))



if __name__ == "__main__":
    app = App()
    app.mainloop()