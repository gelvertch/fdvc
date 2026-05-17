 import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
from scipy.integrate import odeint 
 
# 1. Constantes físicas 
k = 8.987e9       # Constante de Coulomb (N*m^2/C^2) 
e = 1.602e-19     # Carga elemental (C) 
m_e = 9.109e-31   # Masa del electrón (kg) 
Q = 100 * e       # Carga de los protones fijos 
d = 1e-10         # Distancia (1 Angstrom en metros) 
 
# 2. Ecuación diferencial del movimiento 
def ecuacion_movimiento(y, t): 
    x, v = y 
    # Distancia al cuadrado a las cargas fijas 
    r_sq = x**2 + (d/2)**2 
    # Fuerza neta en el eje x 
    fuerza_x = -2 * k * Q * e * x / (r_sq**1.5) 
    # Aceleración (F/m) 
    a = fuerza_x / m_e 
    return [v, a] 
 
# 3. Parámetros de la simulación 
# El electrón inicia desplazado 0.25 Angstroms desde el centro 
y0 = [0.25 * d, 0]  
# Tiempo simulado: 15 femtosegundos (suficiente para ver varios ciclos) 
t = np.linspace(0, 1.5e-14, 200)  
# Resolver la ecuación 
solucion = odeint(ecuacion_movimiento, y0, t) 
posiciones_x = solucion[:, 0] 
# 4. Configuración del entorno gráfico 
fig, ax = plt.subplots(figsize=(8, 6)) 
# Límites de los ejes (ajustados para ver el electrón y las cargas fijas) 
ax.set_xlim(-0.4 * d, 0.4 * d) 
ax.set_ylim(-0.6 * d, 0.6 * d) 
# Dibujar las líneas de los ejes 
ax.axhline(0, color='black', linewidth=0.5, linestyle='--') 
ax.axvline(0, color='black', linewidth=0.5, linestyle='--') 
# Dibujar las dos cargas positivas fijas en (0, d/2) y (0, -d/2) 
ax.scatter([0, 0], [d/2, -d/2], color='red', s=150, zorder=5, label='Cargas Fijas (+Q)') 
# Inicializar el punto que representará al electrón 
electron, = ax.plot([], [], 'bo', markersize=12, zorder=5, label='Electrón (-e)') 
ax.set_title('Dinámica del Electrón (Problema 4)', fontsize=14) 
ax.set_xlabel('Posición X (m)') 
ax.set_ylabel('Posición Y (m)') 
ax.legend(loc='upper right') 
ax.grid(True, alpha=0.3) 
# 5. Funciones de animación 
def init(): 
electron.set_data([], []) 
return electron, 
def update(frame): 
# Actualizar la posición x del electrón en cada fotograma 
# El eje y se mantiene en 0 
electron.set_data([posiciones_x[frame]], [0]) 
return electron, 
print("Generando animación... Por favor espera unos segundos.") 
# Crear la animación 
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, interval=30, blit=True) 
# 6. Guardar la animación como archivo GIF 
nombre_archivo = 'animacion_problema_4.gif' 
ani.save(nombre_archivo, writer='pillow', fps=30) 
 
print(f"La animación se ha guardado como '{nombre_archivo}'.") 
print("Búscalo en tu carpeta y ábrelo para ver el movimiento armónico.")