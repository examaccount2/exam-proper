import newsrandom as NR 
#imports the newsrandom python file as a usable module similar to using pandas or any other non inbuilt pyhton module

# opens the txt file for the news html to use
def article():
    answer = NR.newschoice()
    with open(f"news and updates files/{answer}.txt", 'r') as file:
            content = file.read()
            return content


if __name__ == "__main__":
    print (article())