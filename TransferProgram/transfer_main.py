from tkinter import *
import tkinter as tk

import transfer_gui
import transfer_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        transfer_func.center_window(self,500,300)
        self.master.title("The File Transfer Program")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: transfer_func.ask_quit(self))

        transfer_func.create_db(self)
        transfer_gui.load_gui(self)
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
