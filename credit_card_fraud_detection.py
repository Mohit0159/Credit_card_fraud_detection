from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


import pymysql as pymysql
from PIL import ImageTk, Image
import detail_page as dp
import joblib

import sklearn
# model = joblib.load('credit_card_')

model = joblib.load('credit_card_fraud_detection')

class frauddetectionPageClass:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        self.window.title("credit card fraud prdictor ")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1=self.w
        h1=self.h
        self.window.minsize(w1,h1)
        # self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2))
        self.window.state('zoomed')


        label_width=25

        self.window.config(background=dp.bg_color)

        self.headlbl = Label(self.window, text="Predict credit card fraud ",
                             font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2)

        self.l1 = Label(self.window, text="Distance from home",font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2,relief='ridge',width=label_width)
        # flat, groove, raised, ridge, solid, or sunken
        self.l2 = Label(self.window, text="Distance from last transaction ",font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2,width=label_width,relief='ridge')

        self.l3 = Label(self.window, text="Ratio to median purchase price ",font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2,width=label_width,relief='ridge')
        self.l4 = Label(self.window, text="Repeat Retailer",font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2,width=label_width,relief='ridge')
        self.l5 = Label(self.window, text="Used Chip",font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2,width=label_width,relief='ridge')
        self.l6 = Label(self.window, text="Used Pin Number ",font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2,width=dp.label_width,relief='ridge')
        self.l7 = Label(self.window, text="Online Order",font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2,width=label_width,relief='ridge')
        # self.l8 = Label(self.window, text="fraud", font=myfont1, foreground='#de90c0',
        #                 background=bg_color2)
        self.l8 = Label(self.window, text=" - - - - - ",font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2)

        # Entry box

        self.t1 = Entry(self.window,font=dp.myfont1,foreground=dp.fg_color)
        self.t2 = Entry(self.window,font=dp.myfont1,foreground=dp.fg_color)
        self.t3 = Entry(self.window,font=dp.myfont1,foreground=dp.fg_color)
        self.v1 = StringVar()
        self.c1 = Combobox(self.window, values=["Yes", "No"], textvariable=self.v1, state='readonly',
                           font=dp.myfont1, foreground=dp.fg_color)
        self.v1.set("Select Yes Or No")
        self.v2 = StringVar()
        self.c2 = Combobox(self.window, values=["Yes", "No"], textvariable=self.v2, state='readonly', font=dp.myfont1,
                           foreground=dp.fg_color)
        self.v2.set("Select Yes Or No")
        self.v3 = StringVar()
        self.c3 = Combobox(self.window, values=["Yes", "No"], textvariable=self.v3, state='readonly', font=dp.myfont1,
                           foreground=dp.fg_color)
        self.v3.set("Select Yes Or No")

        self.v4 = StringVar()
        self.c4 = Combobox(self.window, values=["Yes", "No"], textvariable=self.v4, state='readonly',
                           font=dp.myfont1, foreground=dp.fg_color )
        self.v4.set("Select Yes Or No")
        self.btn1 = Button(self.window, text="Predict ", font=dp.myfont1,
                           foreground=dp.fg_color, background=dp.bg_color2,command=self.predict)
        self.btn2 = Button(self.window, text="Reset", font=dp.myfont1,
                           foreground=dp.fg_color, background=dp.bg_color2,command=self.clearPage)
        self.ressize_w = 100
        self.ressize_h = 100
        self.responseimglbl = Label(self.window, background=dp.bg_color)
        cardsize_w = 500
        cardsize_h = 200

        self.cardimg1 = ImageTk.PhotoImage(Image.open("credit_card_PNG4.png").resize((cardsize_w, cardsize_h)))
        self.cardimglbl = Label(self.window, image=self.cardimg1, background=dp.bg_color)

        # ******** PLacing *************
        self.headlbl.place(x=0, y=0, width=w1, height=70)
        x1 = 40
        y1 = 100
        x_diff = 250
        y_diff = 50
        self.l1.place(x=x1, y=y1)
        self.t1.place(x=x1 + x_diff+150, y=y1)
        y1 += y_diff
        self.l2.place(x=x1, y=y1)
        self.t2.place(x=x1 + x_diff+150, y=y1)
        self.responseimglbl.place(x=x1 + x_diff * 3+200, y=y1, width=self.ressize_w, height=self.ressize_h)
        y1 += y_diff
        self.l3.place(x=x1, y=y1)
        self.t3.place(x=x1 + x_diff+150, y=y1)
        y1 += y_diff
        self.l4.place(x=x1, y=y1)
        self.c1.place(x=x1 + x_diff+150, y=y1,width=245)
        self.cardimglbl.place(x=x1 + x_diff * 2+180, y=y1, width=cardsize_w, height=cardsize_h)
        y1 += y_diff
        self.l5.place(x=x1, y=y1)
        self.c2.place(x=x1 + x_diff+150, y=y1,width=245)
        y1 += y_diff
        self.l6.place(x=x1, y=y1)
        self.c3.place(x=x1 + x_diff+150, y=y1,width=245)
        y1 += y_diff
        self.l7.place(x=x1, y=y1)
        self.c4.place(x=x1 + x_diff+150, y=y1,width=245)
        y1 += y_diff
        self.btn1.place(x=x1 + x_diff * 1, y=y1, width=200, height=40)
        y1 += y_diff
        self.btn2.place(x=x1 + x_diff * 1, y=y1, width=200, height=40)
        # self.btn3.place(x=x1 + x_diff * 2, y=y1, width=200, height=40)
        y1 += y_diff
        self.l8.place(x=x1 + x_diff, y=y1)
        self.databaseConnection()
        self.clearPage()
        self.window.mainloop()

    def predict(self):

        distance_from_home = int(self.t1.get())
        distance_from_last_transaction = float(self.t2.get())
        ratio_to_median_purchase_price= float(self.t3.get())
        repeatretailer = self.v1.get()
        if repeatretailer == "Yes":
            repeat_retailer = 1
        else:
            repeat_retailer = 0
        chip = self.v2.get()
        if chip == "Yes":
            used_chip = 1
        else:
            used_chip = 0
        pin_number = self.v3.get()
        if pin_number == "Yes":
            used_pin_number = 1
        else:
            used_pin_number = 0
        onlineorder = self.v4.get()
        if onlineorder == "Yes":
            online_order = 1
        else:
            online_order = 0


        print("distance from home:",distance_from_home)
        print("distance from home:", type(distance_from_home))
        print("distance_from_last_transaction:", distance_from_last_transaction)
        print("distance_from_last_transaction:", type(distance_from_last_transaction))
        print("ratio_to_median_purchase_price:", ratio_to_median_purchase_price)
        print("ratio_to_median_purchase_price:", type(ratio_to_median_purchase_price))

        print("repeat_retailer", repeat_retailer)
        print("repeat_retailer",type(repeat_retailer) )
        print("used_chip", used_chip)
        print("used_chip", type(used_chip))
        print("used_pin_number", used_pin_number)
        print("used_pin_number", type(used_pin_number))
        print("online_order", online_order)
        print("online_order",type(online_order))

        self.predict =int(model.predict([[distance_from_home,distance_from_last_transaction , ratio_to_median_purchase_price,repeat_retailer, used_chip,used_pin_number ,
                                online_order  ]]))


        self.output = self.predict
        print("predict = ",self.predict)
        if self.output == 1:
            # print("Congratulation you are away from fraud")
            # print("\n \000200D ")
            # print("There is highe ")
            # print("\n \U0001FAE8 ")
            self.l8.config(text="There is higher chance of having Fraud Transaction\n \U0001FAE8 ")

            self.responseimg1 = ImageTk.PhotoImage(Image.open("Fraud_Alert_Logo.png").resize((self.ressize_w,self.ressize_h)))
            self.responseimglbl.config(image=self.responseimg1)
            # self.btn3['state'] = 'disabled'
        else:
            self.l8.config(text="Congratulation you are away from fraud Transaction \n \U0001FAE8 ")
            self.responseimg1 = ImageTk.PhotoImage(Image.open("facebook-thumbs-up-u0h.png").resize((self.ressize_w,self.ressize_h)))
            self.responseimglbl.config(image=self.responseimg1)
            # self.btn3['state'] = 'normal'
        self.saveData()

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.c1.current(0)
        self.c2.current(0)
        self.c3.current(0)
        self.c4.current(0)
        self.l8.config(text="")
        # self.btn3['state'] = 'disabled'
        self.output = ""
        self.responseimg1 = ImageTk.PhotoImage(
            Image.open("question_mark_PNG134.png").resize((self.ressize_w, self.ressize_h)))
        self.responseimglbl.config(image=self.responseimg1)
    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='credit_card_fraud_detection', user='root', password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error in Database Connection : \n" + str(e), parent=self.window)
    def saveData(self):
        # if self.validate_check()==False:
        #     return
        try:
            from datetime import date
            today = date.today()
            today2 = today.strftime("%Y-%m-%d")


            qry = " insert into prediction_page (distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeatretailer,chip,pin_number,onlineorder,date,prediction_output) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry, (int(self.t1.get()),str(float(self.t2.get())) ,str(float(self.t3.get())),
                                               self.v1.get(), self.v2.get(), self.v3.get(), self.v4.get(),today2,self.output ))
            self.conn.commit()
            if (rowcount == 1):
                messagebox.showinfo("Success", "chances of fraud predict successfully", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error in Insertion : \n" + str(e), parent=self.window)


if __name__ == '__main__':
    dummy=Tk()
    obj = frauddetectionPageClass(dummy)
    dummy.mainloop()

