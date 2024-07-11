from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import detail_page as dp
import seaborn as sns
class Comparision2Class:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        self.window.title("Credit card fraud detector")
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
                             font=dp.myfont1, foreground=dp.fg_color, background=dp.bg_color2)
        self.headlbl.place(x=0, y=0, width=w1, height=70)

        self.l1 = Label(self.window, text="Bivarate analysis", font=('Century', 20, 'bold'),
                        foreground=dp.fg_color, background=dp.bg_color2)
        self.l1.place(x=40, y=100)
        x1 = 40
        y1 = 200
        x_dif = 440
        card_data = pd.read_csv('card_transdata.csv')



        figure1 = plt.Figure(figsize=(5, 5), dpi=60)
        ax1 = figure1.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure1, self.window)
        diagram.get_tk_widget().place(x=x1 + x_dif * 0, y=y1)
        ax1.set_title('repeat retailer v/s fraud')
        sns_ax1 = sns.countplot(data=card_data, x='repeat_retailer', hue='fraud',ax=ax1)
        sns_ax1.set(xticks=[0, 1], xticklabels=['regular retailer ', 'new retailer'])

        figure2 = plt.Figure(figsize=(5, 5), dpi=60)
        ax2 = figure2.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure2, self.window)
        diagram.get_tk_widget().place(x=x1 +x_dif-100 , y=y1)
        ax2.set_title('used chip v/s fraud')
        sns_ax2 = sns.countplot(data=card_data, x='used_chip', hue='fraud', ax=ax2)
        sns_ax2.set(xticks=[0, 1], xticklabels=['regular used chip ', 'new used chip'])

        figure3 = plt.Figure(figsize=(5, 5), dpi=60)
        ax3 = figure3.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure3, self.window)
        diagram.get_tk_widget().place(x=x1 + x_dif *2-200 , y=y1)
        ax3.set_title('used pin number v/s fraud')
        sns_ax3 = sns.countplot(data=card_data, x='used_pin_number', hue='fraud', ax=ax3)
        sns_ax3.set(xticks=[0, 1], xticklabels=['regular used pin number ', 'new used pin number'])

        figure4 = plt.Figure(figsize=(5, 5), dpi=60)
        ax4 = figure4.add_subplot(111)
        diagram = FigureCanvasTkAgg(figure4, self.window)
        diagram.get_tk_widget().place(x=x1 + x_dif *3-280, y=y1)
        ax4.set_title('online order v/s fraud')
        sns_ax4 = sns.countplot(data=card_data, x='online_order', hue='fraud', ax=ax4)
        sns_ax4.set(xticks=[0, 1], xticklabels=['regular online order ', 'new online order'])

        self.window.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Close ? ", parent=self.window)
        if ans == 'yes':
            self.window.destroy()

if __name__ == '__main__':
    dummy = Tk()
    obj = Comparision2Class(dummy)
    dummy.mainloop()
