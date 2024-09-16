import numpy
import matplotlib as mpl
import imageio as iio

G = 0

def rrt(qinit, K, delta, D):
    G = init(qinit)
    for i in range(K):
        qrand = Random_Config(D)
        qnear = Nearest_Node(qrand, G)
        qnew = New_Config(qnear, qrand, delta)
        addNode(qnew, G)
        addEdge(qnear, qnew, G)
    return G

def init(qinit):
    pass

def Random_Config(D):
    pass

def Nearest_Node(qrand, G):
    pass

def New_Config(qnear, qrand, delta):
    pass

def addNode(qnew, G):
    pass

def addEdge(qnear, qnew, G):
    pass