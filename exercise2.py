"""
@author Andrea Ippolito

"""
import numpy as np
import brownian_paths as bp
import xlsxwriter





def riemann_sum_brownian_motion(brownian_motion_paths):
    """It calculates the Riemann Sum of Brownian Motion using pseudo-randomly generated Brownian
    Paths.
    inferior -- should be a real number representing the left boundary point of the integral.
    superior -- real number representing the right boundary point of the integral.
    brownian_motion_paths -- vectors of floats containing the points of pseudo Brownian Motion.
    """
    time_interval = brownian_motion_paths.time_step
    riemann_sum = np.zeros(brownian_motion_paths.no_of_paths)
    for i in range(0, brownian_motion_paths.no_of_paths):
        current_path = brownian_motion_paths.paths[i, :]
        riemann_sum[i] = np.inner(current_path, time_interval * np.ones(brownian_motion_paths.no_of_steps+1))
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
    ito_integral = np.zeros(brownian_motion_paths.no_of_paths)
    for i in range(0, brownian_motion_paths.no_of_paths):
        ito_integral[i] = np.inner(function_left_values, brownian_motion_increments[i, :])
    return ito_integral


def main():
    a = 1
    b = 12
    results = np.zeros((b-a, 2))
    brownian_motion_paths = bp.BrownianPaths(10, 5000, 0, 5)
    riemann_sum = riemann_sum_brownian_motion(brownian_motion_paths)
    ito_integral = ito_integral_calculator(brownian_motion_paths)
    print(riemann_sum, ito_integral)
    workbook = xlsxwriter.Workbook('numerical_integration.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write_column(0, 0, riemann_sum)
    worksheet.write_column(0, 1, ito_integral)
    workbook.close()
if __name__ == '__main__':
    main()
