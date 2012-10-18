#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  newtonova-metoda.py
# Datum:   25.09.2012 12:33
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: 
# Popis:   
# 
#########################################
# funkce 1/4 počáteční hodnota 0.4
#        1
# f(x)= --- - b
#        x
b=4
x=0.4

i=1
while i<12:
    i += 1
    print "%.20f" % x
    x = x + ( x*(1-b*x) )

print "==================================="
#########################################

# funkce odmocnina a
#       2
# f(x)=x - a
#

a=9
x=14.

i=1
while i<12:
    i += 1
    print "%.20f" % x
    x = (x+a/x) / 2.0



