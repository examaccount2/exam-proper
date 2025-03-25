import random
import pandas as pd
import csv

def newschoice():
    num = random.randint(1,10)
    test = []
    df = pd.read_csv("newsnames.csv")
    with open('newsnames.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            test.append(row)
        tries = 0
        row_search = 0
        name_check = test[row_search].get('number', '').strip()
        while name_check != num and row_search < len(test):
            row_search +=1
            name_check = test[row_search - 1].get('number', '').strip()
            if row_search > len(test):
                row_search = 1
            name_check = int(name_check)
            if name_check == num:

                row = num -2
                column = 'article' 
                with open('newsnames.csv', 'r') as file:
                    csv_reader = csv.DictReader(file)
                    rows = list(csv_reader) 
                    if row < len(rows): 
                        value = rows[row].get(column, None)
                        article = value 
                        return article






if __name__ == '__main__':
    print(details_check_staff())



