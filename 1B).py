import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation, PillowWriter 

# Constantes 
q = -1.602e-19 
m = 9.11e-31 
E = 400 
v0x = 3e6 

# Aceleración 
a = q * E / m 

# Tiempo 
t_ns = np.arange(0, 3001, 100) 
t = t_ns * 1e-9 

# Posiciones 
x = v0x * t 
y = 0.5 * a * t**2 

# Configuración gráfica 
fig, ax = plt.subplots() 
ax.set_xlim(0, max(x)*1.1) 
ax.set_ylim(min(y)*1.1, 0) 
ax.set_xlabel("Posición x (m)") 
ax.set_ylabel("Posición y (m)") 
ax.set_title("Animación del movimiento del electrón") 
line, = ax.plot([], [], 'o-') 

def update(frame): 
    
    line.set_data(x[:frame], y[:frame]) 
    return line, 

ani = FuncAnimation(fig, update, frames=len(x), interval=200) 

# Guarda animación 
ani.save("animacion_electron.gif", writer=PillowWriter(fps=5)) 
plt.show()