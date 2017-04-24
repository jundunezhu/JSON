from tkinter import *
import tkinter as tk
import datetime

import transfer_main
import transfer_func

def load_gui(self):

    self.origin_file = StringVar()
    self.destination_file = StringVar()
    self.time_file = StringVar()

    self.lbl_ofile = tk.Label(self.master,text='Origin File:')
    self.lbl_ofile.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.btn_ofile = tk.Button(self.master,text='Browse:', command=lambda: transfer_func.browse_file(self,0))
    self.btn_ofile.grid(row=0,column=1,padx=(27,0),pady=(10,0),sticky=N+W)
    
    self.lbl_dfile = tk.Label(self.master,text='Destination File:')
    self.lbl_dfile.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.btn_dfile = tk.Button(self.master,text='Browse:', command=lambda: transfer_func.browse_file(self,1))
    self.btn_dfile.grid(row=2,column=1,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_osfile = tk.Label(self.master,textvariable=self.origin_file)
    self.lbl_osfile.grid(row=0,column=2,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_dsfile = tk.Label(self.master,textvariable=self.destination_file)
    self.lbl_dsfile.grid(row=2,column=2,padx=(27,0),pady=(10,0),sticky=N+W)
    
    
    self.btn_transfer = tk.Button(self.master,width=12,height=2,text='Transfer',command=lambda: transfer_func.transfer_file(self))
    self.btn_transfer.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)

    self.lbl_otfile = tk.Label(self.master,textvariable=self.time_file)
    self.lbl_otfile.grid(row=8,column=1,padx=(25,0),pady=(45,10),sticky=W)

if __name__ == "__main__":
    pass
































    
