import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint 
 
# 1. Constantes físicas 
k = 8.987e9       # N*m^2/C^2 
e = 1.602e-19     # C 
m = 9.109e-31     # Usaremos la masa del electrón como referencia (masa m) 
Q = 100 * e       # Carga fija 
q = e             # Carga móvil 
d = 1e-10         # Distancia de separación (1 Angstrom) 
 
# 2. Definición del sistema dinámico 
def sistema_movimiento_5a(state, t): 
    x, v = state 
    # Evitamos divisiones por cero con un pequeño margen de seguridad 
    limite = 0.49 * d  
    if abs(x) >= limite: 
        return [v, 0] # La partícula llegó al límite 
     
    # Fuerza neta: F = F_izq - F_der 
    # F_izq = k*Q*q / (d/2 + x)^2 
    # F_der = k*Q*q / (d/2 - x)^2 
    fuerza_x = k * Q * q * (1/(d/2 + x)**2 - 1/(d/2 - x)**2) 
     
    
    a = fuerza_x / m 
    return [v, a] 

# 3. Simulación 
# Desplazamiento inicial muy pequeño para observar el M.A.S. 
x0 = [0.01 * d, 0]  
t = np.linspace(0, 1e-13, 100)  
solucion = odeint(sistema_movimiento_5a, x0, t) 
posiciones = solucion[:, 0] 
velocidades = solucion[:, 1] 

# 4. Resultados (primeras 30 posiciones) 
print(f"{'Punto':<10} | {'Posición (m)':<20} | {'Velocidad (m/s)':<20}") 
for i in range(30): 
    
    print(f"{i+1:<10} | {posiciones[i]:<20.4e} | {velocidades[i]:<20.4e}") 

# 5. Gráfica 
plt.figure(figsize=(10, 5)) 
plt.plot(t * 1e15, posiciones * 1e10, 'ro-', markersize=4, label='Posición (Å)') 
plt.title('Oscilación de la carga positiva (5a)') 
plt.xlabel('Tiempo (femtosegundos)') 
plt.ylabel('Posición (Å)') 
plt.grid(True) 
plt.legend() 
plt.show()