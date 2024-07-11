import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Combobox
import pymysql
from tkcalendar import DateEntry
import detail_page as dp



class ViewReportClass:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        self.window.title("Sale Report")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1 = self.w
        h1 = self.h
        self.window.minsize(w1, h1)
        # self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2))
        self.window.state('zoomed')

        # ----------------- widgets -----------------------------------------------------
        self.window.config(background=dp.bg_color2)
        self.headlbl = Label(self.window, text="Report ",
                             font=dp.myfont1, foreground=dp.fg_color, background=dp.bg_color2)

        self.l1=Label(self.window,text='From ',font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2)
        self.l2=Label(self.window,text='to',font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2)
        self.l3=Label(self.window,text='Total Data',font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2)


        from datetime import date
        today = date.today()
        self.t1 = DateEntry(self.window, width=20, foreground='white', borderwidth=2, date_pattern='y-mm-dd',
                            state="readonly",font=dp.myfont1,background=dp.bg_color2)
        self.t2 = DateEntry(self.window, width=20, foreground='white',borderwidth=2, date_pattern='y-mm-dd',
                            state="readonly",font=dp.myfont1,background=dp.bg_color2)
        self.t3=Label(self.window,text='0',font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2)

        #--------table----------
        self.tablearea = Frame(self.window )
        scrollbarx = Scrollbar(self.tablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tablearea, orient=VERTICAL)
        # srno	year	showroom_price	km_drived	previous_owner	fuel_type	seller_type	transmission	price	sold_on

        self.mytable = Treeview(self.tablearea,height=20,columns=['a','b','c','d','e','f','g','h','i'],
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbarx.config(command=self.mytable.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.config(command=self.mytable.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        # 'distance_from_home', 'distance_from_last_transaction', 'ratio_to_median_purchase_price',
        # 'repeatretailer', 'chip', 'pin_number', 'onlineorder', 'date', 'prediction_output'
        self.mytable.heading('a',text=' distance_from_home')
        self.mytable.heading('b',text='distance_from_last_transaction')
        self.mytable.heading('c',text='ratio_to_median_purchase_price')
        self.mytable.heading('d',text='repeatretailer')
        self.mytable.heading('e',text='chip')
        self.mytable.heading('f',text='pin_number')
        self.mytable.heading('g',text='onlineorder')
        self.mytable.heading('h',text='date')
        self.mytable.heading('i',text='prediction_output')

        self.mytable['show']='headings'
        self.mytable.column("#1", width=150, anchor='center')
        self.mytable.column("#2", width=170, anchor='center')
        self.mytable.column("#3", width=185, anchor='center')
        self.mytable.column("#4", width=130, anchor='center')
        self.mytable.column("#5", width=100, anchor='center')
        self.mytable.column("#6", width=110, anchor='center')
        self.mytable.column("#7", width=100, anchor='center')
        self.mytable.column("#8", width=100, anchor='center')
        self.mytable.column("#9", width=250, anchor='center')

        self.mytable.pack()


        #------ buttons---------
        self.b1=Button(self.window,text='Search',font=dp.myfont1, foreground=dp.fg_color,background=dp.bg_color2,command=lambda :self.fetchalldata(by='date'))
        # self.b2=Button(self.window,text='Print',font=dp.myfont1, foreground=dp.fg_color,background=dp.bg_color2,command=self.getPrintout)

        #---------------placements-----------------
        x1 = 160
        y1 = 100
        ydiff = 45
        xdiff = 150
        wigdet_width = 200
        t_diff = xdiff + xdiff + xdiff + xdiff
        upper_btn_x = x1 + xdiff + xdiff + 55
        btn_low_width = 120
        v_diff=600
        go_side=0
        self.headlbl.place(x=0, y=0,width=w1,height=70)

        self.l1.place(x=x1,y=y1)
        self.t1.place(x=x1+(xdiff*1),y=y1,width=wigdet_width)
        self.l2.place(x=x1+(xdiff*3),y=y1)
        self.t2.place(x=x1+(xdiff*4),y=y1,width=wigdet_width)
        self.b1.place(x=x1+(xdiff*5)+70,y=y1,width=btn_low_width,height=31)

        y1 += ydiff
        self.tablearea.place(x=x1-go_side, y=y1)

        y1=v_diff
        self.l3.place(x=x1,y=y1)
        self.t3.place(x=x1+(xdiff*1),y=y1,width=wigdet_width)
        # bw=200
        # self.b2.place(x=self.w/2-bw,y=y1,width=bw)

        self.clearpage()
        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='credit_card_fraud_detection', user='root', password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error in Database Connection : \n" + str(e), parent=self.window)

    def clearpage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)

    def fetchalldata(self,by):
        self.databaseConnection()
        try:
            myqry='select * from prediction_page  where date between %s and %s'
            self.curr.execute(myqry ,(self.t1.get(),self.t2.get()))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            total_data=len(data)
            self.print_data=[]
            if data:
               for row in data:
                   if row[8]=="[1.]":
                        message="There is higher chance of having Fraud Transaction"
                   else:
                       message="Congratulation you are away from fraud Transaction"
                   d1=[row[0],row[1],row[2],row[3],row[5],row[6],row[7],message]
                   d2=[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],message]
                   self.print_data.append(d1)
                   self.mytable.insert('', END, values=d2)
               self.t3.config(text=str(total_data))
            else:
                messagebox.showwarning("No record", "No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error","Error while Searching of record\n\n"+str(e),parent=self.window)

    # def getPrintout(self):
    #     pdf = Report1PDF()
    #     pdf.foot_msg1 = "Total Data = "+self.t3['text']
    #     heading = "Fraud  Report"
    #     col_heading = ['distance_from_home','distance_from_last_transaction','ratio_to_median_purchase_price',
    #                    'repeatretailer','chip','pin_number','onlineorder','date','prediction_output']
    #
    #     pdf.print_page(heading, col_heading, self.print_data)
    #     pdf.output('report1.pdf')
    #     os.system('report1.pdf ')


if __name__ == '__main__':
    window = Tk()
    ViewReportClass(window)
    window.mainloop()