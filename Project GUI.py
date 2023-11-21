from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from RRSP import *

black = "#000000"
maroon = "#800000" 
grey = "#B6B6B4"

window = Tk()
window.title ("RRSP")
window.geometry('1000x600')
window.configure(background=black)
window.resizable(width=FALSE, height=FALSE)

Title = Label(window, text="Chaar Yaar Revenue and Stock Prediction", font=('Segoe Script', '20', 'bold'), height = 1, width=500, anchor='n', bg=maroon, fg=grey)
Title.pack(side="top", fill="x", pady=0)

city_name = Label(window, text="City Name", width=20, height=1, font=('Consolas','15'), bg=black, fg=grey, anchor='nw')
city_name.place(x=10, y=60)
city_entry = Entry(window, width=25, justify='left', highlightthickness=1, relief="solid", bg=grey, fg=black)
city_entry.place(x=190, y=60)

hours_open = Label(window, text = "Opening Hours", width=20, height=1, font = ('Consolas', '15'), bg = black, fg = grey, anchor = 'nw')
hours_open.place(x=10, y=100)
hours_entry = Entry(window, width=25, justify='left', highlightthickness=1, relief='solid', bg=grey, fg=black)
hours_entry.place(x=190, y=100)

rating_label = Label(window, text="Overall Ratings", width=20, height=1, font=('Consolas', '15'), bg = black, fg = grey, anchor = 'nw')
rating_label.place(x=10, y=140)
rating_entry = Entry(window, width=25, justify='left', highlightthickness=1, relief="solid", bg=grey, fg=black)
rating_entry.place(x=190, y=140)

expenses_label = Label(window, text="Expenses", width=20, height=1, font=('Consolas', '15'), bg = black, fg = grey, anchor = 'nw')
expenses_label.place(x=10, y=180)
expenses_entry = Entry(window, width=25, justify='left', highlightthickness=1, relief="solid", bg=grey, fg=black)
expenses_entry.place(x=190, y=180)

year_label = Label(window, text="Years", width=20, height=1, font=('Consolas', '15'), bg=black, fg=grey, anchor='nw')
year_label.place(x=10, y=220)
year_entry = Entry(window, width=25, justify='left', highlightthickness=1, relief="solid", bg=grey, fg=black)
year_entry.place(x=190, y=220)

def graphs():
    fig = Figure(figsize = (5, 5), dpi = 100)
    y = expense()
    x = revenue()
    z = pred_revenue()
    plot1 = fig.add_subplot(111)
    plot1.plot(y, x)
    plot1.plot(y, z)
    canvas = FigureCanvasTkAgg(fig,
							master = window)
    canvas.draw()
    canvas.get_tk_widget().place(x=450, y=60)
    toolbar = NavigationToolbar2Tk(canvas,
								window)
    toolbar.update()
    canvas.get_tk_widget().place(x=450, y=60)
    

# def show_image(imagefile):
#     image = Image.open(imagefile)
#     image1 = image.resize((500, 281))
#     image1.save('Image.png')
#     image = ImageTk.PhotoImage(file='Image.png')
#     imagebox.config(image=image)
#     imagebox.image = image

# imagebox = Label(window, bg=black)
# imagebox.place(x=450, y=60)
  
submit = Button(window, text="Submit", width=10, height=1, bg=maroon, fg=grey, font=('Consolas 15'), command=graphs)
submit.place(x=50, y=260)
window.mainloop()
