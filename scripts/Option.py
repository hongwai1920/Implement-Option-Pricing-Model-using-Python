import numpy as np
from scipy.stats import norm

class Option:
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
    
    def forward_price(self):
        '''
        output forward price
        '''        
        return self.S * np.exp(self.r * self.T)
    
    def european_call(self):
        '''
        output vanilla European call option's price using Black-Scholes formula 
        '''        
        return self.S * np.exp(-self.d * self.T) * norm.cdf(self.d1) - self.K * np.exp(-self.r * self.T)*norm.cdf(self.d2)
    
    def european_put(self):
        '''
        output vanilla European put option's price using Black-Scholes formula 
        '''        
        return self.K * np.exp(-self.r * self.T)*norm.cdf(-self.d2) - self.S * np.exp(-self.d * self.T)*norm.cdf(-self.d1)
    
    def binary_call(self, face_value):
        '''
        output cash-or-nothing call option's price
        '''
        return face_value * np.exp(-self.r * self.T) * norm.cdf(self.d2)

    def binary_put(self, face_value):
        '''
        ouput cash-or-nothing put option's price
        '''
        return face_value * np.exp(-self.r * self.T) * norm.cdf(-self.d2)
    
    def zero_coupon_bond(self, face_value):
        '''
        output zero coupon bond's price based on the face value
        '''
        return face_value * np.exp(-self.r * self.T)
    
    def forward_contract(self):
        '''
        output forward contract's value
        '''
        return self.S * np.exp(-self.d * self.T) - self.K * np.exp(-self.r * self.T)
    
    def print_all_values(self, face_value):
        '''
        print prices of all options and zero coupon bond
        '''
        print('Forward price: {}'.format(self.forward_price()))
        print('European call: {}'.format(self.european_call()))
        print('European put: {}'.format(self.european_put()))
        print('Binary call: {}'.format(self.binary_call(face_value = 1)))
        print('Binary put: {}'.format(self.binary_put(face_value = 1)))
        print('Forward contract: {}'.format(self.forward_contract()))


class Greeks(Option):
    '''
    This class contains greeks of the European call and put options
    '''
    
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