import scipy.optimize as opt

# Variables: 
# x = gramos de T
# y = gramos de D
c = [1.0, 1.2] 

# Restricciones. Se multiplican por -1 para garantizar la desigualdad <= .
A = [
    [-0.1 / 30, -0.25 / 30],     # Tiamina
    [-1.0 / 30, -0.25 / 30],     # Niacina
    [-110.0 / 30, -120.0 / 30]   # Calorías
]
b = [-1, -5, -400]

# No negatividad
bounds = [(0, None), (0, None)]

res = opt.linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

print(f"Minimum cost: ${res.fun:.2f}")
print(f"Grams of cereal T: {res.x[0]:.2f}")
print(f"Grams of cereal D: {res.x[1]:.2f}")
