import math 
# Constante de Coulomb 
k = 9e9 
# ----------------------------- 
# Cargas (puedes cambiar valores si quieres) 
# ----------------------------- 
q1 = 2e-6 
x1, y1 = 5, 1 
q2 = -3e-6 
x2, y2 = -3, 4 
# ----------------------------- 
# Punto donde calcular el campo 
# ----------------------------- 
x, y = 2, 6 
# ----------------------------- 
# Campo debido a q1 
# ----------------------------- 
dx1 = x - x1 
dy1 = y - y1 
r1 = math.sqrt(dx1**2 + dy1**2) 
Ex1 = k * q1 * dx1 / r1**3 
Ey1 = k * q1 * dy1 / r1**3 
# ----------------------------- 
# Campo debido a q2 
# ----------------------------- 
dx2 = x - x2 
dy2 = y - y2 
r2 = math.sqrt(dx2**2 + dy2**2) 
Ex2 = k * q2 * dx2 / r2**3 
Ey2 = k * q2 * dy2 / r2**3 
# ----------------------------- 
# Campo total 
# ----------------------------- 
Ex_total = Ex1 + Ex2 
Ey_total = Ey1 + Ey2 
# Magnitud 
E_total = math.sqrt(Ex_total**2 + Ey_total**2) 
# Dirección (ángulo con eje x) 
angulo = math.degrees(math.atan2(Ey_total, Ex_total)) 
# Resultados 
print("Magnitud del campo =", E_total, "N/C") 
print("Dirección =", angulo, "grados respecto al eje x")