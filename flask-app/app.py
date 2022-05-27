# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:44:33 2022

@author: filip
"""
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
import object
import os

v_zad=0


app = Flask(__name__)

@app.route('/')
def chart():
        #script_velocity_plot, div_velocity_plot = components({"p": velocity_plot(object.v,object.tt), "slider1":row(slider1), "slider2":row(slider2)})
        script_velocity_slider, div_velocity_slider = components(slider_range())
        script_velocity_plot, div_velocity_plot = components(velocity_plot(object.v,object.tt))
        #slider = range_slider(velocity_plot(object.v,object.tt))
        return render_template('index.html',div_velocity_plot=div_velocity_plot,script_velocity_plot=script_velocity_plot,
        div_velocity_slider=div_velocity_slider,script_velocity_slider=script_velocity_slider)

@app.route('/',methods=['GET', 'POST'])
def chart_post():
    v_zad=request.form['slider_proba']
    #print(v_zad)
    #os.system('object')
        
    #script_velocity_plot, div_velocity_plot = components({"p": velocity_plot(object.v,object.tt), "slider1":row(slider1), "slider2":row(slider2)})
    script_velocity_slider, div_velocity_slider = components(slider_range())
    script_velocity_plot, div_velocity_plot = components(velocity_plot(object.v,object.tt))
    #slider = range_slider(velocity_plot(object.v,object.tt))
    return render_template('index.html',div_velocity_plot=div_velocity_plot,script_velocity_plot=script_velocity_plot,
    div_velocity_slider=div_velocity_slider,script_velocity_slider=script_velocity_slider)

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

    


    
