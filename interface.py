#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:46:18 2020

@author: leila.nedjar
"""

# coding: utf-8
from tkinter import *
from calculatrice import *


# create window
window = Tk()
window.title("Calculatrice")


value = StringVar()
Label(window, textvariable=value, width=30).pack()
value.set("texte par défaut")

#Button
button = Button(window, text="change", command=value.set('texte'))
button.pack()
window.mainloop()