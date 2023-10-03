import requests
import pandas
import json
import numpy
import matplotlib.pyplot as plt


def fetch_data(ticker: str) -> json:
    querystring = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "outputsize": "compact",
        "datatype": "json"
    }
    url = "https://alpha-vantage.p.rapidapi.com/query"
    headers = {
        "X-RapidAPI-Key": "71264d5294mshbb4d959995747a4p12922djsn83db35d67dea",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }
    return requests.get(url, headers=headers, params=querystring).json()


def plot_histogram(data: dict):
    daily_close_prices = data["Time Series (Daily)"]
    close_prices = [
        float(daily_data["4. close"])
        for daily_data in daily_close_prices.values()
    ]

    # Create a histogram with 20 bins (adjust as needed)
    plt.hist(close_prices, bins=20, color='blue', alpha=0.7)

    plt.title("Histogram of AAPL Stock Prices")
    plt.xlabel("Closing Price")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()


def calculate_stats(data: json):
    daily_close_prices = data["Time Series (Daily)"]
    close_prices = [
        float(daily_data["4. close"])
        for daily_data in daily_close_prices.values()
    ]
    average_close_price = sum(close_prices) / len(close_prices)
    print(f"Average Close Price: {average_close_price:.2f}")


data = fetch_data("AAPL")
calculate_stats(data)
plot_histogram(data)