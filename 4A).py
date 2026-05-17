import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint 
 
# 1. Definición de constantes físicas (en unidades SI) 
k = 8.987e9       # N*m^2/C^2 
e = 1.602e-19     # C 
m_e = 9.109e-31   # kg 
Q = 100 * e       # Carga de los protones 
d = 1e-10         # 1 Angstrom (m) 
 
# 2. Definición de la ecuación diferencial 
def sistema_movimiento(state, t): 
    x, v = state 
    # Distancia al cuadrado desde el electrón a una de las cargas fijas 
    r_sq = x**2 + (d/2)**2 
    # Fuerza neta restauradora en x 
    fuerza_x = -2 * k * Q * e * x / (r_sq**1.5) 
     
    # Aceleración a = F/m 
    a = fuerza_x / m_e 
    return [v, a] 
 
# 3. Condiciones iniciales y tiempo 
# Desplazamos ligeramente el electrón (ej. 0.2*d) para que inicie la oscilación 
x0 = [0.2 * d, 0]  
# Generamos un vector de tiempo (escala de femtosegundos) 
t = np.linspace(0, 5e-15, 100)  
 
# Resolver el sistema 
solucion = odeint(sistema_movimiento, x0, t) 
posiciones = solucion[:, 0] 
velocidades = solucion[:, 1] 
 
# 4. Mostrar las primeras 30 ubicaciones 
print("Primeras 30 ubicaciones del electrón:") 
print(f"{'Punto':<10} | {'Posición (m)':<20} | {'Velocidad (m/s)':<20}") 
for i in range(30): 
    print(f"{i+1:<10} | {posiciones[i]:<20.4e} | {velocidades[i]:<20.4e}") 
 
# 5. Graficar resultados 
plt.figure(figsize=(10, 5)) 
plt.plot(t * 1e15, posiciones * 1e10, 'bo-', markersize=4, label='Posición (Angstroms)') 
plt.title('Movimiento oscilatorio del electrón (4a)') 
plt.xlabel('Tiempo (femtosegundos)') 
plt.ylabel('Posición (Å)') 
plt.grid(True) 
plt.legend() 
plt.show()