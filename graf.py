#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  graf.py
# Datum:   02.10.2012 12:56
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   tisk grafu ze souboru
###################################################3 

import pylab as lab

# načtu jmého souboru
jmenoSouboru = raw_input("zadej jméno souboru >>> ")
if jmenoSouboru == '':
    jmenoSouboru = 'tabulka.txt'

popisky = []
data = []

# otevřu soubor pro čtení
f = open(jmenoSouboru,'r')
# čtu soubor řádek po řádku
while True:
    radek = f.readline()
    if radek == '':
        break
    elif len(radek.split()) == 0: # pokud načtu prázdný řádek
        continue                  # pokračuji od začátku cyklu
    elif radek.strip()[0] == '#': # pokud řádek začíná #
        continue                  # pokračuji od začátku cyklu
    elif radek.strip()[0] == '@': # pokud řádek začíná @ 
        kod = radek.strip()[1:].strip()  # ořež @ a mezery a ...
        exec(kod)                 # ... proveď ho jako python kód
        continue
# zpracování řádku
    radek = radek.split()
    popisky.append(radek[0])
    data.append(radek[1:])

# převedu data z řetězců na čísla
for r in range(len(data)):
    for i in range(r):
        data[r][i] = float( data[r][i] )


# vykreslím graf
lab.figure()
lab.grid(True)
for i in range(1,len(data)):
    lab.plot(data[0],data[i])
lab.xlabel(popisky[0])
lab.ylabel(popisky[1:])

lab.title(titulek.decode('utf-8'))

lab.show()
