from scipy.stats import poisson
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider,Button


class Poisson:
    def __init__(self,Lambda=10) :
        self.Lambda=Lambda
        self.x=np.arange(0,200,1)
        self.pmf=self.pmf_value()
        self.cdf=self.cdf_value()
        
    def pmf_value(self):
        return poisson.pmf(self.x,mu=self.Lambda)
    
    def cdf_value(self):
        return poisson.cdf(self.x,mu=self.Lambda)
    
    
    def plot_graph(self):
        fig,ax=plt.subplots(1,2,figsize=(15, 6))
        pmf_curve,=ax[0].plot(self.x,self.pmf,lw=2)
        fig.suptitle("Poisson probability distribution")
        ax[0].set_title("PMF")
        ax[0].set_xlabel("random variables")
        ax[0].set_ylabel("probability")
        ax[1].set_ylabel("cumulative probability")
        ax[1].set_xlabel("random variables")
        ax[1].set_title("CDF")
        
        cdf_curve,=ax[1].plot(self.x,self.cdf)
        fig.subplots_adjust(bottom=0.25,)
        fig.subplots_adjust(bottom=0.25,)
        axmu=fig.add_axes([0.25,0.1,0.65,0.03])
        
        Lambda_slider=Slider(ax=axmu,label='Lambda',valmin=0.1,valmax=100,valinit=self.Lambda)

       
        def update(val):
            self.Lambda=Lambda_slider.val
            print("value of lambda - %s mean of the distribution - %s variance of the distribution - %s"%(self.Lambda,self.Lambda,self.Lambda))
            self.cdf=self.cdf_value()
            self.pmf=self.pmf_value()
            cdf_curve.set_ydata(self.cdf)
            cdf_curve.set_xdata(self.x)
            
            # print('mean - %s and variance - %s'%(mean,vari))
            pmf_curve.set_ydata(self.pmf)
            pmf_curve.set_xdata(self.x)
            fig.canvas.draw_idle() 
        
        
        resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
        button = Button(resetax, 'Reset', hovercolor='0.975')


        def reset(event):
            Lambda_slider.reset()
            
        button.on_clicked(reset)

        Lambda_slider.on_changed(update)

        plt.show()  


if __name__ == "__main__":
    s=Poisson(Lambda=20)
    s.plot_graph()