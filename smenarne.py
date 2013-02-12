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

def vypisMenu(a,b,c):
    nasobekEntry.config(state=NORMAL)
    nasobekEntry.delete(0,END)
    nasobekEntry.insert(0,meny[ menaVar.get() ][1])

    nakupEntry.config(state=NORMAL)
    nakupEntry.delete(0,END)
    nakupEntry.insert(0,meny[ menaVar.get() ][2])

    prodejEntry.config(state=NORMAL)
    prodejEntry.delete(0,END)
    prodejEntry.insert(0,meny[ menaVar.get() ][3])


def vypocet():
#    kurz = mena [ nakupVar.get() ] [  ]
    pass


####################################################

mainWin = Tk(className="foo")
mainWin.title("smenarne.py")
mainWin.option_add('*Font', 'Terminus 14')
mainWin.bind("<Escape>",exit)

####################################################
# výběr operace
operaceGroup = LabelFrame(mainWin, text="Operace", padx=5, pady=5)
operaceGroup.pack(anchor=W)

nakupVar = IntVar() 
nakupVar.set(2)
operace1 = Radiobutton(operaceGroup, text="Nákup", variable=nakupVar, value=1)
operace2 = Radiobutton(operaceGroup, text="Prodej", variable=nakupVar, value=2)
operace1.pack(anchor=W)
operace2.pack(anchor=W)

####################################################
# výběr měny
menaGroup = LabelFrame(mainWin, text="Měna", padx=5, pady=5)
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

#for n,item in enumerate(meny):
#    RB = Radiobutton(menaGroup,text=item[0], variable=menaVar, value=n)
#    RB.pack(anchor=W)
i=0
while i<len(meny):
    RB = Radiobutton(menaGroup,text=meny[i][0], variable=menaVar, value=i)
    RB.pack(anchor=W)
    i += 1

# při změně proměnní menaVar zavolej funkci vypisMenu()
menaVar.trace("w", vypisMenu )

#  meny[menaVar.get()][3]
####################################################
zapakovat=[]
zapakovat += [ LabelFrame(mainWin, text="Násobek", padx=5, pady=5) ]
zapakovat += [ LabelFrame(mainWin, text="Nákup", padx=5, pady=5) ]
zapakovat += [ LabelFrame(mainWin, text="Prodej", padx=5, pady=5) ]

nasobekEntry = Entry(zapakovat[0], state="readonly")
nakupEntry = Entry(zapakovat[1], state="readonly")
prodejEntry = Entry(zapakovat[2], state="readonly")
zapakovat += [nasobekEntry, nakupEntry, prodejEntry ]

zapakovat += [ LabelFrame(mainWin, text=u"Částka", padx=5, pady=5) ]
castkaEntry = Entry( zapakovat[-1], state=NORMAL)
# když stisknu Enter proveď funkci výpočet()
castkaEntry.bind("<Return>",vypocet)


zapakovat += [ LabelFrame(mainWin, text=u"Výpočet", padx=5, pady=5) ]
vypocetEntry = Entry(zapakovat[-1], state="readonly")

zapakovat += [ castkaEntry, vypocetEntry ]

for Q in zapakovat:
    Q.pack(anchor=W)

mainWin.mainloop()


