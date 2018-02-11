import pandas as pd
import Tkinter
import tkFileDialog
import matplotlib

matplotlib.use("TkAgg")

class App():
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.geometry("500x100")
        self.root.wm_title("Main")

        labelframe = Tkinter.LabelFrame(self.root, text="Open file and do something to it")
        labelframe.pack(fill="both", expand="yes")
        right = Tkinter.Button(labelframe, text = 'Give file location', command=self.open_file)
        right.pack()

        button = Tkinter.Button(self.root, text = 'Close', command=self.quit)
        button.pack()
        self.root.mainloop()

    def browse_file(self):
        file_location = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.csv"), ("All files", "*")))
        return(file_location)


    def open_file(self):
        file_location = self.browse_file()
        df1 = pd.read_csv(file_location, header=17, index_col=False, usecols=range(1,13), encoding='latin-1')  
        print (df1)


    def quit(self):
        self.root.destroy() 

app = App()
