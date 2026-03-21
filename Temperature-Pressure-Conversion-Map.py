import numpy as np
import matplotlib.pyplot as plt

R = 8.314
Ea = 95000
k0 = 1e7

def k(T):
    return k0 * np.exp(-Ea / (R * T))

def conversion_kinetic(T, tau=1):
    return 1 - np.exp(-k(T) * tau)

def Keq(T):
    return np.exp(6000 / T - 6)

def conversion_equilibrium(T, P):
    K = Keq(T)
    return (K * P) / (1 + K * P)

def conversion_total(T, P, tau=1):
    return np.minimum(conversion_kinetic(T, tau), conversion_equilibrium(T, P))

T = np.linspace(400, 900, 100)
P = np.linspace(0.1, 10, 100)

T_grid, P_grid = np.meshgrid(T, P)
C = conversion_total(T_grid, P_grid)

plt.contourf(T_grid, P_grid, C, levels=20)
plt.colorbar(label="SO₂ Conversion")

plt.xlabel("Temperature (K)")
plt.ylabel("Pressure (atm)")
plt.title("Conversion Map (Temperature vs Pressure)")
plt.show()
