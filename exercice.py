#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys

sys.path.insert(0, 'C:\\Users\\atcho\\Documents\\GitHub\\2021h-ch6-1-exercices-Atchokogue')

from exercicech6 import frequence

'''import importlib.util
spec = importlib.util.spec_from_file_location("frequence", "/2021h-ch6-1-exercices-Atchokogue/exercicech6.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.(foo)
foo.frequence()'''


# TODO: Définissez vos fonction ici
def VoletMasseEllipsoide(a=5, b=8, c=10, mv=1):
    volume = (4 / 3) * math.pi * a * b * c
    masse = mv * volume

    return volume, masse


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    mass_vol = VoletMasseEllipsoide(a=8, mv=2)
    print(mass_vol)
    (lambda x: sorted(frequence(x), key=frequence(x).__getitem__)[-1])("test test test test test")
