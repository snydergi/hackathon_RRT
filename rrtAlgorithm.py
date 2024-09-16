import numpy
import matplotlib as mpl
import imageio as iio
import node
import tree

def rrt(qparams, K, delta, D):
    G = init(qparams)
    for i in range(K):
        qrand = Random_Config(D)
        qnear = Nearest_Node(qrand, G)
        qnew = New_Config(qnear, qrand, delta, G, D)
        G.addNode(qnew)
        G.addEdge(qnear, qnew)
    return G

def init(qparams):
    qinit = node.Node.initWithParams(qparams)
    return tree.Tree(qinit)

def Random_Config(D):
    return node.Node(D)

def Nearest_Node(qrand, G):
    return G.Nearest_Node(qrand)

def New_Config(qnear, qrand, delta, G, D):
    return G.New_Config(qnear, qrand, delta, D)

