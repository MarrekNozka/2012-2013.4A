#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  kalkulacka.py
# Datum:   20.11.2012 13:11
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   grafická kalkulačka s reverzní notací
####################################################

import sys, cmath, math
from sys import stdin, stdout, stderr
from Tkinter import *
import cmath  # počítání s komplexními čísly
####################################################

def exit(event=None):
    sys.exit(0)

stack = []
# vloží do zásobníku a do Listboxu číslo
def push(item):
    item = item.replace('pi','3.141592653589793')
    item = item.replace('e','2.718281828459045')
    try:
        if item.count(',')==1:
            num = item.split(',')
            stack.append( float(num[0]) + float(num[1])*1j )
            box.insert(END, str(stack[-1]))
            return True
        elif item.count('(')==1:
            num = item.split('(')
            stack.append( float(num[0]) * cmath.exp( float(num[1])*1j ) )
            box.insert(END, str(stack[-1]))
            return True
        else:
            stack.append(complex(item))
            box.insert(END, str(item))
            return True
    except:
        return False

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
        elif token == '/':
            a = pop()
            b = pop()
            push(b/a)
        elif token == '-':
            a = pop()
            b = pop()
            push(b-a)
        elif token == 'log':
            a = pop()
            push(cmath.log10(a))
        elif token == 'ln':
            a = pop()
            push(cmath.log(a))
        elif token == 'pi':
            push(cmath.pi)
        elif token == 'e':
            push(cmath.e)
        else:
            if push(token):
                lblMsg.config(text="OK", fg='black')
            else:
                lblMsg.config(text="Chyba", fg='red')
                err = token + token.join( line.split(token)[1:] )
                edt.delete(0,END)
                edt.insert(0,err)
                edt.icursor(0)
                edt.selection_from(0)
                edt.selection_to(len(token))
                break 




####################################################

mainWin = Tk(className="foo")
mainWin.title("Kalkulacka")
mainWin.option_add('*Font', 'Terminus 16')

# při stisku Esc se aplikace zavře
mainWin.bind("<Escape>",exit)

lbl = Label(mainWin, text=u"Kalkulačka s reverzní notací")
lbl.pack()

box = Listbox(mainWin, width=20, height=10)
box.pack()

lblMsg = Label(mainWin, text=u"...")
lblMsg.pack()

edt = Entry(mainWin, width=20)
edt.pack()
edt.bind("<Return>", goo)

edt.focus_set() # vyberu vstupní pole a můžu hned psát
mainWin.mainloop()

