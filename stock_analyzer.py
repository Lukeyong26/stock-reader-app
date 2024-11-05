import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Pull historical stock data
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Simple moving average (SMA) crossover strategy
def sma_crossover_strategy(stock_data, short_window=50, long_window=200):
    # Calculate short and long SMAs
    stock_data['SMA_short'] = stock_data['Close'].rolling(window=short_window, min_periods=1).mean()
    stock_data['SMA_long'] = stock_data['Close'].rolling(window=long_window, min_periods=1).mean()
    
    # Generate signals
    stock_data['Signal'] = 0
    stock_data['Signal'] = (
        stock_data['SMA_short'][short_window:] > stock_data['SMA_long'][short_window:]
    ).astype(int)
    stock_data['Position'] = stock_data['Signal'].diff()
    
    return stock_data

# Plot stock data with SMA and signals
def plot_stock_data(stock_data, symbol):
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Close'], label='Close Price', color='blue', alpha=0.5)
    plt.plot(stock_data['SMA_short'], label='50-day SMA', color='orange', linestyle='--')
    plt.plot(stock_data['SMA_long'], label='200-day SMA', color='purple', linestyle='--')
    
    # Plot buy signals
    plt.plot(stock_data[stock_data['Position'] == 1].index,
             stock_data['SMA_short'][stock_data['Position'] == 1],
             '^', markersize=10, color='green', lw=0, label='Buy Signal')
    
    # Plot sell signals
    plt.plot(stock_data[stock_data['Position'] == -1].index,
             stock_data['SMA_short'][stock_data['Position'] == -1],
             'v', markersize=10, color='red', lw=0, label='Sell Signal')
    
    plt.title(f'{symbol} Stock Price and SMA Crossover Signals')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend(loc='best')
    plt.show()

# Main function to run the analysis
def main():
    # Define stock symbol, date range, and moving average windows
    symbol = 'PLTR'
    start_date = '2022-01-01'
    end_date = '2024-11-02'
    
    # Get stock data
    stock_data = get_stock_data(symbol, start_date, end_date)
    
    # Apply SMA crossover strategy
    stock_data = sma_crossover_strategy(stock_data, short_window=50, long_window=200)

    # print(stock_data)
    
    # Plot the data and signals
    plot_stock_data(stock_data, symbol)

# Run the main function
if __name__ == "__main__":
    main()