import matplotlib.pyplot as plt
import math
import time
import numpy as np
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

class object:
    def __init__(self) -> None:
        pass

    def change_parameters(self, Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha):
        self.Tp = Tp
        self.t_sim = t_sim
        self.N = int(self.t_sim/self.Tp)
        self.x_axis=np.arange(0.0,self.t_sim,self.Tp)
        self.drag = drag
        self.v = [0]
        self.v_zad = v_zad
        self.Fp = Fp
        self.m = m
        self.load = load
        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td
        self.alpha = (alpha*2*3.141529/360.0)
        self.e=[0]
        self.e_sum=[]
        self.u=[0]

        self.__start()

    def __controllerP(self,n):
        return (self.Kp*self.e[n])

    def __controllerI(self,n):
        u_i = 0
        if(n==0):
            self.e_sum.append(self.e[n])
        else:
            self.e_sum.append(self.e[n]+self.e_sum[n-1])
        u_i=self.e_sum[n]
        return ((self.Kp*self.Tp/self.Ti)*u_i)

    def __controllerD(self,n):
        if(n==0):
            return ((self.Kp * self.Td / self.Tp) * (self.e[n]))
        else:
            return ((self.Kp*self.Td/self.Tp)*(self.e[n]-self.e[n-1]))

    def __controllerPID(self,n):
        u_n = self.__controllerP(n)
        u_n += self.__controllerI(n)
        u_n += self.__controllerD(n)
        return u_n

    def __limit(self,u_n):
        if u_n>100:
            #print("More than 100%")
            u_n = 100
        elif u_n<-50:
            #print("Smaller than -50%")
            u_n = -50
        self.u.append(u_n)
        return u_n

    def __velocity(self,v_n,u_n):
        self.e.append(self.v_zad-v_n)
        return ((self.Tp/(self.m+self.load))*(self.Fp*self.__limit(u_n)-0.5*self.drag*v_n*v_n-(self.m+self.load)*10*math.sin(self.alpha))+v_n)
    
    def __start(self):
        for i in range(0,self.N-1):
            self.v.append(self.__velocity(self.v[i],self.__controllerPID(i)))
    
    def get_v(self):
        return self.v

    def get_u(self):
        return self.u

    def get_e(self):
        return self.e

    def get_x_axis(self):
        return self.x_axis