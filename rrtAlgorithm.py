import numpy
import matplotlib.pyplot as plt
import imageio as iio
import node
import tree
from matplotlib import collections
from matplotlib import patches
import random
import math

#Set Desired Parameters:
D = 2               #Search Dimensions
delta = 1           #Branch Length
# qparams = [50, 50]  #Starting Node Coords
xlim = 100          #Axis Limits
ylim = 100          #Axis Limits
K = 1000             #Iterations
numCircles = 50     #Number of Circles
circleSizes = 5    #Max Circle Radius, must be >2

xs = []
ys = []

#Create Circle Obstacles
circles = []
for i in range(numCircles):
    circles.append(patches.Circle((random.randrange(xlim),random.randrange(ylim)), random.randrange(2,circleSizes)))

#Create Valid Start Params
startParams = []
while True:
    startParams = [random.randrange(xlim), random.randrange(ylim)]
    for i in range(numCircles):
        distance = math.sqrt((startParams[0] - circles[i].center[0])**2 + (startParams[1] - circles[i].center[1])**2)
        if distance <= (circles[i].radius):
            continue
        else:
            break
    break

#Create Valid Goal Params
goalParams = []
while True:
    goalParams = [random.randrange(xlim), random.randrange(ylim)]
    for i in range(numCircles):
        distance = math.sqrt((goalParams[0] - circles[i].center[0])**2 + (goalParams[1] - circles[i].center[1])**2)
        if distance <= (circles[i].radius):
            continue
        else:
            break
    break

def rrt(qparams, K, delta, D):
    G = init(qparams)
    for i in range(K):
        qrand = Random_Config(D)
        qnear = Nearest_Node(qrand, G)
        qnew = New_Config(qnear, qrand, delta, G, D)
        if checkCollision(qnew,qnear,circles) == False:
            continue
        G.addNode(qnew)
        G.addEdge(qnear, qnew)
    return G

def checkCollision(qnew, qnear, circles):
    #############Min Line Distance Equation from [2]#################
    #For reference to source, treating qnear=P1, qnew=P2, circleCenter=P3
    magDist = (qnew.coords[0] - qnear.coords[0])**2 + (qnew.coords[1] - qnear.coords[1])**2
    for i in range(len(circles)):
        circleCenter = circles[i].center
        u = (((circleCenter[0] - qnear.coords[0]) * (qnew.coords[0] - qnear.coords[0])) + ((circleCenter[1] - qnear.coords[1]) * (qnew.coords[1] - qnear.coords[1]))) / magDist
        if u >= 0 or u <= 1:
            ux = qnear.coords[0] + u * (qnew.coords[0] - qnear.coords[0])
            uy = qnear.coords[1] + u * (qnew.coords[1] - qnear.coords[1])
            distSquare = (ux - circleCenter[0])**2 + (uy - circleCenter[1])**2
            if distSquare < (circles[i].radius)**2:
                return False
    return True

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
    for i in range(len(G.nodes)):
        xs.append(G.nodes[i].coords[0])
        ys.append(G.nodes[i].coords[1])
    plt.show()

G = rrt(startParams, K, delta, D)
visualize(xlim, ylim, G)
fig, ax = plt.subplots()
ax.set_xlim(0,xlim)
ax.set_ylim(0,ylim)
linCol = collections.LineCollection(G.edges)
ax.add_collection(linCol)
circCol = collections.PatchCollection(circles)
ax.add_collection(circCol)
plt.scatter(xs,ys,marker='.')
plt.show()