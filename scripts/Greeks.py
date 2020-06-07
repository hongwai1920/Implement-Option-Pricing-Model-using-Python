import numpy as np
from scipy.stats import norm

class Greeks:
    '''
    This class contains greeks of the European call and put options
    '''
    
    def __init__(self, S, K, r, d, sigma, T):
        '''
        Parameters:
        ===========
        S: stock price 
        K: strike price
        r: risk-free interest rate
        d: dividend 
        sigma: volatility (implied)
        T: time to maturity
        
        
        Returns: 
        ===========
        Forward price, vanilla European call and put option' prices, cash-or-nothing call and put options' prices,
        zero coupon bond and forward contract.
        '''
        
        self.S = S
        self.K = K
        self.r = r
        self.d = d
        self.sigma = sigma
        self.T = T
        
        self.d1 = (np.log(self.S/self.K) + (self.r - self.d + self.sigma**2 / 2) * self.T) / (self.sigma * np.sqrt(self.T))
        self.d2 = self.d1 - self.sigma * np.sqrt(self.T)
    
    def delta(self, option_type):
      if option_type == 'call':
        return norm.cdf(self.d1)
      elif option_type == 'put':
        return norm.cdf(self.d1) - 1
    
    def gamma(self):
        return norm.pdf(self.d1) / (self.S * self.sigma * np.sqrt(self.T))
    
    def vega(self):
        return self.S * np.sqrt(self.T) * norm.pdf(self.d1)
    
    def rho(self, option_type):
      if option_type == 'call':
        return self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(self.d2)
      elif option_type == 'put':
        return -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-self.d2)
    
    def theta(self, option_type):
      if option_type == 'call':
        return - self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2) - \
    (self.S * norm.pdf(self.d1) * self.sigma) / (2 * np.sqrt(self.T))
      elif option_type == 'put':
        return self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2) - \
    (self.S * norm.pdf(self.d1) * self.sigma) / (2 * np.sqrt(self.T))
    
    def get_all(self):
        call = 'call'
        put = 'put'
        delta_c = self.delta(call)
        delta_p = self.delta(put)
        gamma_c = self.gamma()
        gamma_p = self.gamma()
        vega_c = self.vega()
        vega_p = self.vega()
        rho_c = self.rho(call)
        rho_p = self.rho(put)
        theta_c = self.theta(call)
        theta_p = self.theta(put)
        greeks = { 'call': {'delta': delta_c, 'gamma': gamma_c, 'vega': vega_c, 'rho': rho_c, 'theta': theta_c}, 
                   'put' : {'delta': delta_p, 'gamma': gamma_p, 'vega': vega_p, 'rho': rho_p, 'theta': theta_p} }
        return greeks