#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:55:02 2022

@author: natsukoyamaguchi
"""
from flask import Flask, render_template, request, flash
import math as m
import os.path

file_dir = os.path.dirname(__file__)
intro_route = os.path.join(file_dir, '/intro/')
operation_result_route = os.path.join(file_dir, '/operation_result/')

Flask_App = Flask(__name__)
Flask_App.config['SECRET_KEY'] = 'NY725'

@Flask_App.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',
                           abspath = intro_route)

@Flask_App.route(intro_route, methods=['GET', 'POST'])
def intro():
   return render_template('intro.html',
                          abspath = intro_route)

@Flask_App.route(operation_result_route, methods=['POST'])
def operation_result():
    
    first_input = request.form['Input1']
    second_input = request.form['Input2']
    third_input = request.form['Input3']
    fourth_input = request.form['Input4']
    sixth_input = request.form['Input6']
    seventh_input = request.form['Input7']
    
    option = request.form['inlineCheckbox']
    
    if option == 'option1':
        npol = 1
    else:
        npol = 2
    
    EIRP_units = request.form['EIRP_units']
    SEFD_units = request.form['SEFD_units']
    
    inputs = [first_input, second_input, third_input, fourth_input, str(npol), sixth_input, seventh_input]
    
    for i in range(len(inputs)):
        if len(inputs[i]) < 1:
            flash('Please do not leave any field empty.')
            return render_template(
                'index.html',  
                abspath = intro_route,
                result="Bad Input", 
                calculation_success=False)
    
    try: 
        sn = float(first_input)
        eirp = float(second_input)
        sefd = float(third_input)
        eta = float(fourth_input)
        tau = float(sixth_input)
        freq = float(seventh_input)
        
        if(eta < 0 or eta > 1):
            flash('Quantization efficiency needs to be between 0 and 1. Please try again.')
            return render_template(
                'index.html', 
                abspath = intro_route,
                result="Bad Input", 
                calculation_success=False)
        
        
        if EIRP_units == "cgs":
            eirp = eirp * (10**(-7))
        elif EIRP_units == "Arecibo":
            eirp = eirp * (2.2e13)
        
        if SEFD_units == "mks":
            sefd = sefd * (10**(26))
        elif SEFD_units == "cgs":
            sefd = sefd * (10**(23))
        

        result = m.sqrt((9 * (100**2) * (eirp/(10**13)) * (10/sefd) * (eta) * m.sqrt(npol * tau / freq))/(sn))
        result = float( '%.2f' % result)

        return render_template(
            'index.html', 
            abspath = intro_route,
            sn=sn, 
            eirp=eirp, 
            sefd=sefd, 
            eta=eta, 
            npol=npol, 
            tau=tau,
            freq=freq, 
            result=result, 
            calculation_success=True)
    
    except ZeroDivisionError:
        flash('Zero division error. Please try again.')
        return render_template(
            'index.html', 
            abspath = intro_route,
            result="Bad Input", 
            calculation_success=False)
    
    except ValueError:
        flash('Please enter only numerical values.')
        return render_template(
            'index.html', 
            abspath = intro_route,
            result="Bad Input", 
            calculation_success=False)
    

if __name__ == '__main__':
    Flask_App.debug = True 
    Flask_App.run()

    
