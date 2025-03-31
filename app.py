import os
import csv
from flask import Flask, render_template, request
from datetime import *
import articlechoice as AC

app = Flask(__name__) 

# renders the first page with the page information written into the txt file

@app.route('/')
def first_page():
   hpinfo = homepageinforamtion()
   return render_template('index.html', hpinfo = hpinfo)

# rerenders the first page if the user relinks back to it
@app.route('/index')
def back_to_start():
   return render_template('index.html')

# renders the store
@app.route('/store')
def store ():   
    return render_template ('store.html')



# renders the cart
@app.route('/cart')
def cart ():
    return render_template ('cart.html')

# renders the news area
@app.route('/news')
def news_and_updates ():
    article = AC.article()
    return render_template ('news.html',article = article)

# renders the login page
@app.route('/login', methods = ['GET', 'POST'])
def sign_in():
    # looks through the csv to check wether the name and password are correct
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

# renders the regester page
@app.route('/register', methods = ['GET', 'POST'])
def Register():
    if request.method == 'POST': 
        # alters the csv so that the user can log in later
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

# renders the calulator
@app.route('/calculator', methods = ['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        #takes the html inputs and puts them into variables for the calcualtor to use
        Name = request.form.get('name')
        electric = int(request.form.get("electric bill number"))
        fuel = int(request.form.get('fuel bill number'))        
        heating = int(request.form.get("natural gas or heating bill"))
        car = float(request.form.get('car millage'))
        shortplane = int(request.form.get("short plane"))
        longplane = int(request.form.get('long plane'))
        newspaper = request.form.get("newspaper")
        tins = request.form.get("tinsandcans")

        thing1 = footprintcalculator (electric,fuel,heating,car,shortplane,longplane,newspaper,tins)

        if thing1 == 0.0:
            waste = ""
            result1 = ""
        elif thing1 > 0.0:
            waste = "pounds of waste"
            result1 = answerfunction(thing1)
        elif thing1 < 0.0:
            result1 = "error, try the calculator without negitives"
            thing1 = ""
            waste = ""
        else:
            # worst case scenario if the system fully brakes beyond how it could
            print(thing1)
            result1 = "error, if you see this contact the site admin and provide information what was was done so the error can be addressed"
            thing1 = ""
            waste = ""


        return render_template(
        'calculator.html',
        thing = thing1,
        result = result1,
        waste = waste
        )


    return render_template('calculator.html')


def details_check(name, Password):
    # checks to see if the name and password are correct for the login to work
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

# renders the store
@app.route('/Error_page')
def error():
    return render_template('Error_page.html')

# the calualtor tat takes the numbers rom the html and does the calulations for them to be output into the csv
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
    number += float(number2)
    number /= 100

    if number == 0.0:
        return ""
    elif number > 0.0 and number == float:
        return number
    else:
        return -1

# the cart csv code that doesnt work sue to it not being in my skill set to get right
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
            while name_check != "panel" and tries <=3 and row_search < len(test):              
                row_search +=1
                name_check = test[row_search].get('name').strip()
            else:
                test[row_search] += 1 
        tries += 1

# the information for the homapage to work correctly
def homepageinforamtion():
        with open(f"news and updates files/companyinformation.txt", 'r') as file:
            content = file.read()
            return content

# for after the calulator number to be more bespoke to the user 
def answerfunction(thing1):
    if thing1 < 6000.00:
        return "congratulations, you are below the threshold and are an exceptional at reducing your own emissions"
    elif thing1 > 6000.00 and thing1 < 16000.00:
        return "not bad, you are doing well and are below average but you can do better, we can direct you to a part of our forum section on good ways of getting rid of emmissions with tiny life changes"
    elif thing1 > 16000.00 and thing1 < 22000.00: 
        return "not terrible but you can do better, here is a link to our store for recomendations for reducing emmision"
    elif thing1 > 22000.00:
        return "you must really try hard in order to reduce your impact on the environment, here are good ways of doing so dramatically"

# to make the code run correctly
if __name__ == '__main__':
    app.run(debug=True)