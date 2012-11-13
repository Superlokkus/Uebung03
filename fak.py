#!/usr/bin/python
# encoding=utf-8


"""Aufgabe 2 & 3 Übung 03 """

def fakultaet(n):
    """Gibt die Fakultät von n zurück"""
    #! zwischenspeichern würde man das nicht -- es ist besser, wenn man im
    #! for-loop sofort sieht, worüber iteriert wird. Nur bei langen, hässlichen
    #! ausdrücken nimmt man Variablen. Außerdem übergibt man nicht explizit die
    #! Schrittweite, wenn man eine Schrittweite von 1 will.
    sequence = range(1,(n+1),1)
    result = 1
    for x in sequence:
        #! *=
        result = result * x
    return result

#! ein paar mehr tests wären gut gewesen ;)
assert fakultaet(0)==1

def Euler(n):
    """Gibt die euler'sche Zahl in als Näherung mit n Termen zurück"""
    result = 1.0
    squence = range (1,n+1,1)  #! squence -> sequence, siehe außerdem oben

    for x in squence:
        result = result + (1.0/fakultaet(x))
    return result

print Euler(10)
print Euler(100)
print Euler(150)
#print Euler(200)

