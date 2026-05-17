import numpy as np 
import matplotlib.pyplot as plt 
 
k = 9e9 
 
# Cargas 
q1 = 1e-6     # positiva 
q2 = -1e-6    # negativa 
 
# Posiciones 
x1, y1 = -1, 0 
x2, y2 =  1, 0 
 
# Función para calcular campo total 
def campo_total(x, y): 
     
    # Campo de q1 
    dx1 = x - x1 
    dy1 = y - y1 
    r1 = np.sqrt(dx1**2 + dy1**2) 
     
    Ex1 = k*q1*dx1/r1**3 
    Ey1 = k*q1*dy1/r1**3 
     
    # Campo de q2 
    dx2 = x - x2 
    dy2 = y - y2 
    r2 = np.sqrt(dx2**2 + dy2**2) 
     
    Ex2 = k*q2*dx2/r2**3 
    Ey2 = k*q2*dy2/r2**3 
     
    return Ex1+Ex2, Ey1+Ey2 
 
 
# Parámetros 
ds = 0.05 
pasos = 300 
 
# Puntos iniciales alrededor de la carga positiva 
puntos_iniciales = [(-1,0.5), (-1,-0.5), (-0.5,0.5), (-0.5,-0.5)] 
 
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
plt.scatter(x1, y1) 
plt.scatter(x2, y2) 
 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Líneas de campo - Dipolo eléctrico") 
plt.axis("equal") 
plt.grid() 
plt.show()