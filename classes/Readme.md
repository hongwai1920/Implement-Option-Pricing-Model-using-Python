## GBM.py
1. `GBM_fd(S0, K, r, d, sigma, T, num_steps = 50, num_paths = 1, plot = False, seed = None)`
Simulate Geometric Brownian Motion Stochastic Differential Equation using Euler'Maruyama method (finite difference) to calculate terminal stock price

2. `GBM_formula(S0, K, mu, d, sigma, T, num_paths = 1, seed = None)` 
Simulate Geometric Brownian Motion using analytical formula

3. `monte_carlo(payoff)`
Monte Carlo method:
    1. Average all payoffs at time T
    2. Discount the average using continuously compounded risk-free interest rate
    
4. `black_scholes_monte_carlo_pricer(option_type, S0, K, r, d, sigma, T, num_steps = 100, num_paths = 20, full_list = False, seed = None)`
Apply Monte Carlo method to price Black Schole option

## Option.py
It contains 2 classes `Option` and a subclass `Greek`.

1. Class `Option` with methods 
    * `__init__(self, S, K, r, d, sigma, T)`, 
    * `forward_price(self)`, `european_call(self)`, 
    * `european_put(self)`, 
    * `binary_call(self, face_value)`, 
    * `binary_put(self, face_value)`, 
    * `zero_coupon_bond(self, face_value)`, 
    * `forward_contract(self)`, 
    * `print_all_values(self, face_value)`

2. Class `Greek(Option)` with methods 
    * delta(self)
    * gamma(self)
    * vega(self)
    * rho(self)
    * theta(self)
    * print_all(self)
  
## Payoff.py
It contains a class `Payoff` with methods 
* `__init__(self, TheOptionsType_, Strike_)`,
* `__call__(self,spot)`

## finite_difference_method.py
`finite_difference(f, e, second_order = False)`
Apply finite difference method to approximate derivative (first or second order)
