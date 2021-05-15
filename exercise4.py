import numpy as np
import brownian_paths as bp
import matplotlib.pyplot as plt


def main_calculation():
    right_end_point = 10
    brownian_paths = bp.BrownianPaths(2**10, 2**10, 0, right_end_point)
    dt = brownian_paths.time_step
    variance = np.ones(brownian_paths.no_of_steps+1)
    exact_solution=np.ones(brownian_paths.no_of_steps+1)
    for i in range(0, brownian_paths.no_of_steps+1):
        variance[i] = np.std(brownian_paths.paths[:, i]-dt*i / right_end_point*brownian_paths.paths[:, brownian_paths.no_of_steps-i])**2
        exact_solution[i] = dt*i+(dt*i/right_end_point)**2*(right_end_point-dt*i)-2*dt*i/right_end_point*np.minimum(dt*i, right_end_point-dt*i)
    error = np.abs(exact_solution-variance)
    x_axis = np.linspace(0, right_end_point, brownian_paths.no_of_steps+1)
    plt.plot(x_axis, error)
    plt.xlabel('t')
    plt.ylabel('Error')
    plt.show()


if __name__ == '__main__':
    main_calculation()

