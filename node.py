#Serve as points within the RRT structure
import random

class Node():
    
    coords = []

    def __init__(self,D):
        for i in range(D):
            self.coords[i] = random.random()

    def initWithParams(self, qparams):
        self.coords = []
        for i in range(len(qparams)):
            self.coords[i] = qparams[i]