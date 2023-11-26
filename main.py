import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_bitcoin_data(ticker, start_date, end_date):
    bitcoin_data = yf.download(ticker, start=start_date, end=end_date)
    return bitcoin_data['Close']

def calculate_sma(data, window_size):
    return data.rolling(window=window_size).mean()

def calculate_ema(data, alpha):
    return data.ewm(alpha=alpha, adjust=False).mean()

def plot_data(data, sma, ema):
    plt.figure(figsize=(10, 6))
    plt.plot(data, label='Bitcoin Price', color='blue')
    plt.plot(sma, label=f'SMA ({window_size} days)', color='orange')
    plt.plot(ema, label=f'EMA ({alpha} smoothing)', color='green')
    plt.title('Bitcoin Price with SMA and EMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    plt.draw()
    plt.waitforbuttonpress()

if __name__ == "__main__":
    ticker = 'BTC-USD'
    start_date = '2023-10-09'
    end_date = '2023-11-17'
    window_size = 20  # Adjust the window size for SMA
    alpha = 0.2  # Adjust alpha for EMA smoothing

    bitcoin_data = get_bitcoin_data(ticker, start_date, end_date)
    sma = calculate_sma(bitcoin_data, window_size)
    ema = calculate_ema(bitcoin_data, alpha)

    plot_data(bitcoin_data, sma, ema)
