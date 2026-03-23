import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# user input
ticker = input("Enter stock ticker: ")
years = int(input("Enter years to simulate: "))
n_sim = int(input("Enter number of simulations: "))

if years>10 :
    print("Too long horizon")
    exit()

# get data
data = yf.download(ticker, period="2y")

if data.empty:
    print("download failed")
    exit()

prices = data["Close"]
prices = prices.dropna().values.flatten()
if len(prices) < 10:
    print("not enough data")
    exit()

# returns
returns = np.diff(prices)/prices[:-1]
mu = returns.mean()
sigma = returns.std()

# settings
S0 = prices[-1]
T = 252*years
dt = 1/252

# simulation
paths = np.zeros((T, n_sim))
paths[0] = S0
for t in range (1, T):
    z = np.random.standard_normal(n_sim)
    paths[t] = paths[t-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)

final_prices = np.array(paths[-1])

# probability of losing money
prob_loss = np.mean(final_prices < S0)
print("Probability of loss: ", prob_loss)

# value at risk
var_95_price = np.percentile(final_prices, 5)
var_95_loss = S0 - var_95_price
print("95% VaR (price level): ", var_95_price)
print("95% VaR (loss): ", var_95_loss)

# expected shortfall (conditional VaR)
worst_cases = final_prices[final_prices <= var_95_price]
es_95 = S0 - worst_cases.mean()
print("Expected shortfall: ", es_95)

# probability of beating market return
market_return = 0.08
target_price = S0*(1 + market_return)
prob_beat_market = np.mean(final_prices > target_price)
print("Probability of beating the market: ", prob_beat_market)

# plot
plt.plot(paths)
plt.show()

#plot histogram with VaR line
plt.figure(figsize=(8,5))
plt.hist(final_prices, bins=40)

plt.axvline(S0, color="black", linestyle="dashed", label="Current price")
plt.axvline(var_95_price, color="red", linestyle="dashed", label="95% VaR")

plt.title("Distribution of Simulated Final Prices")
plt.xlabel("Price after {} years".format(years))
plt.ylabel("Frequency")
plt.legend()
plt.show()