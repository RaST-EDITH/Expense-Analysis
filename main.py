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

    def change( can, page) :

        # Switching canvas
        can.destroy()
        page()

    def expenseAnalysisPage() :

        # Defining Structure
        expAnaly_page = Canvas( root, 
                                 width = self.width, height = self.height, 
                                  bg = "black", highlightcolor = "#3c5390", 
                                   borderwidth = 0 )
        expAnaly_page.pack( fill = "both", expand = True )

        self.root.mainloop()

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

        # Expense Entry Box
        expense = ctk.CTkEntry( master = expTrac_page, 
                                 placeholder_text = "Enter Expense", text_font = ( "Seoge UI", 20 ), 
                                  width = 550, height = 30, corner_radius = 14,
                                   placeholder_text_color = "#666666", text_color = "#191919", 
                                    fg_color = "#e1f5ff", bg_color = "black", 
                                     border_color = "white", border_width = 3)
        expense_win = expTrac_page.create_window( 325, 320-120, anchor = "nw", window = expense )

        # Status box added
        status_box = ctk.CTkTextbox( expTrac_page, 
                                        width = 880, height = 400, 
                                            text_font = ( "Seoge UI", 20 ), 
                                                state = "disabled"  )
        status_box.place( x = 150, y = 220, anchor = "nw")

        expense.bind('<Return>', lambda event = None : updateExp( expense.get(), status_box ) )
        
        # Insert Button
        insert_bt = ctk.CTkButton( master = expTrac_page, 
                                    text = "Insert", text_font = ( "Tahoma", 20 ), 
                                     width = 100, height = 40, corner_radius = 18,
                                      bg_color = "black", fg_color = "red", 
                                       hover_color = "#ff5359", border_width = 0, 
                                        command = lambda : updateExp( expense.get(), status_box ) )
        insert_bt_win = expTrac_page.create_window( 1030, 320-120, anchor = "nw", window = insert_bt )

        # Analysis Button
        analysis_bt = ctk.CTkButton( master = expTrac_page, 
                                      text = "Expense Analysis", text_font = ( "Tahoma", 20 ), 
                                       width = 100, height = 40, corner_radius = 18,
                                        bg_color = "black", fg_color = "red", 
                                         hover_color = "#ff5359", border_width = 0, 
                                          command = lambda : change( expTrac_page, expenseAnalysisPage ) )
        analysis_bt_win = expTrac_page.create_window( 610, 790, anchor = "nw", window = analysis_bt )

        self.root.mainloop()

if __name__ == "__main__" :

    exp_class = ExpenseTracker()
    exp_class.expEntryPage()
