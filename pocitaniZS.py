#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  pocitaniZS.py
# Datum:   19.02.2013 12:41
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   počítání pro Základní školy
####################################################

import sys,random
from sys import stdin, stdout, stderr
from Tkinter import *
####################################################

vysledek=0

def exit(event=None):
    sys.exit(0)


def novyPriklad():
    cisloA= random.randint(1,10)
    cisloB= random.randint(1,10)
    vysledek = cisloA * cisloB

    cisloAentry.delete(0, END)
    cisloAentry.insert(0, str(cisloA) )
    cisloBentry.delete(0, END)
    cisloBentry.insert(0, str(cisloB) )
    lblOperace.config(text='*')

    return vysledek

def goo(event):
    global vysledek
    if vysledek == int( vysledekEntry.get() ):
        lblOK.config(text='OK')
    else:
        lblOK.config(text=':(')
    vysledek = novyPriklad()



####################################################

mainWin = Tk(className="foo")
mainWin.title("pocitaniZS.py")
mainWin.option_add('*Font', 'Terminus 14')
mainWin.bind("<Escape>",exit)

Label(mainWin, text=u"Operace: ").grid(row=0, column=0, columnspan=3)

operaceEntry = Entry(mainWin, width=8)
operaceEntry.grid(row=0, column=3, columnspan=2)

cisloAentry=Entry(mainWin, width=4)
cisloAentry.grid(row=1, column=0)
lblOperace=Label(mainWin,text='?')
lblOperace.grid(row=1, column=1)
cisloBentry=Entry(mainWin, width=4)
cisloBentry.grid(row=1, column=2)
Label(mainWin,text='=').grid(row=1, column=3)
vysledekEntry=Entry(mainWin, width=4)
vysledekEntry.grid(row=1, column=4)

lblOK=Label(mainWin,text='?')
lblOK.grid(row=2, column=0)


vysledekEntry.bind('<Return>',goo)
#mainWin.bind('<Enter>',goo)

mainWin.mainloop()


