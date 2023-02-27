import tkinter
import tkinter.messagebox
import customtkinter

from dataType import point, couple
from bruteForce import bruteForce
from divideConquer import divideConquer
from main import generateRandom

#debug
import time as t

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    WIDTH = 1100
    HEIGHT = 580
    def __init__(self):
        super().__init__()
        # configure window
        self.title("Closest Pair in Multidimension")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.num = 100
        self.dim = 3

        self.sidebar_frame = customtkinter.CTkFrame(master=self, width=250, height=580 ,corner_radius=0)

        self.sidebar_frame.place(x=0, y=0, anchor="nw")
        self.logo_label = customtkinter.CTkLabel(master = self.sidebar_frame, 
                                                 text="Get Closest Pair", 
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(x=120, y=20, anchor="n")
 
        self.num_entry_label = customtkinter.CTkLabel(master = self.sidebar_frame, 
                                                  text="Jumlah Titik        :", anchor='w', 
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
        self.num_entry_label.place(x=20, y=100, anchor="w")

        self.num_entry = customtkinter.CTkEntry( master=self.sidebar_frame, width=60, placeholder_text="100")
        self.num_entry.place(x=170, y=100, anchor="w")

        self.dim_entry_label = customtkinter.CTkLabel(master = self.sidebar_frame, 
                                                  text="Jumlah Dimensi  :", anchor='w', 
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
        self.dim_entry_label.place(x=20, y=140, anchor="w")

        self.dim_entry = customtkinter.CTkEntry( master=self.sidebar_frame, width=60, placeholder_text="3")
        self.dim_entry.place(x=170, y=140, anchor="w")

        self.time_label1 = customtkinter.CTkLabel(master=self.sidebar_frame,
                                              text="BF Execution Time:",
                                              font=customtkinter.CTkFont(size=15, weight="bold"))  # font name and size in px
        self.time_label1.place(x=55, y=200, anchor="w")

        self.time_stamp1 = customtkinter.CTkLabel(master=self.sidebar_frame,
                                              text="00:00:00",
                                              font=customtkinter.CTkFont(size=15, weight="bold"))
        self.time_stamp1.place(x=90, y=230, anchor="w")

        self.time_label2 = customtkinter.CTkLabel(master=self.sidebar_frame,
                                              text="DnC Execution Time:",
                                              font=customtkinter.CTkFont(size=15, weight="bold"))  # font name and size in px
        self.time_label2.place(x=55, y=300, anchor="w")

        self.time_stamp2 = customtkinter.CTkLabel(master=self.sidebar_frame,
                                              text="00:00:00",
                                              font=customtkinter.CTkFont(size=15, weight="bold"))
        self.time_stamp2.place(x=90, y=330, anchor="w")

        self.generate_button = customtkinter.CTkButton(self.sidebar_frame, text="Generate", command=self.run)
        self.generate_button.place(x=120, y=500, anchor="n")

    def run(self):
        points = generateRandom(int(self.num_entry.get()), int(self.dim_entry.get()))
        
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

if __name__ == "__main__":
    app = App()
    app.mainloop()

        # # create main entry and button
        # self.entry_label = customtkinter.CTkLabel(master = self.sidebar_frame, 
        #                                           text="Jumlah Titik :", anchor='w', 
        #                                           font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.entry_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        # self.entry = customtkinter.CTkEntry( master=self.sidebar_frame, placeholder_text="100 (int)")
        # self.entry.grid(row=1, column=0, padx=20, pady=(100, 10))
        # self.entry_label2 = customtkinter.CTkLabel(master = self.sidebar_frame, 
        #                                            text="Jumlah Dimensi :", anchor='w', 
        #                                            font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.entry_label2.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.entry2 = customtkinter.CTkEntry(master=self.sidebar_frame, placeholder_text="3 (int)")
        # self.entry2.grid(row=2, column=0, padx=20, pady=(100, 20))
            
        # self.time_label = customtkinter.CTkLabel(master=self.sidebar_frame,
        #                                       text="Brute Force\n Execution Time:",
        #                                       font=customtkinter.CTkFont(size=15, weight="bold"))  # font name and size in px
        # self.time_label.grid(row=4, column=0, padx=5, pady=(10,10))

        # self.time_stamp = customtkinter.CTkLabel(master=self.sidebar_frame,
        #                                       text="00:00:00 us",
        #                                       font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.time_stamp.grid(row=4, column=0, padx=5, pady=(60, 10))

        # self.generate_button = customtkinter.CTkButton(self.sidebar_frame)
        # self.generate_button.grid(row=5, column=0, padx=20, pady=20)