import numpy as np  # Required of numeric library (array)
import matplotlib.pyplot as plt # Required for plotting    

class function:
    def __init__(self,equation):
        self.equation = "("+equation+")"
        self.h = 10**-8
    def __add__(self, other):
        return function(str(self.equation) +"+"+ str(other.equation))
        
    def __sub__(self, other):
        return function(str(self.equation) +"+ (-1*"+ str(other.equation)+")")
    def __mul__(self, other):
        return function(str(self.equation) +"*"+ str(other.equation))
    def __truediv__(self, other):
        return function(str(self.equation) +"/"+ str(other.equation))
    def call(self,x):
        return eval(self.equation)
    def __str__(self):
        return str(self.equation)
    def deriv(self,x):
        return (self.call(x+self.h)-self.call(x))/self.h
    def plot_deriv(self,x_min,x_max):
        x = np.linspace(x_min,x_max,1000)
        plt.plot(x,self.deriv(x))
        plt.show()
    def plot_graph(self,x_min,x_max):
        x = np.linspace(x_min,x_max,1000)
        plt.plot(x,self.call(x))
        plt.show()
    
        
        
        
        
        
        
    
f1 =  function("x**2")
h1 =  function("x+2")
g1 = f1+h1
x = 10
#print(g1.deriv(x)-(f1.deriv(x)+h1.deriv(x)))
f1.plot_graph(-10,10)
