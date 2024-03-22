import tkinter as tk
from tkinter import filedialog
import csv
import pandas as pd
from tkinter import ttk

flag = 0

# Function to open a specific .csv file
def open_csv_file():
   file_path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
   df = pd.read_csv(file_path)
   df_list = df["tourney_name"].drop_duplicates().tolist()
   dropdown = ttk.Combobox(
   state="readonly",
   )
   dropdown["values"] = df_list #Tournament names
   dropdown.place(x=50, y=50)

   return df


 

# Create a Tkinter window
root = tk.Tk()
root.geometry("720x400")
root.title("Opening a .csv file using button")
# Create a button to open the .csv file
open_button = tk.Button(root, text="Open .csv File", command=open_csv_file)
open_button.pack()









# Start the Tkinter main loop to run the GUI application
root.mainloop() 