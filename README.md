# Quantitative-Finance-Computer-Projects (Python) 
This repository contains all quantitative finance computer projects that I have done so far using Python.

## Using ARIMA to forecast returns
It contains several ipynb notebooks containing detailed introduction to AR, MA, ARMA and ARIMA model. Several tests such as Augmented Dickey Fuller test, Unit test for stationarity are introduced as well.  

## 1. Pricing of vanilla options in the Black-Scholes world and Monte Carlo Simulation.ipynb
This notebook is a simple Python's example of implementing analytical formulas of vanilla options including European and America call and put options. It also contains formulas f binary put, call and forward contract.

We started with testing their consistencies to determine their correctness including put-call parity and relationship among all paramters in the Black-Scholes model.

Then we validated all formulas using the Monte Carlo method. 
We also implemented Euler-Maruyama method to simulate the dynamic of stock price in Geometric Brownian Motion Stochastic Differential Equation.

## 2. 2. Vanilla Greeks using finite difference, pathwise derivative estimate and likelihood ratio methods.ipynb
This notebook applies finite difference and Monte Carlo methods to perform sensitivity analysis on option value.
We also implemented pathwise derivative estimate and likelihood ratio methods to approximate option's greeks.
