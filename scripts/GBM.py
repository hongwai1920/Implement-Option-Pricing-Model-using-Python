import numpy as np
import matplotlib.pyplot as plt

class PayOff:
    def __init__(self, TheOptionsType_, Strike_):
        '''
        Inputs:
        =========
        TheOptionsType_: string (European call, European put, Binary call, Binary put)
        Strike_: float strike price
        '''
        
        self.__TheOptionsType = TheOptionsType_
        self.__Strike = Strike_
        
    def __call__(self,spot):
        # Overloading the ( ) operator
        '''
        inputs:
        =========
        spot: numpy array of spot prices
        
        
        returns:
        =========
        payoff value for each option 
        '''
        
        if self.__TheOptionsType == 'European call':
            return np.maximum(spot - self.__Strike,0)
        elif self.__TheOptionsType == 'European put':
            return np.maximum(self.__Strike - spot,0)
        elif self.__TheOptionsType == 'Binary call':
            return np.piecewise(spot, [spot < self.__Strike, spot >= self.__Strike], [0, 1])
        elif self.__TheOptionsType == 'Binary put':
            return np.piecewise(spot, [spot <= self.__Strike, spot > self.__Strike], [1, 0])
        else:
            raise Exception('Unknown option type found.')


def GBM_fd(S0, r, d, sigma, T, num_steps = 50, num_paths = 1, plot = False, seed = None):
    '''
    Simulate Geometric Brownian Motion Stochastic Differential Equation using Euler'Maruyama method (finite difference)
    to calculate terminal stock price
    
    
    inputs:
    ===========
    
    S0: initial stock price
    r: risk-free interest rate
    d: dividend
    sigma: volatility 
    T: time to maturity 
    num_steps: numer of discretization steps
    num_paths: number of paths (integer)
    plot: plot of all paths generated
    seed: controls the random number generator np.random.RandomState().standard_normal()
    
    returns:
    =========
    numpy array of terminal stock prices of all paths
    '''
    
    dt = T / num_steps
    
    if num_paths == 1:
        S_path = [0] * (num_steps + 1)
    else:
        S_path = np.zeros((num_steps + 1, num_paths))
    
    S_path[0] = S0
    standard_normal_array = np.random.RandomState(seed).standard_normal((num_steps, num_paths))
    
    for i in range(1, num_steps + 1): 
        S_path[i] = S_path[i-1] + r * S_path[i-1] * dt + S_path[i-1] * sigma * np.sqrt(dt) * standard_normal_array[i-1]
        
    if plot:
        plt.figure(figsize= (10,6))
        plt.plot(S_path)
        plt.xlabel('number of discretization steps')
        plt.ylabel('Stock price');
    
    return S_path[-1]


def GBM_formula(S0, mu, d, sigma, T, num_paths = 1, seed = None):
    '''
    Simulate Geometric Brownian Motion using analytical formula
    
    
    inputs:
    ===========
    
    S0: initial stock price
    mu: drift
    d: dividend
    sigma: volatility 
    T: time to maturity 
    num_paths: number of paths (integer)
    seed: Control normal distribution generation
    
    returns
    ===========
    
    numpy array containing stock price(s) at time T
    '''
    
    return S0 * np.exp((mu - d - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * np.random.RandomState(seed).standard_normal(num_paths))
    
    
    
    


def monte_carlo(payoff):
    '''
    Monte Carlo method:
    1. Average all payoffs at time T
    2. Discount the average using continuously compounded risk-free interest rate
    
    inputs:
    ===========
    
    payoff: 1D numpy array of payoffs
    
    
    returns
    ===========
    integer approximate price of an option 
    '''
    
    return np.mean(payoff)
	
	
def black_scholes_monte_carlo_pricer(option_type, S0, K, r, d, sigma, T, num_steps = 100, num_paths = 20, full_list = False, seed = None):
    '''
    Apply Monte Carlo method to price Black Schole option
    
    inputs:
    ==========
    
    option_type: string (European call, European put, Binary call, Binary put)
    S0: initial stock price
    K: strike price
    r: risk-free interest rate
    d: dividend
    sigma: volatility 
    T: time to maturity 
    num_steps: numer of discretization steps
    num_paths: int number of paths
    full_list: boolean return full list of monte carlo values if True, otherwise return the last value
    seed: None or int
    
    returns:
    ==========
    
    Black-Scholes price of the option using monte carlo method
    '''
    
    if not full_list:
        ST = GBM_fd(S0, r, d, sigma, T, num_steps, 2**num_paths, False, seed)
        payoff = np.exp(- r * T) * PayOff(option_type, K)(ST)
        return monte_carlo(payoff)
    
    mc = [0] * num_paths
    
    for num_path in range(1, num_paths + 1):
        ST = GBM_fd(S0, r, d, sigma, T, num_steps, 2**num_path, False, seed)
        payoff = np.exp(- r * T) * PayOff(option_type, K)(ST)
        mc[num_path - 1] = monte_carlo(payoff)
    
    return mc
