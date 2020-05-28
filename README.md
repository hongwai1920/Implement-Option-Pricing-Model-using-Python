# Implement Option Pricing Model using Python
This repository contains all my personal projects Option Pricing Model using Python.

## House Prices (Kaggle)
It contains various machine learning algorithms implementations (Linear Regression with Regularization) on the dataset house prices obtained from Kaggle to perform prediction.
Public score from Kaggle is indiacted beside the algorithms.

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
