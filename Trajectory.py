import matplotlib.pyplot as plt
import numpy as np
def Trajectory(up=1,right=1,g=0.05,frames=1000,sub=0.005,x=0,y=0,endAt0=True,places=6,color='black',marker=None,linestyle='solid',linewidth=1,markersize=1,):
    data=[]
    data_x = []
    data_y = []
    for i in range(0,frames):
        data.append((round(x,places),round(y,places)))
        data_x.append(x)
        data_y.append(y)
        x+=up
        y+=right
        x-=g
        up-=sub
        if x<0 and i !=0 and endAt0==True:
            data.append((round(x,places),round(y,places)))
            break
    xpoints = np.array(data_y)
    ypoints = np.array(data_x)
    plt.plot(xpoints, ypoints, color=color, marker=marker, linestyle=linestyle, linewidth=linewidth, markersize=markersize)
    plt.show()
    return data
