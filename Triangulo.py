# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:14:04 2021

@author: xchel
"""

class Triangulo:
    
    def __init__(self):
        self.verts = []
        self.area = None
        
    def obtVertices(self, v1, v2, v3):
        self.verts.append(v1)
        self.verts.append(v2)
        self.verts.append(v3)
        
    def clcArea(self):
        self.area = ((self.verts[0][0]*self.verts[1][1]) + (self.verts[0][1]*self.verts[2][0]) + (self.verts[2][1]*self.verts[1][0]) - (self.verts[1][1]*self.verts[2][0]) - (self.verts[0][0]*self.verts[2][1]) - (self.verts[0][1]*self.verts[1][0]))/2
        if self.area < 0:
            self.area = -self.area
        
    
    
    def imprVA(self):
        print("Los vértices son", self.verts, "y el área es de", self.area, "unidades cuadradas")