from tkinter import *
from tkinter import messagebox
import detail_page as dp
from comparison_1 import Comparision1Class
from Comparison_2 import Comparision2Class
from credit_card_fraud_detection import frauddetectionPageClass
from PIL import ImageTk, Image
from report_page import ViewReportClass

class HomepageClass:
    def __init__(self):
        self.window = Tk()
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1=int(self.w/2)
        h1=int(self.h/2)
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2))
        # self.window.state('zoomed')
        self.window.title('Fraud Predictor')

        self.headlbl = Label(self.window, text="Credit Card Fraud Detection",
                             font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2)

        self.window.config(background=dp.bg_color)

        self.b1 = Button(self.window,text="Predict",font=dp.myfont1,
                         foreground=dp.fg_color,background=dp.bg_color2,command=lambda : frauddetectionPageClass(self.window))
        self.b2 = Button(self.window,text="Univarate Analysis",font=dp.myfont1,
                         foreground=dp.fg_color,background=dp.bg_color2,command=lambda :Comparision1Class(self.window))
        self.b3 = Button(self.window,text="Bivarate Analysis",font=dp.myfont1,
                         foreground=dp.fg_color,background=dp.bg_color2,command=lambda :Comparision2Class(self.window))
        self.b4 = Button(self.window,text=" Report",font=dp.myfont1,
                         foreground=dp.fg_color,background=dp.bg_color2,command=lambda :ViewReportClass(self.window))
        self.b5 = Button(self.window,text="Close",font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2,command=self.quitter)



        x1 = 30
        y1=100
        y_diff=70
        b_width=220
        b_height=45



        size_w=w1 - (x1+b_width+10)
        size_h=200
        self.img1 = ImageTk.PhotoImage(Image.open("homepage.png").resize((size_w-50,size_h)))
        self.imglbl = Label(self.window,image=self.img1,background=dp.bg_color)



        self.headlbl.place(x=0, y=0,width=w1,height=70)

        self.b1.place(x=x1,y=y1,width=b_width,height=b_height)
        self.imglbl.place(x=x1+b_width+10,y=150,width=size_w,height=size_h)
        y1+=y_diff
        self.b2.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b3.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b4.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b5.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff


        self.window.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Close ? ", parent=self.window)
        if ans == 'yes':
            self.window.destroy()

if __name__ == '__main__':
    HomepageClass()