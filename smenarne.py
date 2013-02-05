#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  smenarne.py
# Datum:   05.02.2013 13:29
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: 
# Popis:   
####################################################

import sys
from sys import stdin, stdout, stderr
from Tkinter import *
####################################################

def exit(event=None):
    sys.exit(0)


####################################################

mainWin = Tk(className="foo")
mainWin.title("smenarne.py")
mainWin.option_add('*Font', 'Terminus 14')
mainWin.bind("<Escape>",exit)

####################################################
# výběr operace
operaceGroup = LabelFrame(mainWin, text="Operace", padx=5, pady=5)
operaceGroup.pack(anchor=W)

v = IntVar() 
v.set(2)
operace1 = Radiobutton(operaceGroup, text="Jednaaaaaa", variable=v, value=1)
operace2 = Radiobutton(operaceGroup, text="Dva", variable=v, value=2)
operace1.pack(anchor=W)
operace2.pack(anchor=W)

####################################################
# výběr měny
menaGroup = LabelFrame(mainWin, text="Operace", padx=5, pady=5)
menaGroup.pack(anchor=W)

meny = (
        ("EUR", 1,    25.3, 25.5),
        ("GBP", 1,    31.2, 31.4),
        ("USD", 1,    19.4, 19.5),
        ("JPY", 100,  22.06, 22.29),
        ("IDR", 1000, 2.0180, 2.0250),
        ("ABC", 1000, 2.0180, 2.0250),
        ("ERY", 1000, 2.0180, 2.0250)
       )

menaVar = IntVar()
menaVar.set(0)

for n,item in enumerate(meny):
    RB = Radiobutton(menaGroup,text=item[0], variable=menaVar, value=n)
    RB.pack(anchor=W)

i=0
while i<len(meny):
    RB = Radiobutton(menaGroup,text=meny[i][0], variable=menaVar, value=i)
    RB.pack(anchor=W)
    i += 1


#  meny[menaVar.get()][3]



####################################################

s= StringVar()
s.set("B")
a = Radiobutton(menaGroup, text="A", variable=s, value="A")
b = Radiobutton(menaGroup, text="B", variable=s, value="B")
c = Radiobutton(menaGroup, text="C", variable=s, value="C")
a.pack(anchor=W)
b.pack(anchor=W)
c.pack(anchor=W)

mainWin.mainloop()


