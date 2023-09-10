# Library and Modules used 
from tkinter import *                                        # pip install tkinter==8.6
import customtkinter as ctk                                  # pip install customtkinter==4.6.3

class ExpenseTracker :

    def __init__(self) :

        ctk.set_appearance_mode( "dark" )
        ctk.set_default_color_theme( "dark-blue" )
        self.width = 1200
        self.height = 700
        self.root = ctk.CTk()
        self.root.title( "Expense Analysis" )
        self.root.geometry( "1200x700+200+80" )
        self.root.resizable( False, False )

    def expEntryPage(self) :

        # Defining Structure
        expTrac_page = Canvas( self.root, 
                                width = self.width, height = self.height, 
                                 bg = "black", highlightcolor = "#3c5390", 
                                  borderwidth = 0 )
        expTrac_page.pack( fill = "both", expand = True )

        # Heading
        expTrac_page.create_text( 700, 120, text = "Expense Tracker", 
                                font = ( "Book Antiqua", 45, "bold", "underline" ), fill = "#1c54df" )

        self.root.mainloop()

if __name__ == "__main__" :

    exp_class = ExpenseTracker()
    exp_class.expEntryPage()
