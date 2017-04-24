from tkinter import *
import tkinter as tk
import os
import time
import shutil
import datetime
import sqlite3

import transfer_main
import transfer_gui

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def browse_file(self,btn_numb):
    fileName = filedialog.askdirectory()
    if btn_numb == 0:
        self.origin_file.set(fileName)
    else:
        self.destination_file.set(fileName)

def transfer_file(self):
    source = self.origin_file.get()
    dest = self.destination_file.get()
    files = os.listdir(source)
    count = 0
    for file_name in files:
        abs_path1 = os.path.join(source, file_name)
        mod_time = os.path.getmtime(abs_path1)
        check_time = time.time() - 86400
        if mod_time >= check_time:
            abs_path3 = os.path.join(source, file_name)
            shutil.move(abs_path3, dest)
            
    insert_time(self)
    print_database(self)
                       
def create_db(self):
    conn = sqlite3.connect('db_transfer_time.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists transfer123 ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_time REAL);")
        conn.commit()
    conn.close()
    
def first_run(self):
    conn = sqlite3.connect('db_transfer_time.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO transfer123 (col_time) VALUES (?)""", ('1234.56789'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM transfer123""")
    count = cur.fetchone()[0]
    return cur,count

def insert_time(self):
    conn = sqlite3.connect('db_transfer_time.db')
    cur = conn.cursor()        
    cur.execute("INSERT INTO transfer123 (col_time) \
        VALUES (?)", [time.ctime()])
    conn.commit()
    conn.close()

def print_database(self):
    conn = sqlite3.connect('db_transfer_time.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_time from transfer123")
        rows = cur.fetchone()
        print(rows)
        self.time_file.set(cur.fetchone())
    conn.close()
    
if __name__ == "__main__":
    pass

































    
                                                                                                                                

                    

            
   
                                                    
