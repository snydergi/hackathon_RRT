#Serves as the overall structure containing all nodes and edges

class Tree():

    nodes = []
    edges = []

    def __init__(self, qinit):
        self.nodes.append(qinit)

    def Nearest_Node(self,q):
        curClosest = self.nodes[0]
        for i in range(len(self.nodes)):
            if self.distance(q,curClosest) > self.distance(q,self.nodes[i]):
                curClosest = self.nodes[i]
        return curClosest
    
    def distance(q1, q2):
        dist = 0
        for i in range(len(q1.coords)):
            dist += (q1.coords[i]-q2.coords[i])^2
        return dist

