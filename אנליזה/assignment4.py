"""
In this assignment you should fit a model function of your choice to data 
that you sample from a contour of given shape. Then you should calculate
the area of that shape. 

The sampled data is very noisy so you should minimize the mean least squares 
between the model you fit and the data points you sample.  

During the testing of this assignment running time will be constrained. You
receive the maximal running time as an argument for the fitting method. You 
must make sure that the fitting function returns at most 5 seconds after the 
allowed running time elapses. If you know that your iterations may take more 
than 1-2 seconds break out of any optimization loops you have ahead of time.

Note: You are allowed to use any numeric optimization libraries and tools you want
for solving this assignment. 
Note: !!!Despite previous note, using reflection to check for the parameters 
of the sampled function is considered cheating!!! You are only allowed to 
get (x,y) points from the given shape by calling sample(). 
"""
import matplotlib.pyplot as plt
import numpy as np
import time
import random
from functionUtils import AbstractShape
from shapely.geometry import Polygon



def batchFilter(x, y, windows_size=120):
    # This function fits a second ordered polynomial to a set of measurements
    # The fitting method is based on least squares method

    xfitted = []
    yfitted = []

    ipos = 0

    for ipos in range(len(x) - (windows_size - 1)):
        index = int(ipos + windows_size / 2)
        coefficientsx = np.polyfit(x[ipos:(ipos + windows_size)], y[ipos:ipos + windows_size], 2)

        yfit = coefficientsx[0] * (x[index] ** 2) + coefficientsx[1] * x[index] + \
               coefficientsx[2]
        xfit = x[index]
        xfitted.append(xfit)
        yfitted.append(yfit)

    return (xfitted, yfitted)


class MyShape(AbstractShape):
    # change this class with anything you need to implement the shape
    def __init__(self, x, y):
        plt.plot(x, y, '.r')
        x_mean = np.mean(x,axis=0)
        y_mean = np.mean(y,axis=0)

        r = np.sqrt((x-x_mean)**2+(y-y_mean)**2)
        theta= np.arctan2((y-y_mean),(x-x_mean))

        index = np.argsort(theta)
        theta= theta[index]
        r = r[index]
        theta1,r1 = self.calcShape1(theta,r)

        theta_new =np.linspace(theta.min(),theta.max(),100)
        r_new = np.interp(theta_new ,theta1,r1)
        xx= r_new*np.cos(theta_new)
        yy = r_new*np.sin(theta_new)
        xx=xx+x_mean
        yy= yy+y_mean
        self.x =xx
        self.y =yy
        plt.plot(xx, yy, '.k')
        plt.show()

    def calcShape1(self, x,y):
       # cs = CubicSpline(theta,r)
        xx,yy= batchFilter(x, y, windows_size=50)
        return xx,yy
    def calcShape(self, x):
        yfit = self.model.predict(x[:, np.newaxis])
        return yfit

    def area(self):
        points = np.vstack([self.x, self.y]).T
        poly = Polygon(points)
        return poly.area


class Assignment4:
    def __init__(self):
        """
        Here goes any one time calculation that need to be made before 
        solving the assignment for specific functions. 
        """

        pass

    def fit_shape(self, sample: callable, maxtime: float) -> AbstractShape:
        """
        Build a function that accurately fits the noisy data points sampled from
        some closed shape. 

        Parameters
        ----------
        sample : callable. 
            An iterable which returns a data point that is near the shape contour.
        maxtime : float
            This function returns after at most maxtime seconds. 

        Returns
        -------
        An object extending AbstractShape. 
        """

        # replace these lines with your solution
        numPoints = 1000
        x = np.zeros(numPoints)
        y = np.zeros(numPoints)
        for i in range(numPoints):
            x[i], y[i] = sample()
        result = MyShape(x, y)

        return result


##########################################################################


import unittest
from sampleFunctions import *
from tqdm import tqdm


class TestAssignment4(unittest.TestCase):
    def test_return(self):
        circ = noisy_circle(cx=1, cy=1, radius=1, noise=0.1)
        ass4 = Assignment4()
        T = time.time()
        shape = ass4.fit_shape(sample=circ, maxtime=5)
        T = time.time() - T
        self.assertTrue(isinstance(shape, AbstractShape))
        self.assertLessEqual(T, 5)

    def test_delay(self):
        circ = noisy_circle(cx=1, cy=1, radius=1, noise=0.1)

        def sample():
            time.sleep(7)
            return circ()

        ass4 = Assignment4()
        T = time.time()
        shape = ass4.fit_shape(sample=sample, maxtime=5)
        T = time.time() - T
        self.assertTrue(isinstance(shape, AbstractShape))
        self.assertGreaterEqual(T, 5)

    def test_circle_area(self):
        circ = noisy_circle(cx=1, cy=1, radius=1, noise=0.1)
        ass4 = Assignment4()
        T = time.time()
        shape = ass4.fit_shape(sample=circ, maxtime=30)
        T = time.time() - T
        a = shape.area()
        print(f'abs(a - np.pi)={abs(a - np.pi)}')
        self.assertLess(abs(a - np.pi), 0.01)
        self.assertLessEqual(T, 32)

    def test_bezier_fit(self):
        circ = noisy_circle(cx=1, cy=1, radius=1, noise=0.1)
        ass4 = Assignment4()
        T = time.time()
        shape = ass4.fit_shape(sample=circ, maxtime=30)
        T = time.time() - T
        a = shape.area()
        self.assertLess(abs(a - np.pi), 0.01)
        self.assertLessEqual(T, 32)


if __name__ == "__main__":
    unittest.main()
