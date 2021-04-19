import numpy as np
import pathgenerator as pathgen

def riemann_sum_brownian_motion(inferior, superior, brownian_motion_paths):
    """This funcion calculates the Riemann Sum of Brownion Motion using pseudo-randomly generated Brownian Paths.
    inferior -- should be a real number representing the left boundary point of the integral.
    superior -- real number representing the right boundary poin of the integral.
    brownian_motion_paths -- vectors of floats containing the points of pseudo Brownian Motion.
    """
    [number_of_paths, number_of_steps]=np.matrix.size(brownian_motion_paths)
    dt=superior-inferior/float(number_of_steps)
    riemann_sum=0
    number_of_paths=np.size(brownian_motion_paths)
    for i in range (0 , number_of_paths):
        current_path=brownian_motion_paths[i, :]
        riemann_sum= np.inner(current_path, dt*np.ones(number_of_steps))+riemann_sum
    print(riemann_sum)
    return riemann_sum
def ito_integral_calculator( function_left_point, stochastic_paths):
    [number_of_paths, number_of_steps]=np.matrix.size(stochastic_paths)
    brownian_motion_increments=np.zeros(number_of_paths, number_of_steps)
    for i in range( 0 , number_of_steps-1):
        brownian_motion_increments[:,i]=stochastic_paths[:, i+1]-stochastic_paths[:,i]
    ito_sum=0
    for i in range (0, number_of_paths):
        ito_sum=np.inner(function_left_point, brownian_motion_increments[i, :])+ito_sum    
    return ito_sum


def main_calculation():
    #[times, stochastic_paths]=pathgen.GeneratePathsBM(10^6, 10^6, 5)
    try_out=pathgen.GeneratePathsBM(10^6, 10^6, 5)
    return try_out

  # riemann_integral=riemann_sum_brownian_motion(0,5, stochastic_paths)
  #  ito_integral = ito_integral_calculator(np.ones((times.size,1,1))*5-times, stochastic_paths )
   # print( ito_integral)
main_calculation()
    