import math
import numpy as np
import pandas as pd

from bokeh.embed import components
from bokeh.models import Slider
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.layouts import column, row

from flask import Flask, render_template, request

#from object import v, tt
from object import object


model=object()

Tp=0.1
t_sim=1000
drag=1.5
v_zad=50
Fp=1000
m=500
load=100
Kp=0.1
Ti=0.1
Td=0.01
alpha=0.5


app = Flask(__name__)

@app.route('/')
def chart():
        model.change_parameters(Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha)

        #script_velocity_slider, div_velocity_slider = components(slider_range())
        script_velocity_plot, div_velocity_plot = components(velocity_plot(model.get_v(),model.get_x_axis()))
        return render_template('index.html',div_velocity_plot=div_velocity_plot,script_velocity_plot=script_velocity_plot)

@app.route('/',methods=['GET', 'POST'])
def chart_post():
    v_zad=request.form['slider_proba']
    v_zad=int(v_zad)
    model.change_parameters(Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha) 

    #script_velocity_slider, div_velocity_slider = components(slider_range())
    script_velocity_plot, div_velocity_plot = components(velocity_plot(model.get_v(),model.get_x_axis()))
    #print(v_zad)
    return render_template('index.html',div_velocity_plot=div_velocity_plot,script_velocity_plot=script_velocity_plot)

def plot_line_styler(p):
    p.title.text = "Wykres prędkości od czasu"
    p.title.text_font_size = "25px"
    p.title.text_font_style = "bold"
    p.title.align = "center"
    #p.title.background_fill_color = "#033a63"
    p.title.text_color = "#033a63"
    p.axis.axis_label_text_font_style = "bold"
    p.axis.axis_label_text_font_size = "15pt"
    p.axis.axis_label_text_color = "#033a63"

def slider_range():
    return Slider(start=0, end = 100, value = 0, step = 1, title = "Wzmocnienie")

def velocity_plot(v,tt):
    p = figure(x_range=(1, 1000),title="Wykres_velocity", x_axis_label="s", y_axis_label="m/s")
    p.line(tt, v,line_width=2, color="#033a63")
    plot_line_styler(p)
    return p




if __name__ == '__main__':
    app.run(debug=True)

    


    
