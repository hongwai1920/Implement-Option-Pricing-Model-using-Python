import numpy as np

class BinomialTree:
  def __init__(self, S0, r, d, sigma, T):
    self.S0 = S0
    self.r = r
    self.d = d
    self.sigma = sigma
    self.T = T

  def generate_tree(self, N, model = 'crr'):
    '''
    generate an upper triangular matrix recording all possible price paths 
    by using up and down moves only S0, sigma, T and N.

    inputs: 
    N: number of levels of node
    mode: up and down multipliers are decided by either crr or GBM model

    Outputs:
    dt: T / N
    up: up-move multiplier
    down: down-move multiplier
    price_tree: numpy array containing prices

    '''

    dt = self.T / N

    # Construct a price tree using numpy array
    # Given N periods, there are (N+1) nodes in total 
    # Period starts from 0 (current price)
    price_tree = np.zeros((N+1,N+1))

    if model == 'crr':
      # Cox, Ross & Rubinstein (CRR) formulas are
      # $$up = e^{\sigma\sqrt{\Delta t}} \quad \text{and} \quad down = e^{-\sigma\sqrt{\Delta  t}} =\frac{1}{up}.$$
      # Note that ud = 1 
      up = np.exp(self.sigma * np.sqrt(dt))
      down = 1 / up 

    elif model == 'gbm':
      # Geometric Brownian Motion (GBM) formulas are
      # $$up = e^{ (r - d - 0.5 \sigma^2) \Delta t + \sigma\sqrt{\Delta t}} \quad \text{and} \quad down = e^{ (r - d - 0.5 \sigma^2) \Delta t - \sigma\sqrt{\Delta t}}.$$
      # Note that ud \neq 1 
      # Simplifying the discrete GBM gives
      # S_{j\Delta t} = S_{(j-1)\Delta t} exp( ( r - 0.5 \sigma^2)\Delta t + \sigma \sqrt{\Delta t}Z_j)

      det_comp = (self.r - self.d - 0.5 * self.sigma ** 2) * dt
      stoc_comp = self.sigma * np.sqrt(dt)

      up = np.exp(det_comp + stoc_comp)
      down = np.exp(det_comp - stoc_comp)

    # concepts: at [i,j]-th entry of the tree, 
    # number of up + number of down = j (col)
    # number of down = i (row)
    # So, number of up = j - i
    # Hence, [i,j]-th entry = S0 x up^{j-i} x down^i

    size = (N+1, N+1)
    f = lambda i,j : up**(j-i) * down**i if i <= j else 0
    price_tree = self.S0 * np.fromfunction(np.vectorize(f), size)

    return dt, up, down, price_tree

  def option_price(self, num_sim, payoff, model = 'crr', exercise_style = 'European'):
    '''
    inputs:
    num_sim: number of simulations 
    payoff: (lambda function) option's payoff function at maturity
    model: either crr or gbm
    exercise_style: either European or American

    output:
    list of (should converge) prices
    '''
    prices = [0] * num_sim

    for a in range(1, num_sim + 1):
      N = 2 ** a
      dt, up, down, price_tree = self.generate_tree(N, model = model) 

      # price option
      if model == 'crr':
        # To ensure no-arbitrage, we must have 
        # 0 <= p_tilde <= 1, that is, d <= e^{r\delta t} <= u, that is, 
        # e^{-sigma \sqrt{\Delta t}} <= e^{r\delta t} <= e^{sigma \sqrt{\Delta t}}, that is, 
        # -sigma <= r \sqrt{T/N} <= sigma
        # Since the LHS is always true, so we just need to check r \sqrt{T/N} <= sigma
        assert self.r * np.sqrt(self.T/N) <= self.sigma, ' r \sqrt{T/N} <= sigma is not fulfilled, leading to arbitrage'
      
      p_tilde = (np.exp( (self.r - self.d) * dt ) - down) / (up - down)
      cash_flows = np.zeros((N+1,N+1))
      cash_flows[:, -1] =  payoff(price_tree[:, -1])

      if exercise_style == 'European':
        for j in range(N-1, -1, -1):
          for i in range(j+1):
            cash_flows[i,j] = np.exp(-self.r * dt) * (p_tilde * cash_flows[i,j+1] + (1-p_tilde) * cash_flows[i+1,j+1] )

      elif exercise_style == 'American':
        exercise_value = payoff(price_tree)
        for j in range(N-1, -1, -1):
          for i in range(j+1):
            cash_flows[i,j] = np.maximum(exercise_value[i,j], np.exp(-self.r * dt) * (p_tilde * cash_flows[i,j+1] + (1-p_tilde) * cash_flows[i+1,j+1] ))

      prices[a - 1] = cash_flows[0,0]

    return prices