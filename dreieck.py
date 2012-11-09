#!/usr/bin/python
# encoding=utf-8

"""Aufgabenstellung 1. Übung 03"""


def dreieck(a,b,c,):
    """Gibt wahr zurueck bei rechtwinkligem Dreieck"""
    if (((a**2)+(b**2))==(c**2)):
        return True
    else:
        return False
        


#Konkrete Werte
print dreieck(3,4,5)


#Euklid Algo