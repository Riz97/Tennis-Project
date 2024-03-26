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
   df_list = df["winner_name"].drop_duplicates().tolist()
   sorted_list = sorted(df_list)
   dropdown = ttk.Combobox(
   state="readonly",
   )
   dropdown["values"] = sorted_list #Tournament names
   dropdown.place(x=50, y=50)

   printButton = tk.Button(root, text = "Select the player",command=printInput)
   printButton.place(x=200,y=50)  

   return df,dropdown

def printInput():
   inp = dropdown.get()
   print(inp)
   tree= ttk.Treeview(root,columns=4)
   tree.pack()


  
 

# Create a Tkinter window
root = tk.Tk()
root.geometry("720x400")
root.title("Tennis Players Statistics")


df,dropdown = open_csv_file()








# Start the Tkinter main loop to run the GUI application
root.mainloop() 