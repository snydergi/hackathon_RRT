import numpy
import matplotlib.pyplot as plt
import imageio as iio
import node
import tree

#Set Desired Parameters:
D = 2               #Search Dimensions
delta = 1           #Branch Length
qparams = [50, 50]  #Starting Node Coords
xlim = 100          #Axis Limits
ylim = 100          #Axis Limits
K = 500             #Iterations

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
    qinit = node.Node(D)
    qinit.initWithParams(qparams)
    return tree.Tree(qinit)

def Random_Config(D):
    return node.Node(D)

def Nearest_Node(qrand, G):
    return G.Nearest_Node(qrand)

def New_Config(qnear, qrand, delta, G, D):
    return G.New_Config(qnear, qrand, delta, D)

def visualize(xlim, ylim, G):
    xs = []
    ys = []
    for i in range(len(G.nodes)):
        xs.append(G.nodes[i].coords[0])
        ys.append(G.nodes[i].coords[1])
    plt.scatter(xs,ys)
    plt.show()

G = rrt(qparams, K, delta, D)
visualize(xlim, ylim, G)