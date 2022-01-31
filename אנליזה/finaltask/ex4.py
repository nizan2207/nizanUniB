import numpy as np
import matplotlib.pyplot as plt
import math

from scipy.interpolate import CubicSpline

def createShape(n):

    q = np.linspace(0,180,n)
    r = 20
    noisex = np.random.normal(0,1,n)/2
    noisey = np.random.normal(0,1,n)/2
    x= r*np.cos(np.deg2rad(q))
    y= r*np.sin(np.deg2rad(q))
    plt.plot(x,y)
    xn=x+noisex
    yn=y+noisey
    plt.plot(x,yn)
    return x,yn

def batchFilter(x,y,order=2,windows_size=20):
    # This function fits a second ordered polynomial to a set of measurements
    # The fitting method is based on least squares method

    xfitted = []
    yfitted = []

    ipos=0

    for ipos in range(len(x)-(windows_size-1)):
        index = int(ipos + windows_size / 2)
        coefficientsx = np.polyfit(x[ipos:(ipos+windows_size)], y[ipos:ipos+windows_size], 2)

        yfit = coefficientsx[0] * (x[index] ** 2) + coefficientsx[1] * x[index] + \
                   coefficientsx[2]
        xfit=x[index]
        xfitted.append(xfit)
        yfitted.append(yfit)

    return (xfitted,yfitted)

if __name__=='__main__':
    n = 18001
    windows_size = 50

    (x,y)=createShape(n)
    index = sorted(range(len(x)),key=lambda k:x[k])
    xx = x[index]
    yy = y[index]
    cs = CubicSpline(xx,yy)
    x_new=np.linspace(-20,20,10)
    plt.plot(x_new, cs(x_new), 'ok')

    # (xfitted, yfitted) = batchFilter(x, y, order=2, windows_size=windows_size)
    # plt.plot(xfitted, yfitted,'ok')

    plt.show()