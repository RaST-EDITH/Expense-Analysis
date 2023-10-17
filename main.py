# Library and Modules used 
import os                                                    # pip install os ( In case if not present )
import numpy as np                                           # pip install numpy ( In case if not present )
import pandas as pd                                          # pip install pandas==1.4.3
import openpyxl as oxl                                       # pip install openpyxl==3.0.10
from tkinter import *                                        # pip install tkinter==8.6
import customtkinter as ctk                                  # pip install customtkinter==4.6.3
import matplotlib.pyplot as plt                              # pip install matplotlib==3.4.3
from PIL import Image ,ImageTk                               # pip install pillow==9.3.0
from datetime import datetime, date
from tkinter.messagebox import showerror, showinfo

class ExpenseTracker :

    def __init__(self) :

        ctk.set_appearance_mode( "dark" )
        ctk.set_default_color_theme( "dark-blue" )
        self.width = 1200
        self.height = 700
        self.root = ctk.CTk()
        self.root.title( "Expense Analysis" )
        self.root.iconbitmap( os.path.join( os.getcwd(), "Background\coin.ico" ))
        self.root.geometry( "1200x700+200+80" )
        self.root.resizable( False, False )
        self.count = [1,2]
        self.path = os.path.join( os.getcwd(), "Sheet\ExpenseSheet.xlsx")
        self.first_back_image = self.Imgo( os.path.join( os.getcwd(), "Background\Firstpage.jpg" ), 1498, 875)
        self.first_front_image = self.Imgo( os.path.join( os.getcwd(), "Background\Firstdesign.jpg" ), 300, 300)
        self.second_back_image = self.Imgo( os.path.join( os.getcwd(), "Background\SecondPage.jpg" ), 1498, 875)
        self.third_back_image = self.Imgo( os.path.join( os.getcwd(), "Background\ThirdPage.jpg" ), 1498, 875)
        self.pie1_img = self.Imgo( os.path.join( os.getcwd(), "try1.jpg" ), 150, 150 )
        self.pie2_img = self.Imgo( os.path.join( os.getcwd(), "month1.jpg" ), 150, 150 )
        self.bar1_img = self.Imgo( os.path.join( os.getcwd(), "month1.jpg" ), 150, 150 )
        self.bar2_img = self.Imgo( os.path.join( os.getcwd(), "month1.jpg" ), 150, 150 )
        self.back = self.Imgo( os.path.join( os.getcwd(), "Background\logout.png" ), 35, 35 )

    def change( self, can, page) :

        # Switching canvas
        can.destroy()
        page()

    def Imgo( self, file, w, h ) :

        # Image processing
        img = Image.open(file)
        pht = ImageTk.PhotoImage( img.resize((w,h), Image.Resampling.LANCZOS ))
        return pht

    def pieShow( self, data ) :

        if data["Status"] :

            title = plt.title(  f'{data["Month"]} Expenses - Rs {data["Total"]}')
            title.set_ha("center")
            plt.gca().axis("equal")
            explode = [0.05]*len(data["Y"])
            pie = plt.pie( data["X"], labels = data["X"], explode = explode, shadow = True, autopct = '%.2f%%' )
            plt.legend( labels = data["Y"], bbox_to_anchor=(0,0), loc = "lower left", bbox_transform = plt.gcf().transFigure )
            plt.show()
        
        else :
            showerror( title = "Empty Records", message = "No Data Found")

    def barShow( self, data, flag ) :

        w = 0.5
        c = 0
        exp_bar, req_months = data
        colors = [
            '#FF6B6B', '#6B4226', '#6AB04A', '#F9A03F', '#F7DB4F',
            '#F7665A', '#48A9A6', '#F4A261', '#FFD700', '#F4A261',
            '#58B19F', '#F19066', '#9A8C98', '#4B778D', '#45ADA8',
            '#A85183', '#FFD700', '#CC8E35', '#FFCB77', '#68B0AB',
            '#CB769E', '#FF6B6B', '#577590', '#40C9A2', '#8A5E9F'
        ]
        if flag == 1 :
            x_place = np.arange( 1, 4*5, 5)
            label = []
            for i in exp_bar.keys() :
                if i !="Total" :
                    plt.bar( x_place + c*w, exp_bar[i], width = w, color = colors[(c*3)%25] )
                    c = c+1
                    label.append(i)
            plt.xticks( x_place + (c-1)*w/2, req_months )
            plt.legend( labels = label )
        
        else :
            x_place = np.arange( 1, 5)
            plt.bar( x_place, exp_bar["Total"], width = w, color = "#ee5160" )
            plt.xticks( x_place, req_months )
        
        plt.xlabel("Months")
        plt.ylabel("Expense Amount")
        plt.title("Previous Months Expense Chart")
        plt.show()

    def expenseAnalysis( self ) :

        sheet = pd.read_excel( pd.ExcelFile( self.path ), 'Expense_Sheet')
        column = sheet.columns
        all_months = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April', 
            5: 'May', 6: 'June', 7: 'July', 8: 'August', 
            9: 'September', 10: 'October', 11: 'November', 12: 'December'
        }

        curr_month = int(date.today().strftime("%m%Y"))
        months = sheet[column[4]].unique()
        req_months = {}

        if len(months) >= 4 :
            months = months[-1:-5:-1]
            for i in all_months.keys() :
                if ( date.today().strftime("%B") == all_months[i] ) :
                    k = i
                    break
            for i in range(4) :
                req_months[months[i]] = all_months[k]
                k = ( k+11 )%12

        else :
            months = months[::-1]
            for i in all_months.keys() :
                if ( date.today().strftime("%B") == all_months[i] ) :
                    k = i
                    break
            for i in range(len(months)) :
                req_months[months[i]] = all_months[k]
                k = ( k+11 )%12
        
        # Current Month
        mon_res = ( sheet[column[4]] == months[0] )
        unq_res = sheet[mon_res][column[1]].unique()
        exp_mon_1 = {}
        exp = [exp_mon_1]
        for i in unq_res :
            res = ( sheet[column[1]] == i ) & mon_res
            exp_mon_1[i] = sheet[res][column[2]].sum()
        
        # Pie Chart-1 Data
        pie_1_data ={
            "Status" : True,
            "Month" : str(req_months[months[0]]),
            "Total" : str(sheet[mon_res][column[2]].sum()),
            "X" : exp_mon_1.values(),
            "Y" : exp_mon_1.keys()
        }
        
        # Pie Chart-2 Data
        pie_2_data ={
            "Status" : False
        }
        if ( len(months) > 1 ) :

            # Previous Month
            mon_res = ( sheet[column[4]] == months[1] )
            unq_res = sheet[mon_res][column[1]].unique()
            exp_mon_2 = {}
            exp.append(exp_mon_2)
            for i in unq_res :
                res = ( sheet[column[1]] == i ) & mon_res
                exp_mon_2[i] = sheet[res][column[2]].sum()
            
            pie_2_data ={
                "Status" : True,
                "Month" : str(req_months[months[1]]),
                "Total" : str(sheet[mon_res][column[2]].sum()),
                "X" : exp_mon_2.values(),
                "Y" : exp_mon_2.keys()
            }

            if ( len(months) > 2 ) :

                # Third Month
                mon_res = ( sheet[column[4]] == months[2] )
                unq_res = sheet[mon_res][column[1]].unique()
                exp_mon_3 = {}
                exp.append(exp_mon_3)
                for i in unq_res :
                    res = ( sheet[column[1]] == i ) & mon_res
                    exp_mon_3[i] = sheet[res][column[2]].sum()
                
                if ( len(months) > 3 ) :

                    # Fourth Month
                    mon_res = ( sheet[column[4]] == months[3] )
                    unq_res = sheet[mon_res][column[1]].unique()
                    exp_mon_4 = {}
                    exp.append(exp_mon_4)
                    for i in unq_res :
                        res = ( sheet[column[1]] == i ) & mon_res
                        exp_mon_4[i] = sheet[res][column[2]].sum()
        
        # All Month Data
        exp_bar = { "Total" : [] }
        
        for a in exp :
            for i in a.keys() :
                exp_bar[i] = []
        
        for i in range( len(exp) ) :
            exp_bar["Total"].append( sum(list(exp[i].values())) )
            for x in exp_bar.keys() :
                if x in exp[i].keys() :
                    exp_bar[x].append(exp[i][x])
                elif x != "Total" :
                    exp_bar[x].append(0)

        for i in exp_bar.keys() :
            if ( len(exp_bar["Total"]) != len(exp_bar[i]) ) :
                exp_bar[i].extend([0]*(len(exp_bar["Total"]) - len(exp_bar[i])))

        return [ pie_1_data, pie_2_data, ( exp_bar, req_months.values() ) ]

    def updateExpSheet(self) :

        expense_sheet = pd.read_excel( pd.ExcelFile( self.path ), 'Expense_Sheet')
        row, col = expense_sheet.shape
        
        wb = oxl.load_workbook( self.path )
        sheet_xl = wb['Expense_Sheet']
        sheet_xl[f"A{row+2}"].value = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        sheet_xl[f"B{row+2}"].value = self.data["Category"]
        sheet_xl[f"C{row+2}"].value = self.data["Amount"]
        sheet_xl[f"D{row+2}"].value = self.data["Comment"]
        sheet_xl[f"E{row+2}"].value = int(date.today().strftime("%m%Y"))

        try :
            wb.save( self.path )

            temp_sheet = pd.read_excel( pd.ExcelFile( self.path ), 'Expense_Sheet')
            temp_column = temp_sheet.columns
            mon = int(date.today().strftime("%m%Y"))
            res_cat = ( temp_sheet[temp_column[1]] == self.data["Category"] ) & ( temp_sheet[temp_column[4]] == mon )
            res_mon = ( temp_sheet[temp_column[4]] == mon )

            self.data["Incat"], self.data["Total"] = temp_sheet[res_cat][temp_column[2]].sum(), temp_sheet[res_mon][temp_column[2]].sum()
            return 1 
        
        except :
            showerror( title = "Open File", message = "Close File in Background" )
        
        return 0

    def updateExp( self, value, area ) :

        rst = value.split()
        self.data = {
            "Amount" : 0,
            "Category" : "",
            "Comment" : "",
            "Total" : 0,
            "Incat" : 0
        }

        if ( len(rst) >= 2 and ( rst[0].isnumeric() or rst[1].isnumeric() ) ) :
            if rst[0].isnumeric() :
                self.data["Amount"] = int(rst[0])
                self.data["Category"] = rst[1].capitalize()

            else :
                self.data["Amount"] = int(rst[1])
                self.data["Category"] = rst[0].capitalize()
            
            if( len(rst) > 2 ) :
                self.data["Comment"] = " ".join(rst[2:])

            try :

                if self.updateExpSheet() :
                    show_val = " "*( 138 - int(1.8*len(value) ) )
                    show_val = show_val + value
                    final = f'Saved { self.data["Amount"] } in category { self.data["Category"] }\n'
                    final = final + f'Total in category { self.data["Category"] } : { self.data["Incat"] }\n'
                    final = final + f'This month : { self.data["Total"] }\n'

                    area.configure( state = "normal")
                    area.insert( f"{self.count[0]}.0", str(show_val)+'\n' )
                    area.insert( f"{self.count[1]}.0", final )
                    area.configure( state = "disabled")
                    self.count[0] += 2 + 2
                    self.count[1] += 2 + 2
            
            except :
                showerror( message = "Invalid Entry!", title = "Invalid")
        
        else :
            showerror( message = "Invalid Entry!!", title = "Invalid")

    def expenseAnalysisPage(self) :

        data_1, data_2, bar_data = self.expenseAnalysis()

        # Defining Structure
        expAnaly_page = Canvas( self.root, 
                                 width = self.width, height = self.height, 
                                  bg = "black", highlightcolor = "#3c5390", 
                                   borderwidth = 0 )
        expAnaly_page.pack( fill = "both", expand = True )

        # Background Image
        expAnaly_page.create_image( 0, 0, image = self.third_back_image , anchor = "nw")

        # Heading
        expAnaly_page.create_text( 530, 132, text = "Expense Analysis", 
                                font = ( "Georgia", 42, "bold" ), fill = "#ec1c24" )

        # Pie 1 Button
        pie1_bt = ctk.CTkButton( master = expAnaly_page, 
                                  text = "Current Month", text_font = ( "Georgia", 20 ), 
                                   width = 200, height = 200, corner_radius = 18,
                                    bg_color = "#fcd7ab", fg_color = "#f68207", 
                                     hover_color = "#f68207", text_color = "white",
                                      border_width = 5, border_color = "white",
                                       image = self.pie1_img, compound = "top", 
                                        command = lambda : self.pieShow( data_1 ) )
        pie1_bt_win = expAnaly_page.create_window( 150, 220, anchor = "nw", window = pie1_bt )

        # Pie 2 Button
        pie2_bt = ctk.CTkButton( master = expAnaly_page, 
                                  text = "Previous Month", text_font = ( "Georgia", 20 ), 
                                   width = 200, height = 200, corner_radius = 18,
                                    bg_color = "#fcd7ab", fg_color = "#f68207", 
                                     hover_color = "#f68207", text_color = "white",
                                      border_width = 5, border_color = "white",
                                       image = self.pie2_img, compound = "top",  
                                        command = lambda : self.pieShow( data_2 ) )
        pie2_bt_win = expAnaly_page.create_window( 500, 220, anchor = "nw", window = pie2_bt )

        # Bar 1 Button
        Bar1_bt = ctk.CTkButton( master = expAnaly_page, 
                                  text = "Past Months\nOverlook", text_font = ( "Georgia", 20 ), 
                                   width = 200, height = 200, corner_radius = 18,
                                    bg_color = "#fcd7ab", fg_color = "#c65d01", 
                                     hover_color = "#f68207", text_color = "white",
                                      border_width = 5, border_color = "white", 
                                       image = self.bar1_img, compound = "top",
                                        command = lambda : self.barShow( bar_data, 2 ) )
        Bar1_bt_win = expAnaly_page.create_window( 350, 510, anchor = "nw", window = Bar1_bt )

        # Bar 2 Button
        Bar2_bt = ctk.CTkButton( master = expAnaly_page, 
                                  text = "Past Months\nDetailed", text_font = ( "Georgia", 20 ), 
                                   width = 200, height = 200, corner_radius = 18,
                                    bg_color = "#fcd7ab", fg_color = "#f68207", 
                                     hover_color = "#f68207", text_color = "white",
                                      border_width = 5, border_color = "white", 
                                       image = self.bar2_img, compound = "top", 
                                        command = lambda : self.barShow( bar_data, 1) )
        Bar2_bt_win = expAnaly_page.create_window( 700, 510, anchor = "nw", window = Bar2_bt )

        # Return Button
        back_bt = ctk.CTkButton( master = expAnaly_page, 
                                  image = self.back, text = None, 
                                   width = 45, height = 45, corner_radius = 23, 
                                    bg_color = "#fcd7ab", fg_color = "red", 
                                     hover_color = "#ff5359", border_width = 0, 
                                      command = lambda : self.change( expAnaly_page, self.expEntryPage ))
        back_bt_win = expAnaly_page.create_window( 30, 20, anchor = "nw", window = back_bt )

        self.root.mainloop()

    def expEntryPage(self) :

        # Defining Structure
        expTrac_page = Canvas( self.root, 
                                width = self.width, height = self.height, 
                                 bg = "black", highlightcolor = "#3c5390", 
                                  borderwidth = 0 )
        expTrac_page.pack( fill = "both", expand = True )

        # Background Image
        expTrac_page.create_image( 0, 0, image = self.second_back_image , anchor = "nw")

        # Heading
        expTrac_page.create_text( 530, 130, text = "Expense Tracker", 
                                font = ( "Georgia", 42, "bold" ), fill = "#ec1c24" )

        # Expense Entry Box
        expense = ctk.CTkEntry( master = expTrac_page, 
                                 placeholder_text = "Enter Expense with Specification", text_font = ( "Georgia", 20 ), 
                                  width = 600, height = 30, corner_radius = 14,
                                   placeholder_text_color = "#666666", text_color = "#191919", 
                                    fg_color = "#e1f5ff", bg_color = "#fcd7ab", 
                                      border_color = "white", border_width = 3)
        expense_win = expTrac_page.create_window( 190, 200, anchor = "nw", window = expense )

        # Status box added
        status_box = ctk.CTkTextbox( expTrac_page, 
                                        width = 950, height = 400, 
                                         bg_color = "#fcd7ab", fg_color = "#fecc8f",
                                          border_width = 5, border_color = "white",
                                            text_font = ( "Georgia", 20 ), text_color = "#654033",
                                             corner_radius = 15, state = "disabled"  )
        status_box.place( x = 115, y = 220, anchor = "nw")

        expense.bind('<Return>', lambda event = None : self.updateExp( expense.get(), status_box ) )
        
        # Insert Button
        insert_bt = ctk.CTkButton( master = expTrac_page, 
                                    text = "Insert", text_font = ( "Georgia", 20 ), 
                                     width = 100, height = 40, corner_radius = 18,
                                      bg_color = "#fcd7ab", fg_color = "red", 
                                       hover_color = "#ff5359", border_width = 0,
                                        text_color = "white", 
                                         command = lambda : self.updateExp( expense.get(), status_box ) )
        insert_bt_win = expTrac_page.create_window( 960, 200-1, anchor = "nw", window = insert_bt )

        # Analysis Button
        analysis_bt = ctk.CTkButton( master = expTrac_page, 
                                      text = "Expense Analysis", text_font = ( "Georgia", 20 ), 
                                       width = 100, height = 40, corner_radius = 18,
                                        bg_color = "#fcd7ab", fg_color = "red", 
                                         hover_color = "#ff5359", border_width = 0, 
                                          text_color = "white",
                                           command = lambda : self.change( expTrac_page, self.expenseAnalysisPage ) )
        analysis_bt_win = expTrac_page.create_window( 930, 790, anchor = "nw", window = analysis_bt )

        # Return Button
        back_bt = ctk.CTkButton( master = expTrac_page, 
                                  image = self.back, text = None, 
                                   width = 45, height = 45, corner_radius = 23, 
                                    bg_color = "#fcd7ab", fg_color = "red", 
                                     hover_color = "#ff5359", border_width = 0, 
                                      command = lambda : self.change( expTrac_page, self.firstPage ))
        back_bt_win = expTrac_page.create_window( 30, 20, anchor = "nw", window = back_bt )

        self.root.mainloop()

    def firstPage(self) :

        # Defining Structure
        first_page = Canvas( self.root, 
                              width = self.width, height = self.height, 
                               bg = "black", highlightcolor = "#3c5390", 
                                borderwidth = 0 )
        first_page.pack( fill = "both", expand = True )

        # Background Image
        first_page.create_image( 0, 0, image = self.first_back_image , anchor = "nw")
        first_page.create_image( 500,360, image = self.first_front_image , anchor = "nw")

        # Heading
        first_page.create_text( 400, 119, text = "Expense Tracker", 
                                font = ( "Georgia", 42, "bold" ), fill = "#ec1c24" )
        first_page.create_text( 280, 500, text = "A personalized\nexpense monitoring\napplication\nwith features like\nexpense analysis and\nvisualization using\nbar graphs\nand pie charts.", 
                                font = ( "Georgia", 20), fill = "white" )

        # Next Page Button
        next_bt = ctk.CTkButton( master = first_page, 
                                  text = "Let's Go ->", text_font = ( "Tahoma", 20 ), 
                                   width = 100, height = 40, corner_radius = 18,
                                    bg_color = "#fecc8f", fg_color = "#ec1c24", 
                                     hover_color = "#ff5359", border_width = 0,
                                      text_color = "white",
                                       command = lambda : self.change( first_page, self.expEntryPage ) )
        next_bt_win = first_page.create_window( 320, 720, anchor = "nw", window = next_bt )

        self.root.mainloop()

if __name__ == "__main__" :

    exp_class = ExpenseTracker()
    exp_class.firstPage()
