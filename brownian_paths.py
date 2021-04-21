"""
Module containing the class Brownian Paths, that is different realizion of Brownian Motions between 0 and a an ending poin
"""
import numpy as np
class BrownianPaths(object):
    def __init__(self,no_of_paths, no_of_steps, starting_point, ending_point):
        self.no_of_paths=no_of_paths
        self.no_of_steps=no_of_steps
        self.starting_point=starting_point
        self.ending_point=ending_point
        self.brownian_motion_paths=self.generate_paths_BM(self)
    
    def generate_paths_BM(self):
        ###generate 
        normal_values=np.random.normal(0.0, 1.0,(self.no_of_paths,self.no_of_steps))
        return  temp
 
    
