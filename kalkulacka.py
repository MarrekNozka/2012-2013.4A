#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  kalkulacka.py
# Datum:   20.11.2012 13:11
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   grafická kalkulačka s reverzní notací
####################################################

import sys
from sys import stdin, stdout, stderr
from Tkinter import *
####################################################

def exit(event=None):
    sys.exit(0)

stack = []
# vloží do zásobníku a do Listboxu číslo
def push(item):
    stack.append(complex(item))
    box.insert(END, str(item))

def pop():
    box.delete(END)
    return stack.pop()


# hlavní funkce, ktrá provádí požadovanou akci
def goo(event=None):
    line = edt.get()     # vezmu celý uživatelský vstup
    items = line.split() # rozdělím ho na jednotlivé položky
    edt.delete(0,END)    # vymažu vstupní pole
    for token in items: 
        if token == '+':
            a = pop()
            b = pop()
            push(a+b)
        elif token == '*':
            a = pop()
            b = pop()
            push(a*b)
        else:
            push(token)


####################################################

mainWin = Tk(className="foo")
mainWin.title("Kalkulacka")
mainWin.option_add('*Font', 'Terminus 14')

# při stisku Esc se aplikace zavře
mainWin.bind("<Escape>",exit)

lbl = Label(mainWin, text=u"Kalkulačka s reverzní notací")
lbl.pack()

box = Listbox(mainWin, width=20, height=10)
box.pack()

edt = Entry(mainWin, width=20)
edt.pack()
edt.bind("<Return>", goo)

edt.focus_set() # vyberu vstupní pole a můžu hned psát
mainWin.mainloop()

