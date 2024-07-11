from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import detail_page as dp
import seaborn as sns
class Comparision1Class:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        self.window.title("Credit fraud detector")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1=self.w
        h1=self.h
        self.window.minsize(w1,h1)
        # self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2))
        self.window.state('zoomed')

        # ----------------- widgets -----------------------------------------------------
        self.window.config(background=dp.bg_color2)
        self.headlbl = Label(self.window, text="Analysis ",
                             font=dp.myfont1,foreground=dp.fg_color,background=dp.bg_color2)
        self.headlbl.place(x=0, y=0,width=w1,height=70)

        self.l1 = Label(self.window, text="Univariate analysis",font=('Century', 20, 'bold'),
                        foreground=dp.fg_color,background=dp.bg_color2)
        self.l1.place(x=40,y=100)

        x1 = 75
        y1 = 280
        x_dif = 410
        car_data = pd.read_csv('card_transdata.csv')

        figure1 = plt.Figure(figsize=(5,5), dpi=60)
        ax1 = figure1.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure1, self.window)
        diagram.get_tk_widget().place(x=x1 + x_dif * 0, y=y1)
        ax1.set_title('About repeat_retailer')
        car_data.repeat_retailer.value_counts().plot(kind='bar', ax=ax1, x='repeat_retailer', legend=True, rot=45)

        figure2 = plt.Figure(figsize=(5,5), dpi=60)
        ax2 = figure2.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure2, self.window)
        diagram.get_tk_widget().place(x=x1 +x_dif-70 , y=y1)
        ax2.set_title('About used_chip')
        car_data.used_chip.value_counts().plot(kind='bar', ax=ax2, x='used_chip', legend=True, rot=0)

        figure3 = plt.Figure(figsize=(5,5), dpi=60)
        ax3 = figure3.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure3, self.window)
        diagram.get_tk_widget().place(x=x1 + x_dif *2-130 , y=y1)
        ax3.set_title('About used_pin_number')
        car_data.used_pin_number.value_counts().plot(kind='bar', ax=ax3, x='used_pin_number', legend=True, rot=0)

        figure4 = plt.Figure(figsize=(5,5), dpi=60)
        ax4 = figure4.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure4, self.window)
        diagram.get_tk_widget().place(x=x1 + x_dif *3-200, y=y1)
        ax4.set_title('About online_order')
        car_data.online_order.value_counts().plot(kind='bar', ax=ax4, x='online_order', legend=True, rot=0)

        self.window.mainloop()

if __name__ == '__main__':
    dummy = Tk()
    obj = Comparision1Class(dummy)
    dummy.mainloop()

