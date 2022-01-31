"""
In this assignment you should interpolate the given function.
"""

import numpy as np
import time
import random

def func1():  # -inf<x<inf
    return  lambda x: x*0+5
def func2():
   return lambda x: x ** 2 - 3 * x + 5
def func3(): # -inf<x<inf
    return lambda x: np.sin(x ** 2)
def func4():
    return lambda x:  np.exp(-2 * x ** 2)
def func5():   # -inf<x<inf
    return lambda x:np.arctan(x)
def func6():# x!=0
    def func(x):
        if(np.isscalar(x)):
            if(x==0):
                f=0.0
            else:
                f = np.sin(x) / x
        else:
            xx=x[x!=0]
            f= np.sin(xx) / xx
        return f
    return func
def func7(): # x>0 & X!=1
    def func(x):
        if (np.isscalar(x)):
            if (x>0 and x!=1):
               f = 1. / np.log(x)
        else:
            xx=x[(x!=1 and x>0)]
            f =1. / np.log(xx)
        return f
    return func
def func8():
    return lambda x: np.exp(np.exp(x))
def func9(): # x>=1
    return lambda x: np.log(np.log(x))
def func10(): # x>0
    return lambda x:  np.sin(np.log(x))
def func11(): # x!=0
    return lambda x: 2 ** (1 / x ** 2) * np.sin(1 / x)

class Assignment1:
    def __init__(self):
        """
        Here goes any one time calculation that need to be made before 
        starting to interpolate arbitrary functions.
        """

        pass

    def interpolate(self, f: callable, a: float, b: float, n: int) -> callable:
        """
        Interpolate the function f in the closed range [a,b] using at most n 
        points. Your main objective is minimizing the interpolation error.
        Your secondary objective is minimizing the running time. 
        The assignment will be tested on variety of different functions with 
        large n values. 
        
        Interpolation error will be measured as the average absolute error at 
        2*n random points between a and b. See test_with_poly() below. 

        Note: It is forbidden to call f more than n times. 

        Note: This assignment can be solved trivially with running time O(n^2)
        or it can be solved with running time of O(n) with some preprocessing.
        **Accurate O(n) solutions will receive higher grades.** 
        
        Note: sometimes you can get very accurate solutions with only few points, 
        significantly less than n. 
        
        Parameters
        ----------
        f : callable. it is the given function
        a : float
            beginning of the interpolation range.
        b : float
            end of the interpolation range.
        n : int
            maximal number of points to use.

        Returns
        -------
        The interpolating function.
        """
        x = np.linspace(a,b,n)
        y = f(x)
        def find_nearest(array, value):
            idx = np.abs(array - value).argmin()
            if (array[idx] > value):
                idx = idx - 1
            return int(idx)
        def  result(xx):
            i =  find_nearest(x,xx)
            if(xx==x[i]):
                yy= y[i]
            elif(xx<x[0]):
                yy = y[0]
            elif(xx>x[-1]):
                yy =y[-1]
            else:
                yy = y[i] + (xx - x[i]) * (y[i + 1] - y[i]) / (x[i + 1]-x[i])
            return yy
        return result

##########################################################################


import unittest
from functionUtils import *
from tqdm import tqdm


class TestAssignment1(unittest.TestCase):

    def test_with_poly(self):
        T = time.time()
        ass1 = Assignment1()
        mean_err = 0
        d = 300
        for i in tqdm(range(100)):
            a = np.random.randn(d)
            f =  func7()
            ff = ass1.interpolate(f, -10, 10, 300 + 1)
            xs = np.random.random(200)
            err = 0
            for x in xs:
                yy = ff(x)
                y = f(x)
                err += abs(y - yy)
            err = err / 200
            mean_err += err
        mean_err = mean_err / 100

        T = time.time() - T
        print(T)
        print(mean_err)

    def test_with_poly_restrict(self):
        ass1 = Assignment1()
        a = np.random.randn(5)
        f = RESTRICT_INVOCATIONS(10)(np.poly1d(a))
        ff = ass1.interpolate(f, -10, 10, 10)
        xs = np.random.random(20)
        for x in xs:
            yy = ff(x)


if __name__ == "__main__":
    unittest.main()
