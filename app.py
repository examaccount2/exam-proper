import os
import csv
from flask import Flask, render_template, request
from datetime import *
import articlechoice as AC

login_check = False

app = Flask(__name__) 

@app.route('/')
def first_page():
   hpinfo = homepageinforamtion()
   return render_template('index.html', hpinfo = hpinfo)

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
    article = AC.article()
    return render_template ('news.html',article = article)

@app.route('/login', methods = ['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        name = request.form.get('name', type=str)
        Password = request.form.get('password', type=str)
        print(name, Password)
        pass_check = details_check(name, Password)
        if pass_check == True:
           global login_check
           login_check = True
           return render_template('calculator.html')
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def Register():
    if request.method == 'POST':
        name = request.form.get('name')
        Password = request.form.get('password')
        Email = request.form.get('email')
        button = request.form.get('button')
        add_user = os.path.isfile('login.csv')

        print( name , Password, Email, button)
        with open('login.csv', 'a', newline = '' ) as file:
            writer = csv.writer(file)
            if not add_user:
                writer.writerow(['name', 'Password', 'Email' ])
                writer.writerow([ name , Password, Email  ])
            else:
                writer.writerow([ name, Password, Email ])
            return render_template('index.html')
    return render_template('register.html')


@app.route('/calculator', methods = ['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        
        Name = request.form.get('name')
        electric = int(request.form.get("electric bill number"))
        fuel = int(request.form.get('fuel bill number'))        
        heating = int(request.form.get("natural gas or heating bill"))
        car = float(request.form.get('car millage'))
        shortplane = int(request.form.get("short plane"))
        longplane = int(request.form.get('long plane'))
        newspaper = request.form.get("newspaper")
        tins = request.form.get("tinsandcans")

        print (newspaper , tins)
        print(login_check)
        thing1 = footprintcalculator (electric,fuel,heating,car,shortplane,longplane,newspaper,tins)
        if thing1 == 0.0:
            result1 = ""
        elif thing1 >0.0 and thing1 == float:
            result1 = answerfunction(thing1)
        else:
            result1 = "error, try the calculator without negitives"
            thing1 = ""

        return render_template(
        'calculator.html',
        thing = thing1,
        result = result1 
        )


    return render_template('calculator.html')


def details_check(name, Password):
    count= int()
    for row in open('login.csv'):
        count+= 1
    test = []
    with open('login.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            test.append(row)
        tries = 0
        row_search = 0
        name_check = test[row_search].get('name', '').strip() 
        # Now the line above goes into the CSV file and gets the first value it finds and checks it against the users input (which is below), if the data doesn't match it run back through the CSV - (next line)
        # with a plus one to the row it checks, so if it finds it on row two, it keeps the two value and checks to see if the password on the row matches as well, if it does then it loads the page back for - (next line)
        # them to try again. 
        while name_check != name and tries <=3 and row_search < len(test):              
            row_search +=1
            name_check = test[row_search].get('name').strip()
        else:
            password_check = test[row_search].get('password').strip()
            if password_check == Password and name_check == name:
                return True
            else:
                return False
    tries += 1

@app.route('/Error_page')
def error():
    return render_template('Error_page.html')

def footprintcalculator(electric,fuel,heating,car,shortplane,longplane,newspaper,tins):
    number = 0
    number2 = 0
    number = number
    number = electric * 105
    number += fuel * 105
    number += heating * 113
    number2 += car * 79
    number += shortplane * 1100
    number += longplane * 4400
    number += 350
    if newspaper == "True":
        number -=184
    if tins == "True":
        number -=166
    number *= 100
    number = float(number)
    number += number2
    number /= 100
    if number == 0.0:
        return ""
    elif number > 0.0 and number == float:
        return number
    else:
        return -1

def cart_enter(panel,meter,charger):
    count = int()
    for row in open('login.csv'):
        count+= 1
    test = []
    if panel == True:
        with open('login.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                test.append(row)
            tries = 0
            row_search = 0
            item_check = test[row_search].get('name', '').strip() 
            # Now the line above goes into the CSV file and gets the first value it finds and checks it against the users input (which is below), if the data doesn't match it run back through the CSV - (next line)
            # with a plus one to the row it checks, so if it finds it on row two, it keeps the two value and checks to see if the password on the row matches as well, if it does then it loads the page back for - (next line)
            # them to try again. 
            while name_check != "panel" and tries <=3 and row_search < len(test):              
                row_search +=1
                name_check = test[row_search].get('name').strip()
            else:
                test[row_search] += 1 
        tries += 1


def homepageinforamtion():
        with open(f"news and updates files/companyinformation.txt", 'r') as file:
            content = file.read()
            return content


def answerfunction(thing1):
    if thing1 < 6000.00:
        return "congratulations, you are below the threshold and are an exceptional at reducing your own emissions", option_1
    elif thing1 > 6000.00 and thing1 < 16000.00:
        return "not bad, you are doing well and are below average but you can do better, we can direct you to a part of our forum section on good ways of getting rid of emmissions with tiny life changes" , option_2
    elif thing1 > 16000.00 and thing1 < 22000.00: 
        return "not terrible but you can do better, here is a link to our store for recomendations for reducing emmision", option_3
    elif thing1 > 22000.00:
        return "you must really try hard in order to reduce your impact on the environment, here are good ways of doing so dramatically" , option_4

if __name__ == '__main__':
    app.run(debug=True)