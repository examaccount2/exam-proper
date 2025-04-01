import random
import pandas as pd
import csv

#takes a random number from the range of 1 - 10 and turns it into the name for a txt file from the csv to be used for the news randomizer

def newschoice():
    num = random.randint(1,10)
    test = []
    df = pd.read_csv("newsnames.csv")
    with open('newsnames.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            test.append(row)
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
    print(newschoice())



