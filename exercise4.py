import numpy as np
import brownian_paths as bp


def main_calculation():
    T = 10
    brownian_paths = bp.BrownianPaths(2**14, 2**14, 0, T)
    dt=brownian_paths.ending_point/float(brownian_paths.no_of_steps)
    var_X = np.ones(brownian_paths.no_of_steps)
    exact_solution=np.ones(brownian_paths.no_of_steps)
    for i in range(0, brownian_paths.no_of_steps+1):
        mean_t = np.sum(brownian_paths.paths[:, i])/brownian_paths.no_of_paths
        standard_deviation_t = np.sqrt(sum(mean_t - brownian_paths.paths[:, i])/(brownian_paths.no_of_steps+1))
        mean_T = np.sum(brownian_paths.paths[:, brownian_paths.no_of_steps-i])/brownian_paths.no_of_paths
        standard_deviation_T = np.sqrt(sum(mean_T - brownian_paths.paths[:, brownian_paths.no_of_steps-i])/(brownian_paths.no_of_steps+1))
        var_X[i] = standard_deviation_t - dt*i / T *standard_deviation_T
        exact_solution [i] = dt*i+dt*i/T*(T-dt*i)-+2*dt*i/T*np.min(dt*i, T-dt*i)
    error = exact_solution-var_X