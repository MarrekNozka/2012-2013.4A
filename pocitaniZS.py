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
dobre = 0
celkem =0

def exit(event=None):
    sys.exit(0)


def novyPriklad(event=None):
    global vysledek
# náhodná operace
    vyber=operaceEntry.get()
# ošetřím zadání chybných znaků do vstupního pole
    new=''
    for znak in vyber:
        if znak in '+-*:/':
            new+=znak
    vyber = new
# ošetřím zadání prázdného řetězce do vstupního pole    
    if vyber=='':
        vyber='+-*/'
# umístím kontrolovaný řetězec zpět do vstupního pole
    operaceEntry.delete(0,END)
    operaceEntry.insert(0,vyber)
    operace=vyber[ random.randint(0,len(vyber)-1) ]
    if operace == '*' :
# generuje čísla a počítá výsledek
        cisloA= random.randint(1,10)
        cisloB= random.randint(1,10)
        vysledek = cisloA * cisloB
# zobrazí operaci
        lblOperace.config(text='*')
    elif operace == '+':
        cisloA= random.randint(1,99)
        cisloB= random.randint(1,100-cisloA)
        vysledek = cisloA + cisloB
        lblOperace.config(text='+')
    elif operace == '-':
        cisloA= random.randint(1,99)
        cisloB= random.randint(1,99)
        if cisloB > cisloA: 
            (cisloA,cisloB) = (cisloB,cisloA)
        vysledek = cisloA - cisloB
        lblOperace.config(text='-')
    elif operace == '/' or operace == ':':
        vysledek = random.randint(1,10)
        cisloB = random.randint(1,10)
        cisloA = vysledek * cisloB
        lblOperace.config(text='/')

# umístí čísla do udělátek
    cisloAentry.delete(0, END)
    cisloAentry.insert(0, str(cisloA) )
    cisloBentry.delete(0, END)
    cisloBentry.insert(0, str(cisloB) )


def kontrola(event):
    global vysledek
    global dobre
    global celkem
    try:
        if vysledek == int( vysledekEntry.get() ):
            lblOK.config(text='OK')
            dobre += 1
        else:
            lblOK.config(text=';-(')
        celkem +=1
# po tom, co jsem kontroloval generuji nový příklad
        vysledekEntry.delete(0,END)
        lblStat.config(text='{0}/{1}'.format(dobre,celkem))
        novyPriklad()
    except:
        lblOK.config(text='Zadej číslo')



####################################################

mainWin = Tk(className="foo")
mainWin.title("pocitaniZS.py")
mainWin.option_add('*Font', 'Terminus 24')
mainWin.bind("<Escape>",exit)

# výběr operace
Label(mainWin, text=u"Operace: ").grid(row=0, column=0, columnspan=3)
operaceEntry = Entry(mainWin, width=8, )
operaceEntry.grid(row=0, column=3, columnspan=2)
operaceEntry.insert(0,'+-*/')

# Číslo A
cisloAentry=Entry(mainWin, width=4)
cisloAentry.grid(row=1, column=0)
# matematická operace
lblOperace=Label(mainWin,text='?')
lblOperace.grid(row=1, column=1)
# Číslo B
cisloBentry=Entry(mainWin, width=4)
cisloBentry.grid(row=1, column=2)
# rovnítko
Label(mainWin,text='=').grid(row=1, column=3)
# Výsledek
vysledekEntry=Entry(mainWin, width=4)
vysledekEntry.grid(row=1, column=4)

# Hodnocení
lblOK=Label(mainWin,text='?')
lblOK.grid(row=2, column=0)
# Statistika
lblStat=Label(mainWin,text='0/0')
lblStat.grid(row=2, column=4)


########################################################
# vazby na události
vysledekEntry.bind('<Return>',kontrola)
mainWin.bind('<Map>',novyPriklad)

mainWin.mainloop()


