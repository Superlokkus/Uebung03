#!/usr/bin/python
# encoding=utf-8


"""Aufgabe 2 & 3 Übung 03 """

def fakultaet(n):
    """Gibt die Fakultät von n zurück"""
    sequence = range(1,(n+1),1)
    result = 1
    for x in sequence:
        result = result * x
    return result

assert fakultaet(0)==1

def Euler(n):
    """Gibt die euler'sche Zahl in als Näherung mit n Termen zurück"""
    result = 1.0
    squence = range (1,n+1,1)
    
    for x in squence:
        result = result + (1.0/fakultaet(x))
    return result
    
print Euler(10)
print Euler(100)
print Euler(150)
#print Euler(200)

