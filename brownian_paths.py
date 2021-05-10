"""
Module containing the class Brownian Paths, that is different realization of Brownian Motions between 0 and
an ending time
"""
import numpy as np


class BrownianPaths(object):
    def __init__(self, no_of_paths, no_of_steps, starting_point, ending_point):
        self.no_of_paths = no_of_paths
        self.no_of_steps = no_of_steps
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.paths = self.generate_paths_bm()
    
    def generate_paths_bm(self):
        # generate
        dt = self.ending_point/float(self.no_of_steps+1)
        normal_values = np.random.normal(0.0, 1.0, (self.no_of_paths, self.no_of_steps+1))
        for i in range(0, self.no_of_steps+1):
            mean = sum(normal_values[:, i])/self.no_of_paths
            standard_deviation = np.sqrt(((mean-normal_values[i])**2)/self.no_of_paths)
            normal_values[:, i] = (normal_values[:, i]-mean)/standard_deviation
        brownian_paths = np.zeros((self.no_of_paths, self.no_of_steps+1), float)
        for i in range(0, self.no_of_steps+1):
            brownian_paths[:, i+1] = brownian_paths[:, i] + pow(dt, 0.5)*normal_values[:, i]
        return brownian_paths
