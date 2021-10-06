"""Napisati metod double duzinaDuzi(double x1, double y1, double x2,
double y2) koji vraća dužinu duži čije su krajnje tačke A(x1, y1) i B(x2,y2)."""
import math


def duzina_duzi (x1,x2,y1,y2) :
   return math.sqrt ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
print(duzina_duzi(1,1,1,1))

