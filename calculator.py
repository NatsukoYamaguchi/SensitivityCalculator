#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:55:02 2022

@author: natsukoyamaguchi
"""
from flask import Flask, render_template, request

Flask_App = Flask(__name__)

@Flask_App.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@Flask_App.route('/variables/', methods=['GET', 'POST'])
def variables():
   return render_template('variables.html')

@Flask_App.route('/intro/', methods=['GET', 'POST'])
def intro():
   return render_template('intro.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    
    first_input = request.form['Input1']
    second_input = request.form['Input2']
    third_input = request.form['Input3']
    fourth_input = request.form['Input4']
    fifth_input = request.form['Input5']
    sixth_input = request.form['Input6']
    seventh_input = request.form['Input7']
    
    EIRP_units = request.form['EIRP_units']
    SEFD_units = request.form['SEFD_units']
    
    inputs = [first_input, second_input, third_input, fourth_input, fifth_input, sixth_input, seventh_input]
    
    for i in range(len(inputs)):
        if len(inputs[i]) < 1:
            return render_template(
                'index.html',  
                # operation=operation, 
                result="Bad Input", 
                calculation_success=False, 
                error = "Please do not leave any field empty.")
    
    for i in range(len(inputs)):
        if type(inputs[i]) != int and type(inputs[i]) != float:
            return render_template(
                'index.html',  
                # operation=operation, 
                result="Bad Input", 
                calculation_success=False, 
                error = "Please only enter numerical values.")
    
    try: 
        input1 = float(first_input)
        input2 = float(second_input)
        input3 = float(third_input)
        input4 = float(fourth_input)
        input5 = float(fifth_input)
        input6 = float(sixth_input)
        input7 = float(seventh_input)
        
        if EIRP_units == "cgs":
            input2 = input2 * (10**(-7))
        
        if SEFD_units == "mks":
            input3 = input3 * (10**(26))
        elif SEFD_units == "cgs":
            input3 = input3 * (10**(23))
        
        result = input1 * input2 * input3 * input4 * input5 * input6 * input7
        
        # if operation == "+":
        #     result = input1 + input2
        
        # elif operation == "-":
        #     result = input1 - input2
        
        # elif operation == "/":
        #     result = input1 / input2
        
        # elif operation == "*":
        #     result = input1 * input2
            
        # else:
        #     operation = "%"
        #     result = input1 % input2 
        
    
        return render_template(
            'index.html', 
            input1=input1, 
            input2=input2, 
            input3=input3, 
            input4=input4, 
            input5=input5, 
            input6=input6,
            input7=input7, 
            #operation=operation, 
            result=result, 
            calculation_success=True)
    
    except ZeroDivisionError:
        return render_template(
            'index.html', 
            input1=input1, 
            input2=input2, 
            input3=input3, 
            input4=input4, 
            input5=input5, 
            input6=input6,
            input7=input7, 
            # operation=operation, 
            result="Bad Input", 
            calculation_success=False, 
            error = "You cannot divide by zero")
    
    except ValueError:
        return render_template(
            'index.html', 
            input1=input1, 
            input2=input2, 
            input3=input3, 
            input4=input4, 
            input5=input5, 
            input6=input6,
            input7=input7, 
            # operation=operation, 
            result="Bad Input", 
            calculation_success=False, 
            error = "Cannot perform numeric operations with provided inputs.")
    
     

if __name__ == '__main__':
    Flask_App.debug = True 
    Flask_App.run()

    

