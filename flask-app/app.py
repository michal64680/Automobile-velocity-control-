import math
import numpy as np
import pandas as pd

from bokeh.embed import components
from bokeh.models import Slider,Legend
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.layouts import column, row

from flask import Flask, render_template, request

#from object import v, tt
from object import object


model=object()
model_before=object()

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
        model_before.change_parameters(Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha) 
        #model_before.change_parameters(Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha) 
        #script_velocity_plot_before, div_velocity_plot_before = components(velocity_plot(model_before.get_v(),model_before.get_x_axis(),t_sim))
        model.change_parameters(Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha)
        #script_velocity_slider, div_velocity_slider = components(slider_range())
        script_velocity_plot, div_velocity_plot = components(velocity_plot(model.get_v(),model.get_x_axis(),t_sim,0,0))
        script_u_plot, div_u_plot = components(u_plot(model.get_u(),model.get_x_axis(),t_sim,0,0))
        script_e_plot, div_e_plot = components(e_plot(model.get_e(),model.get_x_axis(),t_sim,0,0))
        return render_template('index.html',
        div_velocity_plot=div_velocity_plot,script_velocity_plot=script_velocity_plot,
        #div_velocity_plot_before=div_velocity_plot_before,script_velocity_plot_before=script_velocity_plot_before,
        div_u_plot=div_u_plot,script_u_plot=script_u_plot,
        div_e_plot=div_e_plot,script_e_plot=script_e_plot,
        v_zad=v_zad,
        Tp=Tp,
        t_sim=t_sim,
        drag=drag,
        Fp=Fp,
        m=m,
        load=load,
        Kp=Kp,
        Ti=Ti,
        Td=Td,
        alpha=alpha
        )

@app.route('/upload_value',methods=['GET', 'POST'])
def chart_post():
    global v_zad,Tp,t_sim,drag,Fp,m,load,Kp,Ti,Td,alpha
    selected_control = request.form.get('dropdown-select')
    model_before.change_parameters(Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha) 
    if request.method == 'POST' and request.form['drop-value'] == 'drop-value':
        print(selected_control)
        v_zad=request.form['slider_v_zad']
        v_zad=int(v_zad)
        Tp=request.form['slider_Tp']
        Tp=float(Tp)
        t_sim=request.form['slider_t_sim']
        t_sim=int(t_sim)
        drag=request.form['slider_drag']
        drag=float(drag)
        Fp=request.form['slider_Fp']
        Fp=int(Fp)
        m=request.form['slider_m']
        m=int(m)
        load=request.form['slider_load']
        load=int(load)
        Kp=request.form['slider_Kp']
        Kp=float(Kp)
        Ti=request.form['slider_Ti']
        Ti=float(Ti)
        Td=request.form['slider_Td']
        Td=float(Td)
        alpha=request.form['slider_alpha']
        alpha=float(alpha)
    model.change_parameters(Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha)
    script_velocity_plot, div_velocity_plot = components(velocity_plot(model.get_v(),model.get_x_axis(),t_sim,model_before.get_v(),model_before.get_x_axis()))
    script_u_plot, div_u_plot = components(u_plot(model.get_u(),model.get_x_axis(),t_sim,model_before.get_u(),model_before.get_x_axis()))
    script_e_plot, div_e_plot = components(e_plot(model.get_e(),model.get_x_axis(),t_sim,model_before.get_e(),model_before.get_x_axis()))
        
    return render_template('index.html',
    div_velocity_plot=div_velocity_plot,script_velocity_plot=script_velocity_plot,
    #div_velocity_plot_before=div_velocity_plot_before,script_velocity_plot_before=script_velocity_plot_before,
    div_u_plot=div_u_plot,script_u_plot=script_u_plot,
    div_e_plot=div_e_plot,script_e_plot=script_e_plot,
    v_zad=v_zad,
    Tp=Tp,
    t_sim=t_sim,
    drag=drag,
    Fp=Fp,
    m=m,
    load=load,
    Kp=Kp,
    Ti=Ti,
    Td=Td,
    alpha=alpha
    )

@app.route('/change_control',methods=['GET', 'POST'])
def change_control():
    global v_zad,Tp,t_sim,drag,Fp,m,load,Kp,Ti,Td,alpha
    selected_control = request.form.get('dropdown-select')
    model_before.change_parameters(Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha) 
    model.change_parameters(Tp, t_sim, drag, v_zad, Fp, m, load, Kp, Ti, Td, alpha)
    script_velocity_plot, div_velocity_plot = components(velocity_plot(model.get_v(),model.get_x_axis(),t_sim,model_before.get_v(),model_before.get_x_axis()))
    script_u_plot, div_u_plot = components(u_plot(model.get_u(),model.get_x_axis(),t_sim,model_before.get_u(),model_before.get_x_axis()))
    script_e_plot, div_e_plot = components(e_plot(model.get_e(),model.get_x_axis(),t_sim,model_before.get_e(),model_before.get_x_axis()))
        
    return render_template('index.html',
    div_velocity_plot=div_velocity_plot,script_velocity_plot=script_velocity_plot,
    #div_velocity_plot_before=div_velocity_plot_before,script_velocity_plot_before=script_velocity_plot_before,
    div_u_plot=div_u_plot,script_u_plot=script_u_plot,
    div_e_plot=div_e_plot,script_e_plot=script_e_plot,
    v_zad=v_zad,
    Tp=Tp,
    t_sim=t_sim,
    drag=drag,
    Fp=Fp,
    m=m,
    load=load,
    Kp=Kp,
    Ti=Ti,
    Td=Td,
    alpha=alpha,
    selected_control=selected_control
    )


def plot_line_styler(p):
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


def velocity_plot(v,tt,t_sim,v2,tt2):
    p = figure(x_range=(1, t_sim),title="Wykres prędkości", x_axis_label="s", y_axis_label="m/s", width=350, height=350)
    w1=p.line(tt, v,line_width=2, color="#033a63")
    w2=p.line(tt2, v2,line_width=2, color="#8B0000")
    plot_line_styler(p)

    legend = Legend(items=[
    ("Aktualny",   [w1]),
    ("Poprzedni", [w2]),
    ], location="top_right")
    p.add_layout(legend)
    return p

def u_plot(u,tt,t_sim,u2,tt2):
    p = figure(x_range=(1, t_sim),title="Sygnał sterowania", x_axis_label="s", y_axis_label="", width=350, height=350)
    w1=p.line(tt, u,line_width=2, color="#033a63")
    w2=p.line(tt2, u2,line_width=2, color="#8B0000")
    plot_line_styler(p)

    legend = Legend(items=[
    ("Aktualny",   [w1]),
    ("Poprzedni", [w2]),
    ], location="top_right")

    p.add_layout(legend)
    return p

def e_plot(e,tt,t_sim,e2,tt2):
    p = figure(x_range=(1, t_sim),title="Wykres błędu", x_axis_label="s", y_axis_label="", width=350, height=350)
    w1=p.line(tt, e,line_width=2, color="#033a63")
    w2=p.line(tt2, e2,line_width=2, color="#8B0000")
    plot_line_styler(p)
    legend = Legend(items=[
    ("Aktualny",   [w1]),
    ("Poprzedni", [w2]),
    ], location="top_right")

    p.add_layout(legend)
    return p






if __name__ == '__main__':
    app.run(debug=True)

    


    
