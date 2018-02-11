import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib

matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib.figure import Figure


def browse_file():
    global file_location
    file_location = tk.filedialog.askopenfilename(filetypes = (("Template files", "*.csv"), ("All files", "*")))
    return(file_location)

df1 = pd.read_csv(file_location, header=17, index_col=False, usecols=range(1,13), encoding='latin-1')  



#GUI
LARGE_FONT= ("Verdana", 12)

class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Big Data")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Page1, Page2):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Page1)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="See graph",
                            command=lambda: [browse_file(), controller.show_frame(Page2)])

        button1.pack()

class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(Page1))
        button1.pack()

        fig = Figure(figsize=(5,4), dpi=100)
        ax= fig.add_subplot(111)

        df1.plot.scatter('x', 'y', ax=ax)
        #line_graph('Time', 'Force (N)')

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = BigData()
app.mainloop()
