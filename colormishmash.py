#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  colormishmash.py
# Datum:   13.11.2012 13:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   jednoduchý program pro míchání barev
####################################################

import sys
from Tkinter import *
####################################################

# ukončí program
def exit(event=None):
    sys.exit(0)


# formátovaání: http://docs.python.org/2.7/library/string.html#formatstrings
# převede hodnoty posuvníků na barvu
def goo(value):
    color = "#{:02x}{:02x}{:02x}".format(scaleR.get(),scaleG.get(),scaleB.get())
    colorPanel.config(bg=color)
    # změním hodnotu ve vstupním poli htmlValue, protože je svázána s textArray
    textArray.set(color)

####################################################

mainWin = Tk()  # vytvořím okno
mainWin.title("colormishmash.py") # nastavím titulek

# vytvořím udělátko
scaleR = Scale(mainWin, from_=0, to=255, orient=HORIZONTAL, length=200, 
               label='červená', command=goo)   
scaleR.pack()  # umístím udělátko
scaleG = Scale(mainWin, from_=0, to=255, orient=HORIZONTAL, length=200,
               label='zelená', command=goo)   
scaleG.pack()  
scaleB = Scale(mainWin, from_=0, to=255, orient=HORIZONTAL, length=200, 
               label='modrá', command=goo)   
scaleB.pack()  
 
# proměná, kterou svážu s údajem ve vstupním poli htmlValue
textArray = StringVar()
htmlValue = Entry(mainWin, textvariable=textArray )
htmlValue.pack()

colorPanel = Canvas(mainWin, bg='red', height=200, width=200)
colorPanel.pack()

mainWin.mainloop()

