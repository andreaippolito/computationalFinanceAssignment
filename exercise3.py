import brownian_paths as bp
import numpy as np
import matplotlib.pyplot as plt


def option_maturity_value(stock_price_1, stock_price_2, strike_price, discount_factor):
    euler_option_value = np.maximum(1/2 * stock_price_1 - 1/2 * stock_price_2, strike_price)*discount_factor
    number_of_processes = np.size(euler_option_value)
    present_option_value = sum(euler_option_value)/number_of_processes
    return present_option_value


def main_calculation(stock_price_1_initial_value=100, stock_price_2_initial_value=10):
    maturity = 7
    interest_rate = 0.06
    drift_term_1 = 0.04
    volatility_1 = 0.38
    drift_term_2 = 0.1
    volatility_2 = 0.15
    discount_factor = np.exp(-maturity*interest_rate)
    strike_prices = np.linspace(0, 0.1, 10)
    brownian_paths = bp.BrownianPaths(1000, 365*maturity, 0, maturity)
    stock_price_1 = stock_price_1_initial_value*np.ones(brownian_paths.no_of_paths)
    stock_price_2 = stock_price_2_initial_value*np.ones(brownian_paths.no_of_paths)
    brownian_paths_neutral_measure_1 = brownian_paths.change_of_measure(drift_term_1, interest_rate, volatility_1)
    brownian_paths_neutral_measure_2 = brownian_paths.change_of_measure(drift_term_2, interest_rate, volatility_2)

    present_option_values = np.zeros(np.size(strike_prices))
    time_step = (brownian_paths.ending_point - brownian_paths.starting_point)/brownian_paths.no_of_steps
    for i in range(0, brownian_paths.no_of_steps - 1):
        stock_price_1 = stock_price_1 * np.exp((interest_rate - 1 / 2 * volatility_1 ** 2) * time_step + \
                        volatility_1 * (
                                brownian_paths_neutral_measure_1.paths[:, i + 1] - brownian_paths_neutral_measure_1.paths[:, i]))
        stock_price_2 = stock_price_2 * np.exp((interest_rate - 1 / 2 * volatility_2 ** 2) * time_step + \
                        volatility_2 * (
                                brownian_paths_neutral_measure_2.paths[:, i + 1] - brownian_paths_neutral_measure_2.paths[:, i]))
    for i in range(0, np.size(present_option_values)):
        present_option_values[i] = option_maturity_value(stock_price_1, stock_price_2, strike_prices[i], discount_factor)
    plt.plot(strike_prices, present_option_values, linewidth=0, marker='o')
    plt.xticks(strike_prices)
    plt.yticks(present_option_values)
    plt.xlabel('Strike Values')
    plt.ylabel('V(t)')

    plt.savefig('exercise3.png', bbox_inches='tight')



if __name__ == '__main__':
    main_calculation()
