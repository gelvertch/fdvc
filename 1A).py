
import matplotlib.pyplot as plt 
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
# Figura 
plt.figure() 
plt.scatter(x, y) 
plt.plot(x, y) 
plt.xlabel("Posición x (m)") 
plt.ylabel("Posición y (m)") 
plt.title("Trayectoria del electrón en campo eléctrico") 
plt.grid() 
# Guarda imagen para imprimir 
plt.savefig("figura_movimiento.png") 
plt.show()