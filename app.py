
import csv
import os
from flask import Flask, render_template, request
from datetime import *
import pandas as pd
app = Flask(__name__) 

@app.route('/')
def first_page():
   return render_template('index.html')

@app.route('/index')
def back_to_start():
   return render_template('index.html')

@app.route('/store')
def store ():
    return render_template ('store.html')

@app.route('/login')
def login ():
    return render_template ('login.html')

@app.route('/register')
def register ():
    return render_template ('register.html')

@app.route('/cart')
def cart ():
    return render_template ('cart.html')

@app.route('/news')
def news_and_updates ():
    return render_template ('news.html')

# @app.route('/sign_in', methods = ['GET', 'POST'])
# def sign_in():
#     if request.method == 'POST':
#         Student_number = request.form.get('student_number', type=str)
#         if len(Student_number) != 8:
#             return render_template('index.html') 
#         if Student_number.__contains__('E'):
#             return render_template('index.html') 
#         Password = request.form.get('password', type=str)
#         print(Student_number, Password)
#         pass_check = details_check(Student_number, Password)
#         if pass_check == True:
#             CSV_check()
#             os.replace('C:/Users/phant/Documents/FOL/Equipment_log.html', 'C:/Users/phant/Documents/FOL/templates/Equipment_log.html')
#             return render_template('Homepage.html')
#     return render_template('index.html')

@app.route('/Register', methods = ['GET', 'POST'])
def Register():
    if request.method == 'POST':
        Student_number = request.form.get('student number')
        if len(Student_number) != 8:
            return render_template('Register.html')
        Password = request.form.get('password')
        Email = request.form.get('email')
        add_user = os.path.isfile('Student.csv')
        with open('Student.csv', 'a', newline = '' ) as file:
            writer = csv.writer(file)
            if not add_user:
                writer.writerow(['Student Number', 'Password', 'Email' ])
                writer.writerow([  Student_number, Password, Email  ])
            else:
                writer.writerow([ Student_number, Password, Email ])
            return render_template('Homepage.html')
    return render_template('Register.html')

@app.route('/calculator', methods = ['GET', 'POST'])
def Booking():
    if request.method == 'POST':
        Name = request.form.get('name')
        electric = int(request.form.get("electric bill number"))
        fuel = int(request.form.get('fuel bill number'))        
        heating = int(request.form.get("natural gas or heating bill"))
        car = float(request.form.get('car millage'))
        shortplane = int(request.form.get("short plane"))
        longplane = int(request.form.get('long plane'))

        
        answer = footprintcalculator(electric,fuel,heating,car,shortplane,longplane)

        render_template(
        'calculator.html',
        answer = "10"
        )


    return render_template(
        'calculator.html',
        )


@app.route('/Error_page')
def error():
    return render_template('Error_page.html')
def footprintcalculator(electric,fuel,heating,car,shortplane,longplane):
    number = 0
    number2 = 0
    number = number
    number = electric * 105
    number += fuel * 105
    number += heating * 113
    number2 += car * 79
    number += shortplane * 1100
    number += longplane * 4400
    # newspaper = input ('do you recycle newspaper')
    # if newspaper == 'Yes' or 'yes':
    #     number +=184
    #    print(number)
    # newspaper = input ('do you recycle tins and cans')
    # if newspaper == 'Yes' or 'yes':
    #     number +=166
    #     print(number)
    number *= 100
    number = float(number)
    number += number2
    number /= 100
    print(number)



if __name__ == '__main__':
    app.run(debug=True)