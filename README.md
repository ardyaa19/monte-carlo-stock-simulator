Monte Carlo Stock Price Simulator with Risk Analytics

This project implements a Monte Carlo simulation framework to model possible future price paths of a stock using the Geometric Brownian Motion (GBM) assumption.
It demonstrates practical application of probability modeling, stochastic processes, and numerical simulation in financial analysis.

Features: 
1. Historic price retrieval using Yahoo Finance API
2. Simulation of multiple stochastic price paths
3. User defined inputs
4. Risk analytics include: probability of loss, value at risk (VaR), expected shortfall (ES), probability of outperforming a benchmark return
5. Visualizations: simulated price trajectory plots, histogram of final price distribution with risk thresholds

<img width="1282" height="1095" alt="image" src="https://github.com/user-attachments/assets/ed813da3-feb3-4f1c-ace1-97fd0256d33b" />
<img width="1599" height="1124" alt="image" src="https://github.com/user-attachments/assets/37f82953-4bbf-428f-becf-f1dc53cb8a20" />
(Images represent graphs plotted for stock ticker AAPL, duration 4 years, 500 simulated paths)

Limitations:
1. Assumes constant drift and volatility
2. Does not account for market jumps/ regime changes
3. Relies on Yahoo Finance data availability

Future improvements:
1. Use log-return modeling and parameter annualization
2. Compare multiple assets simultaneously

Author:
Aradhya Kashyap
UG Mathematics & Computing
