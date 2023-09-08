# Library and Modules used 
from tkinter import *                                        # pip install tkinter==8.6
import customtkinter as ctk                                  # pip install customtkinter==4.6.3

def expTrackerPage() :

    # Defining Structure
    expTrac_page = Canvas( root, 
                        width = wid, height = hgt, 
                         bg = "black", highlightcolor = "#3c5390", 
                          borderwidth = 0 )
    expTrac_page.pack( fill = "both", expand = True )

    root.mainloop()

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
    
    expTrackerPage()