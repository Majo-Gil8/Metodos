# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:27:48 2020

@author: maria
"""

import numpy as np 
import meshio
from mpl_toolkits import mplot3d  
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

malla = meshio.read("knight.msh") 
pts = malla.points 
tets = malla.cells[0].data

# Para sacar volumen
v_total = 0.0
tets_filas = tets.shape[0] # Numero de filas
det_elem = np.ones((4,4), dtype = "float64") # Matriz determinante de tets
for i in range (0,tets_filas):
    for f in range (0,4):
        for c in range (0,4):
            if c != 3:  # Este if es porque la matriz pts solo tiene 3 columnas y el for nos lleva hasta la columna 4
                det_elem[f,c] = pts[tets[i,f],c]
            if c == 4:  # La 4ta columna de det_elem es de unos
                det_elem[f,c] = 1
    
    v = (1/6)*abs(np.linalg.det(det_elem)) # Formula del volumen de un tetraedro
    v_total = v_total + v # La suma de todos los volumenes

# Para graficar
a = np.array(pts[:,0]) # Columna 1/Eje x
b = np.array(pts[:,1]) # Columna 2/Eje y
c = np.array(pts[:,2]) # Columna 3/Eje z
   
# Plot nodos
fig = plt.figure(figsize = (10, 10)) 
ax = plt.axes(projection = "3d")

# Creating plot 
ax.scatter3D(a, b, c, color = "purple"); 
plt.title("Caballito Pepito") 

# Show plot 
plt.show()