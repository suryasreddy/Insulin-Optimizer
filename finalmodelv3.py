import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the system of differential equations
def model(y, t, alpha, beta, K, C, lam):
    N, I, E = y
    dNdt = alpha * N * (1 - N / K) - beta * I * N
    if t % 1 <= 0.3:
        if(I - (N/C - lam) < 0):
            dIdt = -I
            dEdt = I
        else:
            dIdt = N/C - lam
            dEdt = lam
    else:
        dIdt = N / C
        dEdt = 0
    return [dNdt, dIdt, dEdt]

# Set the parameters
alpha = 0.035
beta = 1.8
K = 100000
C = 100000
lambdas = [0, 0.001, 0.0001, 0.00001]  # Different values of lambda

# 0.0005, 0.002, 0.006
# Initial conditions
N0 = 100
I0 = 0
E0 = 0  # Add initial condition for E
y0 = [N0, I0, E0]  # Update the initial conditions

# Time points
t = np.linspace(0, 100, 1000)

# Plot the results for different lambdas
plt.figure(figsize=(10, 6))
colors = ['blue', 'green', 'red', 'purple']
for i, lam in enumerate(lambdas):
    # Solve the system of differential equations
    solution = odeint(model, y0, t, args=(alpha, beta, K, C, lam))
    N, I, E = solution.T  # Transpose the solution for proper unpacking
    plt.plot(t, E, label=f'Insulin Extracted, $\lambda$ = {lam}', color=colors[i], linestyle='-.')

plt.xlabel('Time (minutes)', fontsize=14)
plt.ylabel('Extraction (mg/mL)', fontsize=14)
plt.title('Total Insulin Extracted for Different $\lambda$', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
