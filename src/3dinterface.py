# import random
# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# from mpl_toolkits.mplot3d import Axes3D
# import time as t

# class MainWindow:
#     def __init__(self, master):
#         self.master = master
#         master.title("Divide And Conquer Closest Pair")

#         # Create a label and entry widget for the input
#         self.input_label = tk.Label(master, text="Masukkan banyak titik")
#         self.input_label.pack()
#         self.input_entry = tk.Entry(master)
#         self.input_entry.pack()

#         # Create a button to generate and plot the points
#         self.plot_button = tk.Button(master, text="Generate", command=self.plot)
#         self.plot_button.pack()

#         self.time_label= tk.Label(master, text=f"Execution Time : {0.00}")
#         self.time_label.pack()

#         # Create a 3D Matplotlib plot
#         self.fig = Figure(figsize=(8, 6), dpi=100)
#         self.ax = self.fig.add_subplot(111, projection='3d')

#         # Create a canvas to display the plot
#         self.canvas = FigureCanvasTkAgg(self.fig, master=root)
#         self.canvas.get_tk_widget().pack()

#     def plot(self):
#         # Get the input from the entry widget
#         num_points = int(self.input_entry.get())

#         start = t.time()
#         # Generate random points
#         xs = [random.random() for i in range(num_points)]
#         ys = [random.random() for i in range(num_points)]
#         zs = [random.random() for i in range(num_points)]

#         # Clear the previous plot
#         self.ax.clear()

#         # Plot the random points
#         self.ax.scatter(xs, ys, zs)
#         stop = t.time()
#         self.time_label.configure(text = f"{stop-start} detik")

#         # Redraw the canvas
#         self.canvas.draw()

# if __name__ == '__main__':
#     root = tk.Tk()
#     mainWindow = MainWindow(root)
#     root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

import numpy as np
import customtkinter

import time

start = time.time()
ss=time.time()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue") 

BACKGROUND_COLOR_OFF = "#7e69a7"
TOGGLE_COLOR_OFF = "#aaaaff"
COLOR1_OFF = "#655596"
COLOR2_OFF = "#57409f"
BLACK_OFF = "#333333"
BACKGROUND_COLOR_ON = "#f8f8fa"
TOGGLE_COLOR_ON = "#d2d4dc"
COLOR1_ON = "#e5e6eb"
COLOR2_ON = "#c0c2ce"
BLACK_ON = "#afafaf"
BLACK = "black"


class App(customtkinter.CTk):

    WIDTH = 1600
    HEIGHT = 1200

    def __init__(self):
        super().__init__()

        self.title("Closest Pair in Multidimension")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============
        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(9, weight=1)  # empty row as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Insert Your DataSet",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=5, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Upload DataSet",
                                                command=self.open_file_dataset)
        self.button_1.grid(row=1, column=0, pady=10, padx=20)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Insert Your Image",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=2, column=0, pady=5, padx=10)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Upload Image",
                                                command=self.open_file_image)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Camera",
                                                command=self.openCam)
        self.switch_1.grid(row=6, column=0, pady=10, padx=20)

        self.label_mode1 = customtkinter.CTkLabel(master=self.frame_left, text="Choose Camera :")
        self.label_mode1.grid(row=4, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_2 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=['0', '1', '2', '3'],
                                                        command=self.change_camera)
        self.optionmenu_2.grid(row=5, column=0, pady=10, padx=20)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Execution Time:",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_3.grid(row=7, column=0, pady=5, padx=10)

        self.label_4 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="00:00:00",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_4.grid(row=8, column=0, pady=5, padx=10)

        self.label_spacing = customtkinter.CTkLabel(master=self.frame_left,
                                                text="",
                                                text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_spacing.grid(row=9, column=0, pady=5, padx=10)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="",
                                                width=0,
                                                height=0)
        self.button_3.grid(row=10, column=0, pady=10, padx=20)

        self.label_5 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Result",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_5.grid(row=11, column=0, pady=5, padx=10)
        

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Download",
                                                command=self.formating_output_file)
        self.button_5.grid(row=12, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=13, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=14, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0,1), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.label_title = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Test Image",
                                              text_font=("Roboto Medium", -30))  # font name and size in px
        self.label_title.grid(row=1, column=0, pady=5, padx=10)
        self.label_title = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Closest Result",
                                              text_font=("Roboto Medium", -30))  # font name and size in px
        self.label_title.grid(row=1, column=1, pady=5, padx=10)
        
        self.frame_info1 = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info1.grid(row=4, column=0, columnspan=1, rowspan=4, pady=20, padx=20, sticky="nsew")
        self.image_label1 = customtkinter.CTkLabel(master=self.frame_info1, image=self.photo_input)
        self.image_label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.frame_info2 = customtkinter.CTkFrame(master=self.frame_right)

        self.frame_info2.grid(row=4, column=1, columnspan=1, rowspan=4, pady=20, padx=20, sticky="nsew")
        self.image_label2 = customtkinter.CTkLabel(master=self.frame_info2, image=self.photo_closest)
        self.image_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # set default values
        self.optionmenu_1.set("Light")
        self.optionmenu_2.set("0")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def saveFile(self):
        # Save file as
        file = filedialog.asksaveasfile(mode='w', defaultextension=".pdf")
        if file is None:
            return
        self.pdf_file = self.formating_output_file 
        self.pdf_file.save(file)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()