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

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.result = tk.StringVar()
        self.result.set("0")
        self.entry = tk.Entry(master, textvariable=self.result, width=20, font=("Arial", 20), bd=5, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        row = 1
        col = 0
        for button in buttons:
            if col == 4:
                col = 0
                row += 1
            tk.Button(self.master, text=button, width=5, height=2, font=("Arial", 20),
                      command=lambda x=button: self.click_button(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
    
    def click_button(self, key):
        if key == "=":
            try:
                result = str(eval(self.result.get()))
            except:
                result = "Error"
            self.result.set(result)
        elif key == "C":
            self.result.set("0")
        elif key == "CE":
            self.result.set(self.result.get()[:-1])
        else:
            if self.result.get() == "0":
                self.result.set(key)
            else:
                self.result.set(self.result.get() + key)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()