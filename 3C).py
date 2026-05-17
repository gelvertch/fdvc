import numpy as np 
import matplotlib.pyplot as plt 
 
k = 9e9 
q = 1e-6 
 
# Lista de cargas: (q, x, y) 
cargas = [ 
    ( q, -1, -1), 
    ( q,  1,  1), 
    (-q,  1, -1), 
    (-q, -1,  1) 
] 
 
# Función campo total 
def campo_total(x, y): 
    Ex_total = 0 
    Ey_total = 0 
     
    for qi, xi, yi in cargas: 
        dx = x - xi 
        dy = y - yi 
        r = np.sqrt(dx**2 + dy**2) 
         
        Ex = k * qi * dx / r**3 
        Ey = k * qi * dy / r**3 
         
        Ex_total += Ex 
        Ey_total += Ey 
         
    return Ex_total, Ey_total 
 
# Parámetros 
ds = 0.05 
pasos = 400 
 
# Puntos iniciales 
puntos_iniciales = [ 
    (0, 0.5), 
    (0, -0.5), 
    (0.5, 0), 
    (-0.5, 0), 
    (0.7, 0.7), 
    (-0.7, -0.7) 
] 
 
plt.figure() 
 
for x, y in puntos_iniciales: 
     
    xs = [x] 
    ys = [y] 
     
    for i in range(pasos): 
         
        Ex, Ey = campo_total(x, y) 
        E = np.sqrt(Ex**2 + Ey**2) 
         
        x = x + (Ex/E)*ds 
        y = y + (Ey/E)*ds 
         
        xs.append(x) 
        ys.append(y) 
     
    plt.plot(xs, ys) 
 
# Dibujar cargas 
for qi, xi, yi in cargas: 
    plt.scatter(xi, yi) 
 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Líneas de campo - Cuatro cargas") 
plt.axis("equal") 
plt.grid() 
plt.show()