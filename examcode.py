import csv
import os
from flask import Flask, render_template, request
from datetime import *
import pandas as pd
app = Flask(__name__) 



def footprintcalculator():
    number1= int(input('enter lec bill'))
    number2 = number1 * 105
    number3 = number2
    print (number3) 
    number2 = number1 * 105
    number3 = number2 + number3
    print (number3) 
    number2 = number1 * 113
    number3 = number2 + number3
    print (number3) 
    number1 = 10000
    number2 = number1 * 0.79
    number3 = number2 + number3
    print (number3) 
    number1 = 2
    number2 = number1 * 1100
    number3 = number2 + number3
    print (number3) 
    number2 = number1 * 4400
    number3 = number2 + number3
    print (number3) 
    newspaper = input ('do you recycle newspaper')
    if newspaper == 'Yes' or 'yes':
        number3 +=184
        print(number3)
    newspaper = input ('do you recycle tins and cans')
    if newspaper == 'Yes' or 'yes':
        number3 +=166
        print(number3)

    
@app.route('/', methods = ['GET', 'POST'])
def Booking():
    if request.method == 'POST':
        Name = request.form.get('name')
        Email= request.form.get('email')
        Date_of_booking = request.form.get('date of booking')
        date_of_booking_check = past_date(Date_of_booking)
        if date_of_booking_check == False:
            return render_template('Error_page.html')
        elif date_of_booking_check == True:
            Date_of_return = request.form.get('date of return')
            date_of_return_check = selected_date(Date_of_booking,Date_of_return)
            if date_of_return_check == False:
                return render_template('Error_page.html')
            elif date_of_return_check == True:
                Equipment = request.form.get('equipment')
                pass_check = Equipment_check(Equipment)
                if pass_check == True:
                    add_booking = os.path.isfile('Bookings.csv')
                    with open('Bookings.csv', 'a', newline = '' ) as file:
                        writer = csv.writer(file)
                        if not add_booking:
                            writer.writerow(['Name', 'Email', 'Date of Booking', 'Date of Return', 'Equipment' ])
                            writer.writerow([ Name, Email, Date_of_booking, Date_of_return, Equipment ])
                            return render_template('Conformation.html')
                        writer.writerow([ Name, Email, Date_of_booking, Date_of_return, Equipment ])
                        return render_template('Conformation.html')
                elif pass_check == False:
                    return render_template('Error_page.html')
    return render_template('Booking.html')



if __name__ == '__main__':
    footprintcalculator()
if __name__ == '__main__':
    app.run(debug=True)