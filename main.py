import numpy as np
from scipy.optimize import minimize

# Initial data
income = [100] * 5
expense = [-200] * 5
net = np.array(income) + np.array(expense)
initial_invest = 100
return_rate = 0.05

# Define the objective function to find the scale_factor that makes the last investment just above 0
def objective(scale_factor):
    invest = initial_invest
    for i in range(len(income)):
        net = income[i] + expense[i]*scale_factor
        invest = invest*(1+return_rate)+net
    return abs(invest) # we want to minimize the absolute difference from 0

# Initial guess for scale_factor
initial_scale_factor = 1

# find optimal scale_factor
result = minimize(objective, initial_scale_factor, method='Nelder-Mead')

# extract the optimal scale factor
optimal_scale_factor = result.x[0]
print(f"Optimal Scale Factor: {optimal_scale_factor}")


# Verify the results by calculating the investment series with the optimal scale factor
invest = initial_invest
print(f"\nIncome\tExpense\tNet\tScale Factor\tInitial Invest\tInvest\tReturn Rate")
for i in range(len(income)):
    net = income[i] + expense[i] * optimal_scale_factor
    invest = invest * (1 + return_rate) + net
    print(f"{income[i]}\t{expense[i]}\t{net:.4f}\t{optimal_scale_factor:.6f}\t{initial_invest}\t{invest:.4f}\t{return_rate}")


test_rest = objective(0.6154874801635739)
print("test_rest", test_rest)
