import matplotlib.pyplot as plt
import math
import time
import numpy as np
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
Tp=0.1

A = 1.5 #opory
#B=0.035
#Qd=0.05
#h=[0]
v=[0]
#h_zad = 8
v_zad = 50
F = 1000
m=500
t_sim=1000
N=int(t_sim/Tp)
tt=np.arange(0.0,t_sim,Tp)
Kp = 0.02
Ti = 0.1
Td = 1.5
e=[0]
e_sum=[]

def controllerP(Kp,n):
    return (Kp*e[n])

def controllerI(Kp,Tp,Ti,n):
    u_i = 0
    if(n==0):
        e_sum.append(e[n])
    else:
        e_sum.append(e[n]+e_sum[n-1])
    u_i=e_sum[n]
    print(u_i)
    return ((Kp*Tp/Ti)*u_i)

def controllerD(Kp,Tp,Td,n):
    if(n==0):
        return ((Kp * Td / Tp) * (e[n]))
    else:
        return ((Kp*Td/Tp)*(e[n]-e[n-1]))

def controllerPID(Kp,Tp,Td,Ti,n):
    u_n = controllerP(Kp,n)
    u_n += controllerI(Kp,Tp,Ti,n)
    u_n += controllerD(Kp,Tp,Td,n)
    return u_n

def limit(u_n):
    print(u_n)
    if u_n>100:
        print("More than 100%")
        u_n = 100
    elif u_n<-50:
        print("Smaller than 0%")
        u_n = -50
    return u_n

def velocity(v_n,u_n):
    #try:
    e.append(v_zad-v_n)
    #print(v_n)
    return ((Tp/m)*(F*limit(u_n)-0.5*A*v_n*v_n-m*10*math.sin(0.0))+v_n)
    #return ((Tp/A)*(drainage_intensity(u_n)-B*math.sqrt(h_n))+h_n)
    #except:
        #return drainage_intensity(u_n)


for i in range(0,N-1):
    v.append(velocity(v[i],controllerPID(Kp,Tp,Td,Ti,i)))
    print(e[i])


#plt.clf()
plt.plot(tt,v)
plt.xlabel("Czas [min]")
plt.ylabel("Prędkosc")
plt.grid()
plt.show()

#output_file('filename.html')  # Render to static HTML, or
 # Render inline in a Jupyter Notebook

# Set up the figure(s)
 # Instantiate a figure() object
#fig = figure(title='My Coordinates',
#             plot_height=300, plot_width=300,
#             toolbar_location=None)

# Draw the coordinates as circles
#fig.line(x=tt, y=v,
 #          color='green')
# Connect to and draw the data

# Organize the layout

# Preview and save
#show(fig)

