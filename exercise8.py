import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def daily_returns(starting_date, ending_date, path):
    df = pd.read_csv(path, usecols=[0, 4], parse_dates = [0])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.loc[(df['Date'] >= starting_date) & (df['Date'] <= ending_date)]
    stock_values = df.Close.values
    stock_values = stock_values.astype(np.float)
    daily_return = np.zeros(np.size(stock_values))
    for i in range(1, np.size(stock_values)):
        daily_return[i] = (stock_values[i] - stock_values[i - 1]) / stock_values[i - 1]
    df.insert(1, "Daily_Returns", daily_return)
    return df



if __name__ == '__main__':
    independent_stock_values = ['NFLX.csv', 'VOW3.DE.csv']
    dependent_stock_values = ['AMD.csv', 'NVDA.csv']

    for stock_to_retrieve in independent_stock_values:
        data_frame = daily_returns('01-01-2021', '10-05-2021', stock_to_retrieve)
        plt.plot(data_frame['Date'], data_frame['Daily_Returns'], label=stock_to_retrieve[:-4],linewidth=0, marker='.', markersize=10)
        plt.xticks(rotation='vertical')
        plt.rcParams["figure.figsize"] = (25, 3)
        plt.legend()
        plt.grid()
        plt.savefig('independent_stock_values.png')
    plt.close()
    for stock_to_retrieve in dependent_stock_values:
        data_frame = daily_returns('01-01-2021', '10-05-2021', stock_to_retrieve)
        plt.plot(data_frame['Date'], data_frame['Daily_Returns'], label=stock_to_retrieve[:-4],linewidth=0, marker='.', markersize=10)
        plt.xticks(rotation='vertical')
        plt.rcParams["figure.figsize"] = (25, 3)
        plt.legend()
        plt.grid()
        plt.savefig('dependent_stock_values.png')
    plt.close()

