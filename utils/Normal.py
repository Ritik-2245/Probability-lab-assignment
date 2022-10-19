import scipy.stats as stats
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider,Button

class NormalDistribution:
    def __init__(self,mu=1,variance=1):
        self.mu=mu
        self.variance=variance
        self.sigma = math.sqrt(self.variance)
        self.x=self.x_value()
        self.pdf=self.pdf_value()
        self.cdf=self.cdf_value()
    
    def x_value(self):
        return np.linspace(self.mu-10*self.sigma,self.mu+10*self.sigma, 300)
    
    def pdf_value(self):
        return stats.norm.pdf(self.x,self.mu,self.sigma)
    
    def cdf_value(self):
        return stats.norm.cdf(self.x,self.mu,self.sigma)
    
    def plot_distribution(self) -> None:
        fig,ax=plt.subplots(1,2,figsize=(15, 6))
        # plt.title("Normal probability distribution")
        pdf_curve,=ax[0].plot(self.x,self.pdf,lw=2)
        pdf_curve.fillStyles='steps-pre'
        fig.suptitle("Normal probability distribution")
        ax[0].set_title("PDF")
        ax[0].set_xlabel("random variables")
        ax[0].set_ylabel("probability")
        ax[1].set_ylabel("cumulative probability")
        ax[1].set_xlabel("random variables")
        ax[1].set_title("CDF")
        cdf_curve,=ax[1].plot(self.x,self.cdf)
        fig.subplots_adjust(left=0.25, bottom=0.25,)
        
        axmu=fig.add_axes([0.25,0.1,0.65,0.03])
        
        mu_silder=Slider(ax=axmu,label='mu',valmin=0.1,valmax=30,valinit=self.mu)

        ax_vari=fig.add_axes([0.1,0.25,0.0225,0.63])

        vari_slider=Slider(ax=ax_vari,label='variance',valmin=0,valmax=30,valinit=self.variance,orientation='vertical')
     
        def update(val):
            self.mu=mu_silder.val
            self.variance=vari_slider.val
            self.sigma=math.sqrt(self.variance)
            self.cdf=self.cdf_value()
            self.x=self.x_value()
            self.pdf=self.pdf_value()
            cdf_curve.set_ydata(self.cdf)
            cdf_curve.set_xdata(self.x)
            
            pdf_curve.set_ydata(self.pdf)
            pdf_curve.set_xdata(self.x)
            fig.canvas.draw_idle() 
        
        
        resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
        button = Button(resetax, 'Reset', hovercolor='0.975')


        def reset(event):
            mu_silder.reset()
            vari_slider.reset()
        button.on_clicked(reset)

        mu_silder.on_changed(update)
        vari_slider.on_changed(update)

        plt.show()  
        

    
if __name__ == "__main__":
    s=NormalDistribution(mu=2,variance=2)
    s.plot_distribution()