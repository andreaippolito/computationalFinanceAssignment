import numpy as np
import brownian_paths as bp
import matplotlib.pyplot as plt
import pandas as pd


def running_sum(stock_paths):
    (number_of_processes, number_of_points) = stock_paths.shape
    square_increments = np.zeros((number_of_processes, number_of_points-1))

    for i in range(0, number_of_points-1):
        square_increments_sum= np.zeros(number_of_processes)
        for j in range(0, i):
            square_increments_sum[:] = square_increments_sum[:]+(stock_paths[:, j+1]-stock_paths[:, j])**2
        square_increments[:, i]=square_increments_sum[:]
    return square_increments


def extract_data(path):
    df = pd.read_csv(path, usecols=[0, 4], parse_dates=[0])
    df['Date'] = pd.to_datetime(df['Date'])
    stock_values = df.Close.values
    stock_values = stock_values.astype(np.float)
    return stock_values


if __name__ == '__main__':
    mu = 0.05
    sigma = 0.4
    T = 3
    starting_value = 0.7
    time_step = 10**-2
    number_of_step = int(3/time_step)
    file_paths=['NFLX.csv', 'VOW3.DE.csv', 'AMD.csv', 'NVDA.csv']
    brownian_paths = bp.BrownianPaths(10, number_of_step, 0, 3)
    geometric_brownian_motion = np.ones((brownian_paths.no_of_paths, brownian_paths.no_of_steps+1))
    geometric_brownian_motion[0, :]=starting_value
    for i in range(0, brownian_paths.no_of_steps):
        geometric_brownian_motion[:, i+1] = geometric_brownian_motion[:, i]*np.exp((mu-sigma**2/2)*time_step+sigma*(brownian_paths.paths[:,i]-brownian_paths.paths[:, i+1]))
    square_increments = running_sum(geometric_brownian_motion)
    for i in range(0, brownian_paths.no_of_paths):
        plt.plot( np.linspace(0,  3, number_of_step+1), geometric_brownian_motion[i, :])
    plt.savefig('exercise9a.png')
    plt.close()
    for i in range(0, brownian_paths.no_of_paths):

        plt.plot( np.linspace(0,  3, number_of_step), square_increments[i, :])
    plt.savefig('exercise9b.png')
    plt.close()
    for path in file_paths:
        stock_values = extract_data(path)
        number_of_days = stock_values.size
        square_increments= np.zeros(number_of_days)
        for i in range(1, number_of_days):
            square_increments_sum = 0
            for j in range(0, i):
                square_increments_sum = square_increments_sum + (stock_values[j + 1] - stock_values[ j]) ** 2
            square_increments[i] = square_increments_sum
        df = pd.read_csv(path, usecols=[0, 4], parse_dates=[0])
        df['Date'] = pd.to_datetime(df['Date'])
        plt.plot(df['Date'], stock_values, label='Market value of '+path[:-4])
        plt.plot(df['Date'], square_increments, label='Running Sum of square increments')
        plt.legend()
        plt.savefig(path[:-4]+'.png')
        plt.close()
