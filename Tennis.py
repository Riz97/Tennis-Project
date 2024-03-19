import tkinter as tk

window = tk.Tk()

window.geometry("600x600") #Dimensions of the window
window.title("Hello TkInter!") #Name of the window

window.resizable(False, False) #Not resizable by the user

window.configure(background="white") #Background color


#Execution function
if __name__ == "__main__": 
    window.mainloop()