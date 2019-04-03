#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:17:44 2018

@author: nagano
"""

import tkinter as tk
from datetime import datetime
import numpy as np
import sys

root = tk.Tk()
root.title("number count")
root.geometry("150x100")
number = 0

def save():
    global number
    file = open('saveNumber.txt', 'w')  #書き込みモードでオープン
    file.write("人数 : "+str(number)+" Time : " + str(datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

def end():
    sys.exit()



def button_bushed():
    global number
    
    if selection.get() == -1:
        number += -1
    elif selection.get() == 1:
        number += 1
    
    print ("number of people : %d 人__________時間 : %s" %(number,datetime.now().strftime("%Y/%m/%d %H:%M:%S")))



selection = tk.IntVar()
tk.Radiobutton( root, text="+1", variable=selection, value= 1 ).pack()
tk.Radiobutton( root, text="-1", variable=selection, value= -1 ).pack()

tk.Button(root, text='push!', command=button_bushed).pack(side="right")
tk.Button(root,text="save",bg="gray",command=save).pack(side="left")

tk.Button(root,text="exit",bg="gray",command=end).pack(side="left")


root.mainloop()


"""slide bar
def button_bushed():
    print s.get()

tk.Button(root, text='push!', command=button_bushed).pack()
s = tk.Scale(root , from_=0, to=100,  orient="h" )
s.pack()

root.mainloop()
"""