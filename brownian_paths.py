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
        self.time_step = (self.ending_point-self.starting_point)/float(self.no_of_steps)
        self.paths = self.generate_paths_bm()
    
    def generate_paths_bm(self):
        normal_values = np.random.normal(0.0, 1.0, (self.no_of_paths, self.no_of_steps+1))
        for i in range(0, self.no_of_steps+1):
            normal_values[:, i] = (normal_values[:, i]-np.mean(normal_values[:, i]))/np.std(normal_values[:, i])
        brownian_paths = np.zeros((self.no_of_paths, self.no_of_steps+1), float)
        for i in range(0, self.no_of_steps):
            brownian_paths[:, i+1] = brownian_paths[:, i] + pow(self.time_step, 0.5)*normal_values[:, i]
        return brownian_paths

    def change_of_measure(self, drift_term, interest_rate, volatility):
        new_brownian_path = BrownianPaths(self.no_of_paths, self.no_of_steps, self.starting_point, self.ending_point)
        time_step = (self.ending_point - self.starting_point) / self.no_of_steps
        for i in range(0, self.no_of_steps+1):
            new_brownian_path.paths[:, i] = self.paths[:, i] + (drift_term-interest_rate) * time_step*i/ volatility
        return new_brownian_path
