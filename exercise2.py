"""
@author Andrea Ippolito
Module in which the exercise 2 of the take home exam for the Computational Finance Course is solved. 
It is meant to be a self contained solution and therefore not relying on other code written by me.
"""
import numpy as np
import brownian_paths as bp


def riemann_sum_brownian_motion(brownian_motion_paths):
    """It calculates the Riemann Sum of Brownian Motion using pseudo-randomly generated Brownian
    Paths.
    inferior -- should be a real number representing the left boundary point of the integral.
    superior -- real number representing the right boundary point of the integral.
    brownian_motion_paths -- vectors of floats containing the points of pseudo Brownian Motion.
    """

    time_interval = (brownian_motion_paths.ending_point-brownian_motion_paths.starting_point) / \
        brownian_motion_paths.no_of_steps
    riemann_sum = 0
    for i in range(0, brownian_motion_paths.no_of_paths):
        current_path = brownian_motion_paths.paths[i, :]
        riemann_sum = np.inner(current_path, time_interval * np.ones(brownian_motion_paths.no_of_steps+1)) + riemann_sum
    return riemann_sum


def ito_integral_calculator(brownian_motion_paths):
    """
    It returns the approximation of the Ito integral given the values of the integrated function evaluated
    in the left point of each interval
    """
    brownian_motion_increments = np.zeros((brownian_motion_paths.no_of_paths, brownian_motion_paths.no_of_steps))
    for i in range(0, brownian_motion_paths.no_of_steps):
        brownian_motion_increments[:, i] = brownian_motion_paths.paths[:, i+1] - brownian_motion_paths.paths[:, i]

    function_left_values = 5 - np.linspace(0, 5, brownian_motion_paths.no_of_steps, False)
    ito_integral = 0
    for i in range(0, brownian_motion_paths.no_of_paths):
        current_path = brownian_motion_increments[i, :]
        ito_integral = np.inner(function_left_values, current_path) + ito_integral
    return ito_integral


def main():
    a = 1
    b = 12
    results = np.zeros((b-a, 2))
    for i in range(a, b):
        brownian_motion_paths = bp.BrownianPaths(pow(2, i), pow(2, i)-1, 0, 5)
        riemann_sum = riemann_sum_brownian_motion(brownian_motion_paths)
        results[i-a, 0] = riemann_sum
        results[i-a, 1] = ito_integral_calculator(brownian_motion_paths)
    print(results)


if __name__ == '__main__':
    main()
