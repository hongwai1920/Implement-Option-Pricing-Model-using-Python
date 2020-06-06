# Implement Option Pricing Model using Python
This repository contains all my personal projects Option Pricing Model using Python.

## [1. Pricing of vanilla options in the Black-Scholes world and Monte Carlo Simulation.ipynb](https://nbviewer.jupyter.org/github/hongwai1920/Implement-Option-Pricing-Model-using-Python/blob/master/1.%20Pricing%20of%20vanilla%20options%20in%20the%20Black-Scholes%20world%20and%20Monte%20Carlo%20Simulation.ipynb)
This notebook is a simple Python's implemention of analytical formulas of vanilla options including European and America call and put options. It also contains formulas of binary put, call and forward contract.

We started with testing their consistencies to determine their correctness including put-call parity and relationship among all paramters in the Black-Scholes model.

Then we validated all formulas using the Monte Carlo method. 
The following is a plot of using Monte-Carlo method to price European put, call and binary put, call options.
<p align="center"> <img  src="https://github.com/hongwai1920/Implement-Option-Pricing-Model-using-Python/blob/master/Images/MC%20simulation%20to%20price%20options.png" width="700" height="400"></p> 


We also implemented Euler-Maruyama method to simulate the dynamic of stock price under Geometric Brownian Motion Stochastic Differential Equation.
The following is a plot its simulation.

<p align="center"> <img  src="https://github.com/hongwai1920/Implement-Option-Pricing-Model-using-Python/blob/master/Images/GBM%20simulation.png" width="800" height="500"></p> 


## [2. Vanilla Greeks using finite difference, pathwise derivative estimate and likelihood ratio methods.ipynb](https://nbviewer.jupyter.org/github/hongwai1920/Implement-Option-Pricing-Model-using-Python/blob/master/2.%20Vanilla%20Greeks%20using%20finite%20difference%2C%20pathwise%20derivative%20estimate%20and%20likelihood%20ratio%20methods.ipynb)
This notebook performs sensitivity analysis on options' value by applying finite difference and Monte Carlo methods.
We also implemented numerical methods such as pathwise derivative estimate and likelihood ratio methods to approximate option's greeks.

For example, to calculate delta of an European call option, pathwise derivative estimate asserts that 
<p align="center"> <img  src="https://latex.codecogs.com/svg.latex?\frac{\partial&space;c}{\partial&space;S_0}&space;=&space;\frac{\partial}{\partial&space;S_0}&space;\mathbb{E}[e^{-rT}(S_T-K)^&plus;]&space;=&space;\mathbb{E}\left[&space;\frac{\partial}{\partial&space;S_0}&space;e^{-rT}(S_T-K)^&plus;&space;\right]&space;=&space;\mathbb{E}&space;\left[e^{-rT}&space;1_{\{S_T>K\}}&space;\frac{\partial&space;S_T}{\partial&space;S_0}&space;\right]&space;=&space;\mathbb{E}&space;\left[&space;e^{-rT}&space;1_{\{S_T>K\}}&space;e^{(r-d&space;-&space;\frac{1}{2}&space;\sigma^2)T&space;&plus;&space;\sigma&space;\sqrt{T}&space;Z}&space;\right]&space;=&space;\mathbb{E}&space;\left[&space;e^{-rT}&space;1_{\{S_T>K\}}&space;\frac{S_T}{S_0}\right]," title="\frac{\partial c}{\partial S_0} = \frac{\partial}{\partial S_0} \mathbb{E}[e^{-rT}(S_T-K)^+] = \mathbb{E}\left[ \frac{\partial}{\partial S_0} e^{-rT}(S_T-K)^+ \right] = \mathbb{E} \left[e^{-rT} 1_{\{S_T>K\}} \frac{\partial S_T}{\partial S_0} \right] = \mathbb{E} \left[ e^{-rT} 1_{\{S_T>K\}} e^{(r-d - \frac{1}{2} \sigma^2)T + \sigma \sqrt{T} Z} \right] = \mathbb{E} \left[ e^{-rT} 1_{\{S_T>K\}} \frac{S_T}{S_0}\right],"></p> 
Therefore, to calculate the delta, one can apply Monte-Carlo method to calculate the final expectation.

On the other hand, the likelihood ratio method asserts that 
<p align="center"> <img  src="https://latex.codecogs.com/svg.latex?\Delta&space;=&space;\frac{d}{d&space;S(0)}\mathbb{E}&space;[e^{-rT}&space;(S_T-K)^&plus;]&space;=&space;\mathbb{E}&space;\left[&space;e^{-rT}(S_T-K)^&plus;&space;\left(&space;\frac{&space;\ln&space;\left(&space;\frac{S(T)}{S(0)}&space;\right)&space;-&space;(r&space;-&space;\frac{1}{2}\sigma^2)T&space;}{&space;S(0)\sigma^2&space;T}&space;\right)&space;\right]." title="\Delta = \frac{d}{d S(0)}\mathbb{E} [e^{-rT} (S_T-K)^+] = \mathbb{E} \left[ e^{-rT}(S_T-K)^+ \left( \frac{ \ln \left( \frac{S(T)}{S(0)} \right) - (r - \frac{1}{2}\sigma^2)T }{ S(0)\sigma^2 T} \right) \right]."></p> 
Therefore, one can use the Monte-Carlo method again to calculate the final expectation.

## [4. Recombining_Trees.ipynb](https://nbviewer.jupyter.org/github/hongwai1920/Implement-Option-Pricing-Model-using-Python/blob/master/4.%20Recombining_Trees.ipynb)
This notebook uses various binomial trees simulation including CRR and discretize GBM to price options. 
