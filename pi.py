import random
import matplotlib.pyplot as plt
import numpy as np
import math
def points(numpoints,skip=1):
    #This function creates a list of points between the cordinates 0,0 0,1 1,0 and 1,1
    pointslist=[]
    for i in range(0,numpoints):
        pointslist.append([random.random(),random.random()])
        if i%skip==0:
            print(i)
    return pointslist
def incircle(pointx,pointy):
    #this function checks wether a point is inside of a quarter circle with focus being 0,0
    if ((pointx**2)+(pointy**2))<=1:
        incirc=True
    else:
        incirc=False
    return incirc
def circlepoints(numpoints,skip=1,plot=True):
    #this function calculates pi
    shade=0
    total=0
    n=0
    data_x=[]
    data_y=[]
    for i in points(numpoints,skip):
        n+=1
        total+=1
        if incircle(i[0],i[1]):
            shade+=1
        pi=(shade/total)*4
        data_x.append(pi)
        data_y.append(n)
        if n % skip == 0:
            print(pi, abs(pi-math.pi), n, ('('+str(shade)+'/'+str(total)+')'+'*4'))
    if plot:
        xpoints = np.array(data_y)
        ypoints = np.array(data_x)
        plt.plot(xpoints, ypoints,color='black',linestyle='solid',linewidth=1,markersize=1)
        plt.show()
    return pi, abs(pi-math.pi), n, ('('+str(shade)+'/'+str(total)+')'+'*4')