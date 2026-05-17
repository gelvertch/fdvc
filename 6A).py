import numpy as np 
 
# Constantes 
k = 8.987e9          # Constante de Coulomb (N·m²/C²) 
q = 1e-6             # Carga en cada vértice (C) 
Q = 1e-6             # Carga de prueba en el centro (C) 
R = 1                # Radio del polígono (m) 
n = 12               # Número de cargas 
 
# Inicializamos fuerza total 
Fx_total = 0 
Fy_total = 0 
 
# Calculamos la fuerza de cada carga 
for i in range(n): 
    theta = 2 * np.pi * i / n   # Ángulo de cada carga 
     
    # Posición de cada carga 
    x = R * np.cos(theta) 
    y = R * np.sin(theta) 
     
    # Distancia al centro 
    r = np.sqrt(x**2 + y**2) 
     
    # Magnitud de la fuerza 
    F = k * q * Q / r**2 
     
    # Componentes de la fuerza (hacia el centro) 
    Fx = -F * (x / r) 
    Fy = -F * (y / r) 
     
    # Sumamos componentes 
    Fx_total += Fx 
    Fy_total += Fy 
 
print("Fuerza neta en x:", Fx_total) 
print("Fuerza neta en y:", Fy_total) 
print("Magnitud de la fuerza neta:", np.sqrt(Fx_total**2 + Fy_total**2))