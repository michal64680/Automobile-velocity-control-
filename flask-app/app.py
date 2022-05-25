# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:44:33 2022

@author: filip
"""
import math
import numpy as np
import pandas as pd

from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool, PrintfTickFormatter,Div, RangeSlider, Spinner
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models import Div, RangeSlider, Spinner

from flask import Flask, render_template, request

#from object import v, tt
import object




app = Flask(__name__)

@app.route('/')
def chart():
    selected_class = request.form.get('dropdown-select')
    script_velocity_plot, div_velocity_plot = components(velocity_plot(object.v,object.tt))
    #slider = range_slider(velocity_plot(object.v,object.tt))
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
'''
def range_slider(p):
    range_slider = RangeSlider(
    title="Adjust x-axis range",
    start=0,
    end=10,
    step=1,
    value=(p.x_range.start, p.x_range.end),)
    range_slider.js_link("value", p.x_range, "start",attr_selector=0)
    range_slider.js_link("value", p.x_range, "end",attr_selector=1)
'''
    
def velocity_plot(v,tt):
    p = figure(x_range=(1, 1000),title="Wykres_velocity", x_axis_label="s", y_axis_label="m/s")
    p.line(tt, v,line_width=2, color="#033a63")
    plot_line_styler(p)
    return p




if __name__ == '__main__':
    app.run(debug=True)

    


    
