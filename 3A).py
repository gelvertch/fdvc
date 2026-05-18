import numpy as np 
import matplotlib.pyplot as plt 
# Constante de Coulomb 
k = 9e9 
# Carga puntual (ejemplo) 
q = 1e-6   # 1 microCoulomb 
# Posición de la carga 
xq, yq = 0, 0 
# Punto inicial de la línea de campo 
x, y = 1, 0 
# Paso pequeño 
ds = 0.05 
# Número de pasos 
pasos = 200 
# Guardar trayectoria 
xs = [x] 
ys = [y] 
for i in range(pasos): 
dx = x - xq 
dy = y - yq    
    r = np.sqrt(dx**2 + dy**2) 
     
    Ex = k * q * dx / r**3 
    Ey = k * q * dy / r**3 
     
    E = np.sqrt(Ex**2 + Ey**2) 
     
    # Incrementos según el enunciado 
    x = x + (Ex/E)*ds 
    y = y + (Ey/E)*ds 
     
    xs.append(x) 
    ys.append(y) 
 
# Graficar línea de campo 
plt.figure() 
plt.plot(xs, ys) 
plt.scatter(xq, yq)  # posición de la carga 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Línea de campo eléctrico") 
plt.axis("equal") 
plt.grid() 
plt.show()