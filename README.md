# Implement Option Pricing Model using Python
This repository contains all my personal projects Option Pricing Model using Python.

## 1. Pricing of vanilla options in the Black-Scholes world and Monte Carlo Simulation.ipynb
This notebook is a simple Python's implemention of analytical formulas of vanilla options including European and America call and put options. It also contains formulas of binary put, call and forward contract.

We started with testing their consistencies to determine their correctness including put-call parity and relationship among all paramters in the Black-Scholes model.

Then we validated all formulas using the Monte Carlo method. 
The following is a plot of using Monte-Carlo method to price European put, call and binary put, call options.
<p align="center"> <img  src="https://github.com/hongwai1920/Implement-Option-Pricing-Model-using-Python/blob/master/Images/MC%20simulation%20to%20price%20options.png" width="700" height="400"></p> 


We also implemented Euler-Maruyama method to simulate the dynamic of stock price under Geometric Brownian Motion Stochastic Differential Equation.
The following is a plot its simulation.

<p align="center"> <img  src="https://github.com/hongwai1920/Implement-Option-Pricing-Model-using-Python/blob/master/Images/GBM%20simulation.png" width="800" height="500"></p> 


## 2. Vanilla Greeks using finite difference, pathwise derivative estimate and likelihood ratio methods.ipynb
This notebook performs sensitivity analysis on options' value by applying finite difference and Monte Carlo methods.
We also implemented numerical methods such as pathwise derivative estimate and likelihood ratio methods to approximate option's greeks.

## 3. Hedging.ipynb (In progress)
This notebook simulates delta-hedging on European call option.
