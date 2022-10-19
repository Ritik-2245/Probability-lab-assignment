from turtle import pos
from utils import Normal, Poisson,Uniform


def func():
    x=int(input('enter a key   1 for poisson distribution , 2 for uniform distribution, 3 for normal distribution , ctrl+c for cancelellation \n '))
    if x==1:
        while True:
            Lambda=int(input('enter the value of lambda -'))
            if Lambda<=0:
                print('enter a valid value of lambda')
            else:
                break
        
        plot=Poisson.Poisson(Lambda=Lambda)
        plot.plot_graph()
    
    elif x==2:
        while True:
            a=int(input('enter the value of a -'))
            b=int(input('enter the value of b -'))
            if b<=a:
                print('enter a valid value of a and b')
            else:
                break
        plot=Uniform.Uniform(a=a,b=b)
        plot.plot_graph()
    
    elif x==3:
        while True:
            mu=int(input('enter the value of expected mean - '))
            variance=int(input('enter the value of varaince - '))
            if variance<=0:
                print('enter a valid value of varaince')
            else:
                break
        
        plot=Normal.NormalDistribution(mu=mu,variance=variance)
        plot.plot_distribution()

if __name__ == "__main__": 
    while True:
        func()