#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  Tk_uvod.py
# Datum:   06.11.2012 13:40
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   úvod do Tk

from Tkinter import * 
import sys
#########################################

def konec():
    print "končím"
    sys.exit(0)

def nove():
    vedlejsiOkno = Tk()
    napis = Label(vedlejsiOkno,text='Jsem vedlejsi okno')
    napis.pack()

hlavniOkno = Tk()

titulek = Label(hlavniOkno, text='Ahoj')
titulek.pack()

tlacitko = Button(hlavniOkno, text='Konec', command=nove )
tlacitko.pack()

hlavniOkno.mainloop()
