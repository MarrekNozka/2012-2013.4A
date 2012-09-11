#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  chodec-1D.py
# Datum:   11.09.2012 13:14
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   program vypočítá délku dráhy pohyby po přímce
#

suma=0
tady_jsem = input('začínáme  > ')

while True:
    try:
        tady_jsemTEXT = raw_input('další bod > ')
        if tady_jsemTEXT == 'end':
            break
        tady_jsem_byl = tady_jsem 
        tady_jsem = int(tady_jsemTEXT) 
        suma = suma + abs(tady_jsem - tady_jsem_byl)
        print suma
    except EOFError:
        exit()
    except:
        print "musíš zadat číslo"
