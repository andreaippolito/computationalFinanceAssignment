import numpy as np 
def GeneratePathsBM(NoOfPaths,NoOfSteps,T):    
    # Fixing random seed
    np.random.seed(1)
    Z = np.random.normal(0.0,1.0,[NoOfPaths,NoOfSteps])
    X = np.zeros([NoOfPaths, NoOfSteps+1])
    time = np.zeros([NoOfSteps+1])
    dt=T/float(NoOfSteps)
    for i in range(0,NoOfSteps):
        Z[:,i] = (Z[:,i] - np.mean(Z[:,i])) / np.std(Z[:,i]) #this makes 
        X[:,i+1] = X[:,i] +  np.power(dt, 0.5)*Z[:,i]
        time[i+1] = time[i] +dt
    paths = {"time":time,"X":X}
    return paths

