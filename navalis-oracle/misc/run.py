
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import os
import sys
from parse_lab_jsons import LabyrinthMap

SCRIPT_PATH = os.path.abspath(__file__)
sys.path.insert(0, ("\\".join([SCRIPT_PATH])))

# def on_select():
#     chosen_option = variable.get()
#     LabMap = LabyrinthMap()
#     LabMap.plot_map(lab_tier=chosen_option)



# # Variable to hold the selected option
# variable = tk.StringVar(root)
# variable.set("Choose Labyrinth Tier")  # default value

# # List of options for the drop-down menu
# options = ["Normal", "Cruel", "Merciless", "Uber"]



# # Button to confirm selection
# select_button = tk.Button(root, text="Select", command=on_select)
# select_button.pack(pady=5)

class ShowMap():
    def __init__(self, root):
        
        self.root = root

        # Initialize LabyrinthMap with the canvas
        self.map = LabyrinthMap(self.root)

        self.var = tk.StringVar(self.root)
        self.var.set("Choose Labyrinth Tier") 
        options = ["Normal", "Cruel", "Merciless", "Uber"]
        self.option_menu = tk.OptionMenu(self.root, self.var, *options, command=self.on_select)
        self.option_menu.pack(pady=10)

    def on_select(self):
        # self.map.plot(lab_tier=chosen_option)
        self.map.plot(self.var.get())


if __name__ == "__main__":

    # Create the main window
    root = tk.Tk()
    root.title("The Lord's Labyrinth")
    root.geometry("200x100")


    start = ShowMap(root)
    # Start the GUI event loop
    root.mainloop()