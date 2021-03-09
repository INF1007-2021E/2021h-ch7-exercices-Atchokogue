#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys

sys.path.insert(0, 'C:\\Users\\atcho\\Documents\\GitHub\\2021h-ch6-1-exercices-Atchokogue')

from exercicech6 import frequence

from turtle import *


# TODO: Définissez vos fonction ici
def voletMasseEllipsoide(a=5, b=8, c=10, mv=1):
    volume = (4 / 3) * math.pi * a * b * c
    masse = mv * volume

    return volume, masse


def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle*2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)


def draw_tree():
    setheading(90)
    color("green")
    draw_branch(70, 7, 60)


def chaine_ADN_valide(x):
    for lettre in x:
        if lettre != "a" and lettre != "t" and lettre != "c" and lettre != "g":
            return False

    return True




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    mass_vol = voletMasseEllipsoide(a=8, mv=2)
    print(mass_vol)
    (lambda x: sorted(frequence(x), key=frequence(x).__getitem__)[-1])("test test test test test")

    draw_tree()