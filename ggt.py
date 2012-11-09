#!/usr/bin/python
# encoding=utf-8

"""Aufgabe 4 Übung 03"""

def ggt(n,m):
    """Gibt den größten gemeinsamen Teiler zurück"""
    if m==0:
        return n
    else:
        return ggt(m,n%m)
        
print ggt(20790,19404)