import math 
# Constante de Coulomb 
k = 9e9 
# --------------------------------- 
# Definir cargas (ejemplo) 
# --------------------------------- 
cargas = [ 
(2e-6, 5, 1, 0), 
(-3e-6, -3, 4, 2) 
] 
# Punto donde calcular el campo 
x, y, z = 2, 6, 3 
# Inicializar componentes 
Ex_total = 0 
Ey_total = 0 
Ez_total = 0 
for q, xi, yi, zi in cargas: 
dx = x - xi 
dy = y - yi 
dz = z - zi 
r = math.sqrt(dx**2 + dy**2 + dz**2) 
Ex_total += k * q * dx / r**3 
Ey_total += k * q * dy / r**3 
Ez_total += k * q * dz / r**3 
# Magnitud del campo 
E_total = math.sqrt(Ex_total**2 + Ey_total**2 + Ez_total**2) 
# Ángulos con los ejes 
alpha = math.degrees(math.acos(Ex_total / E_total)) 
beta  = math.degrees(math.acos(Ey_total / E_total)) 
gamma = math.degrees(math.acos(Ez_total / E_total)) 
# Mostrar resultados 
print("Componentes del campo:") 
print("Ex =", Ex_total) 
print("Ey =", Ey_total) 
print("Ez =", Ez_total) 
print("\nMagnitud del campo =", E_total) 
print("\nÁngulos:") 
print("Con eje x =", alpha, "grados") 
print("Con eje y =", beta, "grados") 
print("Con eje z =", gamma, "grados")