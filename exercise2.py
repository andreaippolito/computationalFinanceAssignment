import numpy as np
def riemann_sum_brownian_motion(inferior, superior, brownian_motion_paths):
    """It calculates the Riemann Sum of Brownion Motion using pseudo-randomly generated Brownian Paths.
    inferior -- should be a real number representing the left boundary point of the integral.
    superior -- real number representing the right boundary point of the integral.
    brownian_motion_paths -- vectors of floats containing the points of pseudo Brownian Motion.
    """
    [number_of_paths, number_of_steps]=np.matrix.size(brownian_motion_paths)
    dt=superior-inferior/float(number_of_steps)
    riemann_sum=0
    number_of_paths=int(np.size(brownian_motion_paths))
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
 def GeneratePathsBM(NoOfPaths,NoOfSteps,T):
    """
    Method used to create paths of Brownian Motion until a given time.
    T -- time at which the generation is stopped
    NoOfPaths -- integer indicating the number of paths to generate
    NoOfSteps -- integer indicating the number of intervals to consider between 0 and T 
    """
    # Fixing random seed
    np.random.seed(1)
    Z = np.random.normal(0.0,1.0,[NoOfPaths,NoOfSteps])
    X = np.zeros([NoOfPaths, NoOfSteps+1])
    time = np.zeros([NoOfSteps+1])
    dt=T/float(NoOfSteps)
    for i in range(0,NoOfSteps):
        X[:,i+1] = X[:,i] +  np.power(dt, 0.5)*Z[:,i]
        time[i+1] = time[i] +dt
    return X

if __name__ == '__main__':
    main()
    for i in range(4,12):
        brownian_motion_paths=GeneratePathsBM(2^i,2^i, 5)