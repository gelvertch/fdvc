import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
from scipy.integrate import odeint 

# 1. Constantes físicas 
k = 8.987e9       # Constante de Coulomb (N*m^2/C^2) 
e = 1.602e-19     # Carga elemental (C) 
Q = 100 * e       # Cargas fijas (+Q) 
q = e             # Carga móvil (+q) 
d = 1e-10         # Distancia de separación total (1 Angstrom) 
m = 1e-27         # Masa de prueba (ajustada para ver la oscilación claramente) 

# 2. Ecuación diferencial del movimiento 
def ecuacion_movimiento_5(y, t): 
    x, v = y 
    
    # Límite de seguridad para evitar que la carga móvil colisione con las fijas 
    # (Evita la división por cero si x = d/2 o x = -d/2) 
    limite = 0.48 * d 
    x_seguro = np.clip(x, -limite, limite) 
    
    # Fuerza repulsiva de la carga izquierda (empuja a la derecha, +) 
    f_izq = k * Q * q / (d/2 + x_seguro)**2 
    # Fuerza repulsiva de la carga derecha (empuja a la izquierda, -) 
    f_der = k * Q * q / (d/2 - x_seguro)**2 
    
    # Fuerza neta en el eje x 
    fuerza_x = f_izq - f_der 
    
    # Aceleración (F/m) 
    a = fuerza_x / m 
    return [v, a] 

# 3. Parámetros de la simulación 
# La carga inicia desplazada 0.15 Angstroms desde el centro hacia la derecha 
y0 = [0.15 * d, 0]  
# Tiempo simulado (ajustado a la masa de prueba para ver los ciclos) 
t = np.linspace(0, 3e-13, 200)  

# Resolver la ecuación 
solucion = odeint(ecuacion_movimiento_5, y0, t) 
posiciones_x = solucion[:, 0] 

# 4. Configuración del entorno gráfico 
fig, ax = plt.subplots(figsize=(9, 4)) 
# Límites de los ejes 
ax.set_xlim(-0.6 * d, 0.6 * d) 
ax.set_ylim(-0.3 * d, 0.3 * d) 
# Dibujar el eje x (donde ocurre el movimiento) 
ax.axhline(0, color='black', linewidth=1) 
# Dibujar las dos cargas positivas fijas en (-d/2, 0) y (d/2, 0) 
ax.scatter([-d/2, d/2], [0, 0], color='darkred', s=200, zorder=5, label='Cargas Fijas (+Q)') 
# Inicializar el punto que representará la carga móvil 
carga_movil, = ax.plot([], [], 'ro', markersize=12, zorder=6, label='Carga Móvil (+q)') 
ax.set_title('Dinámica de la Carga Positiva (Problema 5)', fontsize=14) 
ax.set_xlabel('Posición X (m)') 
ax.legend(loc='upper right') 
ax.grid(True, alpha=0.3) 
# Ocultar el eje Y ya que el movimiento es 1D 
ax.get_yaxis().set_visible(False) 

# 5. Funciones de animación 
def init(): 
    
    carga_movil.set_data([], []) 
    return carga_movil, 

def update(frame): 
    
    # Actualizar la posición x de la carga móvil 
    carga_movil.set_data([posiciones_x[frame]], [0]) 
    return carga_movil, 

print("Generando animación del Problema 5... Por favor espera.") 
# Crear la animación 
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, interval=30, blit=True) 

# 6. Guardar la animación como archivo GIF 
nombre_archivo = 'animacion_problema_5.gif' 
ani.save(nombre_archivo, writer='pillow', fps=30) 
print(f"La animación se ha guardado como '{nombre_archivo}'.") 
print("Puedes abrir el archivo en tu computadora para visualizar el resultado.")