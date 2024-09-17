import numpy
import matplotlib.pyplot as plt
import imageio as iio
import node
import tree
from matplotlib import collections
from matplotlib import patches
from matplotlib import lines
import random
import math

#Set Desired Parameters:
D = 2               #Search Dimensions
delta = 1           #Branch Length
# qparams = [50, 50]  #Starting Node Coords
xlim = 100          #Axis Limits
ylim = 100          #Axis Limits
K = 1000             #Iterations
numCircles = 100     #Number of Circles
circleSizes = 5    #Max Circle Radius, must be >2

xs = []
ys = []

path = []
pathxs = []
pathys = []

#Create Circle Obstacles
circles = []
for i in range(numCircles):
    circles.append(patches.Circle((random.randrange(xlim),random.randrange(ylim)), random.randrange(2,circleSizes)))

#Create Valid Start Params
startParams = []
startParams = [random.randrange(xlim), random.randrange(ylim)]
for i in range(numCircles):
    distance = math.sqrt((startParams[0] - circles[i].center[0])**2 + (startParams[1] - circles[i].center[1])**2)
    if distance <= (circles[i].radius):
        i = 0
        startParams = [random.randrange(xlim), random.randrange(ylim)]
            
#Create Valid Goal Params
goalParams = []
goalParams = [random.randrange(xlim), random.randrange(ylim)]
for i in range(numCircles):
    distance = math.sqrt((goalParams[0] - circles[i].center[0])**2 + (goalParams[1] - circles[i].center[1])**2)
    if distance <= (circles[i].radius):
        i = 0
        goalParams = [random.randrange(xlim), random.randrange(ylim)]

#Create Goal Node for Checking
goalNode = node.Node(D)
goalNode.initWithParams(goalParams,0)

def rrt(qparams, K, delta, D):
    G = init(qparams)
    iter = 0
    while True:
    # for i in range(K):
        if checkEnd(G):
            break
        qrand = Random_Config(D)
        qnear = Nearest_Node(qrand, G)
        qnew = New_Config(qnear, qrand, delta, G, D)
        if checkCollision(qnew,qnear,circles) == True:
            continue
        G.addNode(qnew)
        G.addEdge(qnear, qnew)
        if iter == K:
            break
        iter += 1
    return G

def checkEnd(G):
    curEnd = G.nodes[-1]
    if checkCollision(curEnd,goalNode,circles) == False:
        goalNode.initWithParams(goalParams, curEnd)
        G.addNode(goalNode)
        G.addEdge(curEnd,goalNode)
        return True
    return False

def checkCollision(qnew, qnear, circles):
    ############# BEGIN_CITATION [3] #################
    #For reference to source, treating qnear=P1, qnew=P2, circleCenter=P3
    magDist = (qnew.coords[0] - qnear.coords[0])**2 + (qnew.coords[1] - qnear.coords[1])**2
    for i in range(len(circles)):
        circleCenter = circles[i].center
        u = (((circleCenter[0] - qnear.coords[0]) * (qnew.coords[0] - qnear.coords[0])) + ((circleCenter[1] - qnear.coords[1]) * (qnew.coords[1] - qnear.coords[1]))) / magDist
        ############# END_CITATION [3] #################
        ############# BEGIN_CITATION [1] ###############
        u = min(1,max(0,u)) ######Credit Joseph Blom
        ############# END_CITATION [1] #################
        if u >= 0 or u <= 1:
            ux = qnear.coords[0] + u * (qnew.coords[0] - qnear.coords[0])
            uy = qnear.coords[1] + u * (qnew.coords[1] - qnear.coords[1])
            distSquare = (ux - circleCenter[0])**2 + (uy - circleCenter[1])**2
            if distSquare < (circles[i].radius)**2:
                return True
    return False

def init(qparams):
    qinit = node.Node(D)
    qinit.initWithParams(qparams,0)
    return tree.Tree(qinit)

def Random_Config(D):
    return node.Node(D)

def Nearest_Node(qrand, G):
    return G.Nearest_Node(qrand)

def New_Config(qnear, qrand, delta, G, D):
    return G.New_Config(qnear, qrand, delta, D)

def visualize(xlim, ylim, G):
    for i in range(1, len(G.nodes) - 1):
        xs.append(G.nodes[i].coords[0])
        ys.append(G.nodes[i].coords[1])
    for i in range(len(path)):
        pathxs.append(path[i].coords[0])
        pathys.append(path[i].coords[1])   
    
def findPath(G):
    path.append(G.nodes[-1])
    for i in range(len(G.nodes)):
        if path[-1].parent != 0:
            path.append(path[-1].parent)
        else:
            break

G = rrt(startParams, K, delta, D)
findPath(G)
visualize(xlim, ylim, G)
fig, ax = plt.subplots()
ax.set_xlim(0,xlim)
ax.set_ylim(0,ylim)
linCol = collections.LineCollection(G.edges)
ax.add_collection(linCol)
circCol = collections.PatchCollection(circles,color='black')
ax.add_collection(circCol)
plt.scatter(xs,ys,marker='.')
plt.scatter(pathxs,pathys,c='Red',marker='.')
plt.scatter(startParams[0],startParams[1],c="Green",marker='o')
plt.scatter(goalParams[0],goalParams[1],c='Red',marker='x')
pathLine = lines.Line2D(pathxs,pathys,color='red')
ax.add_line(pathLine)
figManager = plt.get_current_fig_manager()
figManager.resize(1000,1000)
plt.show()