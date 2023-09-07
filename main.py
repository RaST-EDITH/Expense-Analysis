# Library and Modules used 
from tkinter import *                                        # pip install tkinter==8.6
import customtkinter as ctk                                  # pip install customtkinter==4.6.3

if __name__ == "__main__" :

    global root

    # Defining Main theme of all widgets
    ctk.set_appearance_mode( "dark" )
    ctk.set_default_color_theme( "dark-blue" )
    wid = 1200
    hgt = 700
    root = ctk.CTk()
    root.title( "Expense Analysis" )
    root.geometry( "1200x700+200+80" )
    root.resizable( False, False )
    root.mainloop()