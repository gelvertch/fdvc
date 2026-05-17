import math 
# Constante de Coulomb 
k = 9e9   # N·m²/C² 
# ----------------------------- 
# Definir cargas (mínimo 2) 
# ----------------------------- 
q1 = 2e-6 
x1, y1 = 0, 0 
q2 = -3e-6 
x2, y2 = 3, 0 
# ----------------------------- 
# Punto donde calcular el campo 
# ----------------------------- 
x, y = 1, 2 
# ----------------------------- 
# Campo debido a carga 1 
# ----------------------------- 
dx1 = x - x1 
dy1 = y - y1 
r1 = math.sqrt(dx1**2 + dy1**2) 
Ex1 = k * q1 * dx1 / r1**3 
Ey1 = k * q1 * dy1 / r1**3 
# ----------------------------- 
# Campo debido a carga 2 
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
# Ángulo respecto al eje x (en grados) 
angulo = math.degrees(math.atan2(Ey_total, Ex_total)) 
# ----------------------------- 
# Resultados 
# ----------------------------- 
print("Campo eléctrico en el punto (", x, ",", y, ")") 
print("Ex =", Ex_total, "N/C") 
print("Ey =", Ey_total, "N/C") 
print("Magnitud =", E_total, "N/C") 
print("Ángulo =", angulo, "grados")