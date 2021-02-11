# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:09:55 2021

@author: xchel
"""

import random
from Triangulo import Triangulo

def esUnica(v, Lst):
    esTuplaUnica = True
    for i in range(len(Lst)):
        if v[0] == Lst[i][0] and v[1] == Lst[i][1]:
            esTuplaUnica = False
            break
    return esTuplaUnica

def genVerts():
    v = []
    v1 = (random.uniform(0, 10), random.uniform(0, 10))
    v.append(v1)
    
    while True:
        v2 = (random.uniform(0, 10), random.uniform(0, 10))
        if esUnica(v2, v) == True:
            v.append(v2)
            break
        
    while True:
        v3 = (random.uniform(0, 10), random.uniform(0, 10))
        if esUnica(v3, v) == True:
            v.append(v3)
            break
    return v
        
def genTriangulos():
    triangulos = []
    
    for i in range(0, 100):
        t = Triangulo()
        vert = genVerts()
        t.obtVertices(vert[0], vert[1], vert[2])
        t.clcArea()
        print("Triángulo", i+1, ":")
        t.imprVA()
        triangulos.append(t)
    
    max = 0
    indice = -1
    for i in range(len(triangulos)):
        if triangulos[i].area > max:
            max = triangulos[i].area
            indice = i
    
    print("El triángulo con mayor área es el número", indice + 1, "con las siguientes propiedades:")
    triangulos[indice].imprVA()
    
genTriangulos()