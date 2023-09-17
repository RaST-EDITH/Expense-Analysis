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

    def change( self, can, page) :

        # Switching canvas
        can.destroy()
        page()

    def expenseAnalysisPage(self) :

        data_1, data_2, bar_data = self.expenseAnalysis()

        # Defining Structure
        expAnaly_page = Canvas( self.root, 
                                 width = self.width, height = self.height, 
                                  bg = "black", highlightcolor = "#3c5390", 
                                   borderwidth = 0 )
        expAnaly_page.pack( fill = "both", expand = True )

        # Heading
        expAnaly_page.create_text( 700, 120, text = "Expense Analysis", 
                                font = ( "Book Antiqua", 45, "bold", "underline" ), fill = "#1c54df" )

        # Pie 1 Button
        pie1_bt = ctk.CTkButton( master = expAnaly_page, 
                                  text = "Current Month", text_font = ( "Tahoma", 20 ), 
                                   width = 100, height = 50, corner_radius = 18,
                                    bg_color = "black", fg_color = "red", 
                                     hover_color = "#ff5359", border_width = 0, 
                                      command = lambda : self.pieShow( data_1 ) )
        pie1_bt_win = expAnaly_page.create_window( 100, 200, anchor = "nw", window = pie1_bt )

        # Pie 2 Button
        pie2_bt = ctk.CTkButton( master = expAnaly_page, 
                                  text = "Previous Month", text_font = ( "Tahoma", 20 ), 
                                   width = 100, height = 50, corner_radius = 18,
                                    bg_color = "black", fg_color = "red", 
                                     hover_color = "#ff5359", border_width = 0, 
                                      command = lambda : self.pieShow( data_2 ) )
        pie2_bt_win = expAnaly_page.create_window( 400, 200, anchor = "nw", window = pie2_bt )

        # Bar 1 Button
        Bar1_bt = ctk.CTkButton( master = expAnaly_page, 
                                  text = "Previous Totals", text_font = ( "Tahoma", 20 ), 
                                   width = 100, height = 50, corner_radius = 18,
                                    bg_color = "black", fg_color = "red", 
                                     hover_color = "#ff5359", border_width = 0, 
                                      command = lambda : self.barShow( bar_data, 2 ) )
        Bar1_bt_win = expAnaly_page.create_window( 700, 200, anchor = "nw", window = Bar1_bt )

        # Bar 2 Button
        Bar2_bt = ctk.CTkButton( master = expAnaly_page, 
                                  text = "Previous Detailed", text_font = ( "Tahoma", 20 ), 
                                   width = 100, height = 50, corner_radius = 18,
                                    bg_color = "black", fg_color = "red", 
                                     hover_color = "#ff5359", border_width = 0, 
                                      command = lambda : self.barShow( bar_data, 1) )
        Bar2_bt_win = expAnaly_page.create_window( 1000, 200, anchor = "nw", window = Bar2_bt )

        # Return Button
        ret_bt = ctk.CTkButton( master = expAnaly_page, 
                                 text = "Back", text_font = ( "Tahoma", 20 ), 
                                  width = 100, height = 50, corner_radius = 18,
                                   bg_color = "black", fg_color = "red", 
                                    hover_color = "#ff5359", border_width = 0, 
                                     command = lambda : self.change( expAnaly_page, self.expEntryPage) )
        ret_bt_win = expAnaly_page.create_window( 30, 20, anchor = "nw", window = ret_bt )

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

        expense.bind('<Return>', lambda event = None : self.updateExp( expense.get(), status_box ) )
        
        # Insert Button
        insert_bt = ctk.CTkButton( master = expTrac_page, 
                                    text = "Insert", text_font = ( "Tahoma", 20 ), 
                                     width = 100, height = 40, corner_radius = 18,
                                      bg_color = "black", fg_color = "red", 
                                       hover_color = "#ff5359", border_width = 0, 
                                        command = lambda : self.updateExp( expense.get(), status_box ) )
        insert_bt_win = expTrac_page.create_window( 1030, 320-120, anchor = "nw", window = insert_bt )

        # Analysis Button
        analysis_bt = ctk.CTkButton( master = expTrac_page, 
                                      text = "Expense Analysis", text_font = ( "Tahoma", 20 ), 
                                       width = 100, height = 40, corner_radius = 18,
                                        bg_color = "black", fg_color = "red", 
                                         hover_color = "#ff5359", border_width = 0, 
                                          command = lambda : self.change( expTrac_page, self.expenseAnalysisPage ) )
        analysis_bt_win = expTrac_page.create_window( 610, 790, anchor = "nw", window = analysis_bt )

        self.root.mainloop()

if __name__ == "__main__" :

    exp_class = ExpenseTracker()
    exp_class.expEntryPage()
