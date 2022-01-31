import numpy as np
import matplotlib.pyplot as plt


class myFunction():
    def __init__(self,flag_list ,minRange, maxRange, numberInRange):
        self.x = np.linspace(minRange, maxRange, numberInRange)
        self.function_list=[]
        self.deriv_list =[]
        self.flag_list  = flag_list

        for flag in flag_list:
            self.function = np.zeros(len(self.x))
            self.deriv = np.zeros(len(self.x))
            for i,x in enumerate(self.x):
                (self.function[i], self.deriv[i])= self.calcFunc(flag,x)
            self.function_list.append(self.function)
            self.deriv_list.append(self.deriv)

    def calcFunc(self,flag,x):
        if(flag==1): #-inf<x<inf
            function =  5
            deriv = 0
        elif(flag==2):#-inf<x<inf
            function = x ** 2 - 3 * x + 5
            deriv = 2*x-3
        elif (flag == 3):#-inf<x<inf
            function = np.sin(x ** 2)
            deriv = 2 * x * np.cos(x ** 2)
        elif (flag == 4):#-inf<x<inf
            function = np.exp(-2*x ** 2)
            deriv = -4 * x * np.exp(-2*x ** 2)
        elif (flag == 5): #-inf<x<inf
            function = np.arctan( x )
            deriv =1/( x ** 2+1)
        elif (flag == 6):#x!=0
            function = np.sin(x)/x
            deriv =  (np.cos(x) *x-np.sin(x))/x**2
        elif (flag == 7): #x>0 & X!=1
            function = 1./np.log(x)
            deriv = (-1/x)/(np.log(x)**2)
        elif (flag == 8):
            function = np.exp(np.exp(x))
            deriv    = np.exp(x)*function
        elif (flag == 9): #x>=1
            function = np.log(np.log(x))
            deriv = 1/np.log(x)*1/x
        elif (flag == 10):  # x>0
            function = np.sin(np.log(x))
            deriv = np.cos(np.log(x))/x
        elif (flag == 11):  # x!=0
            function = 2**(1/x**2)*np.sin(1/x)
            deriv = (-2**(1/x**2)/x**2)*(np.sin(1/x)*2/x*np.log(2)+np.cos(1/x))
        return function,deriv

    def getX(self):
        return self.x
    def getFunc(self,flag):
        index= self.flag_list.index(flag)
        return self.function_list[index]
    def Interpolate(self,fx ,x_new): #do not insert values in a out of function legal range
        def find_nearest(array,value):
            idx= np.abs(array-value).argmin()
            if(self.x[idx] > value):
                idx=idx-1
            return idx,array[idx]

        fx_new = np.zeros(len(x_new))
        for i,x in enumerate(x_new):
            index,value =find_nearest(self.x,x)
            fx_new[i] = fx[index]+(x-self.x[index])*\
                    (fx[index+1]-fx[index])/(self.x[index+1]-self.x[index])

        return fx_new
    def plotFunction(self,ax,fx,x_vec,color = 'g',marker=None,linestyle ='-'):
       ax.plot(x_vec,fx,color = color,marker=marker,linestyle =linestyle)
       ax.set_xlabel('x')
       ax.set_ylabel('f(x)')

    def intersection(self,ax,flag1,flag2,x0,eps=0.01):

        f1,d1 = self.calcFunc(flag1, x0)
        f2,d2 = self.calcFunc(flag2, x0)
        x_int =x0
        max_iter = 50
        while(abs(f2-f1)>eps and max_iter>0):
            ax.plot(x_int, f2, 'ok')
            x_int = x_int-(f2-f1)/(d2-d1)
            f1, d1 = self.calcFunc(flag1, x_int)
            f2, d2 = self.calcFunc(flag2, x_int)
            max_iter=max_iter-1
        if(max_iter<=0):
            print('max iter ')
            print(f'not found intersecrion point {x_int} diff fx {f2-f1}')
        else:
            print(f'found intersecrion point x_int={x_int} diff fx {f2-f1} f2 ={f2},f1={f1}')
        ax.plot(x_int, f2 , 'om')
        



        return x_int
    def Integrate(self,f1,x):
        integral=0
        for i,xx in enumerate(range(len(x)-1)):
            integral += (f1[i]+f1[i+1])/2*(x[i+1]-x[i])
        return integral
    def areabetween(self,f1,f2, x_vec):
        new_func=abs(f2-f1)
        integral= self.Integrate(new_func, x_vec)
        return integral



if __name__=='__main__':

    flag = 2 #choose function
    if(flag==1):
        minRange = -100
        maxRange = 100
        numberInRange = 2
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    elif (flag == 2):
        minRange = -18.5
        maxRange = 21.5
        numberInRange = 41
        numberInRange_new = 20
        x_new = np.linspace(minRange+0.25,maxRange-0.25,numberInRange_new)
    elif (flag == 3):
        minRange = -np.sqrt(np.pi)
        maxRange = np.sqrt(np.pi)
        numberInRange = 100
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    elif (flag == 4):
        minRange = -5
        maxRange = 5
        numberInRange = 100
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    elif (flag == 5):
        minRange = -100
        maxRange = 100
        numberInRange = 100
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    elif (flag == 6):
        minRange = -np.pi
        maxRange = np.pi
        numberInRange = 100
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    elif (flag == 7):
        minRange = 1e-6
        maxRange = 100
        numberInRange = 100
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    elif (flag == 8):
        minRange = -5
        maxRange = 1
        numberInRange = 100
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    elif (flag == 9):
        minRange = 1.1
        maxRange = 100
        numberInRange = 100
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    elif (flag == 10):
        minRange = 1e-6
        maxRange = 100
        numberInRange = 100
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    elif (flag == 11):
        # x can not be zero or close to zero   abs(x)>0.5
        # minRange =-21
        # maxRange = -0.5
        minRange = 0.5
        maxRange = 21.5
        numberInRange = 100
        numberInRange_new = 20
        x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)


 #**********************assignment 1 interpolate**********************

    fig = plt.figure()
    ax = fig.add_subplot('111')
    # create My Func   flag in range [1,11] corresponding to
    # function index in the first assignment
    func = myFunction([flag], minRange, maxRange, numberInRange)
    x_vec = func.getX()
    f1 = func.getFunc(flag)
    func.plotFunction(ax, f1, x_vec, color='b', marker=None)
    fx_new = func.Interpolate(f1, x_new)
    func.plotFunction(ax, fx_new, x_new, color='c', marker='*', linestyle='None')
    plt.title('assignment 1')
    plt.grid()
    plt.show()
#**********************end assignment 1********************************
# **********************assignment 2********************************
    # create My Func   flag in range [1,11] corresponding to
    # function index in the first assignment
    flag1=1
    flag2=2
    minRange = -18.5
    maxRange = 21.
    numberInRange = 80
    fig = plt.figure()
    ax = fig.add_subplot('111')
    func1 = myFunction([flag1, flag2], minRange, maxRange, numberInRange)
    # get x
    x_vec = func1.getX()
    # get f given flag
    f1 = func1.getFunc(flag1)
    f2 = func1.getFunc(flag2)
    func1.plotFunction(ax, f1, x_vec)
    func1.plotFunction(ax, f2, x_vec)
    func1.intersection(ax, flag1, flag2, 7, eps=0.001)
    plt.title('assignment 2')
    plt.grid()
    plt.show()
    # **********************end assignment 2********************************


    # **********************assignment 3********************************

    flag1 = 1
    flag2 = 2
    minRange = 0
    maxRange = 3
    numberInRange = 80
    fig = plt.figure()
    ax = fig.add_subplot('111')
    func2 = myFunction([flag1, flag2], minRange, maxRange, numberInRange)
    x_new = np.linspace(minRange + 0.25, maxRange - 0.25, numberInRange_new)
    x_vec = func2.getX()
    # get f given flag
    f1 = func2.getFunc(flag1)
    func2.plotFunction(ax, f1, x_vec, color='r', marker=None)
    f2 = func2.getFunc(flag2)
    func2.plotFunction(ax, f2, x_vec, color='r', marker=None)
    integral = func2.Integrate(f1,x_vec)
    print(f'integral f1 ={integral}')
    integral_between = func2.areabetween(f1,f2, x_vec)
    print(f'integral_between f1,f2 ={integral_between}')
    plt.title('assignment 3')
    plt.grid()
    plt.show()

##############################