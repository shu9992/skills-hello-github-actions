import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000  # Total population
beta = 0.3  # Infection rate (probability of transmission per contact)
gamma = 0.1  # Recovery rate (probability of recovery per day)

# Initial conditions
S = N - 1  # Susceptible individuals
I = 1  # Initial infected individual
R = 0  # Recovered individuals

days = 100
S_list, I_list, R_list = [S], [I], [R]

# Simulation loop
for _ in range(days):
    new_infections = np.random.binomial(S, beta * (I / N))  # Probabilistic infection
    new_recoveries = np.random.binomial(I, gamma)  # Probabilistic recovery
    
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries
    
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(S_list, label='Susceptible', color='blue')
plt.plot(I_list, label='Infected', color='red')
plt.plot(R_list, label='Recovered', color='green')
plt.xlabel('Days')
plt.ylabel('Population')
plt.legend()
plt.title('SIR Model Simulation')
plt.show()

# Analysis
peak_infections = max(I_list)
total_infected = R_list[-1]

print(f'Peak number of infections: {peak_infections}')
print(f'Total number of people infected: {total_infected}')



