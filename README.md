# Python Projects
This repository contains all Python projects for my personal interests. 

## House Prices (Kaggle)
It contains various machine learning algorithms (Linear Regression) on the dataset house prices obtained from Kaggle to perform prediction.

## Using ARIMA to forecast returns
This folder contains several ipynb notebooks containing detailed introduction to AR, MA, ARMA and ARIMA models. 
We also introduced and implemented several stationarity tests such as Augmented Dickey-Fuller (ADF) test and KPSS.  

## 1. Pricing of vanilla options in the Black-Scholes world and Monte Carlo Simulation.ipynb
This notebook is a simple Python's implemention of analytical formulas of vanilla options including European and America call and put options. It also contains formulas of binary put, call and forward contract.

We started with testing their consistencies to determine their correctness including put-call parity and relationship among all paramters in the Black-Scholes model.

Then we validated all formulas using the Monte Carlo method. 
We also implemented Euler-Maruyama method to simulate the dynamic of stock price under Geometric Brownian Motion Stochastic Differential Equation.

## 2. Vanilla Greeks using finite difference, pathwise derivative estimate and likelihood ratio methods.ipynb
This notebook performs sensitivity analysis on options' value by applying finite difference and Monte Carlo methods.
We also implemented pathwise derivative estimate and likelihood ratio methods to approximate option's greeks.

## 3. Hedging.ipynb (In progress)
This notebook simulates delta-hedging on European call option.
