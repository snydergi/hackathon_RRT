#Serve as points within the RRT structure
import random

class Node():
    
    def __init__(self,D):
        self.coords = []
        for i in range(D):
            self.coords.append(random.random()*100)

    def initWithParams(self, qparams):
        self.coords = []
        for i in range(len(qparams)):
            self.coords.append(qparams[i])