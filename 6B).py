import numpy as np 
 
# Constantes 
k = 8.987e9 
q = 1e-6 
Q = 1e-6 
R = 1 
n = 12 
 
Fx_total = 0 
Fy_total = 0 
 
for i in range(n): 
    theta = 2 * np.pi * i / n 
     
    # Saltamos la carga en 270° (6 en punto) 
    if np.isclose(theta, 3*np.pi/2): 
        continue 
     
    x = R * np.cos(theta) 
    y = R * np.sin(theta) 
     
    r = np.sqrt(x**2 + y**2) 
    F = k * q * Q / r**2 
     
    Fx = -F * (x / r) 
    Fy = -F * (y / r) 
Fx_total += Fx 
Fy_total += Fy 
F_total = np.sqrt(Fx_total**2 + Fy_total**2) 
print("Fuerza neta en x:", Fx_total) 
print("Fuerza neta en y:", Fy_total) 
print("Magnitud de la fuerza neta:", F_total)