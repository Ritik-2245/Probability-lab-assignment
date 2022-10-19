import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

class Uniform:
    def __init__(self,a=0,b=1):
        self.a=a
        self.b=b
        self.x=self.x_value()
        self.dist=self.pdf_value()
        self.mean=uniform.mean(self.a,self.b-self.a)
        self.variance=uniform.var(self.a,self.b-self.a)
        
            
    def x_value(self):
        return np.arange(self.a-10,self.b+10,0.01)   
    
    def pdf_value(self):
        return uniform.pdf(self.x,self.a,self.b-self.a)
    
    def plot_graph(self):
        plt.title("uniform probability distribution for random variables form %d to %d"%(self.a,self.b))
        plt.ylabel("probability")
        plt.xlabel('random variables')
        plt.figtext(0.02, 0.1,'mean - %s and variance - %s'%(self.mean,self.variance), fontsize=10)
        plt.subplots_adjust(bottom=0.25)
        plt.fill(self.x,self.dist)
        plt.plot(self.x,self.dist,'r--')
        plt.show()


if __name__ == "__main__":
    s=Uniform(a=3,b=8)
    s.plot_graph()