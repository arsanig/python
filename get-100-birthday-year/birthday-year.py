import datetime
import string

currentDate = datetime.datetime.now()

name = input("What's your name?\n")
while not name.isalpha():
    print("Wrong input try again...\n")
    name = input("What's your name?\n")

age = input("What age will you be turning this year or have already turned?\n")
while not age.isdigit():
    print("Wrong input try again...\n")
    age = input("What age will you be turning this year or have already turned?\n")

hundredBirthdayYear = str(currentDate.year + (100 - int(age)))

print("Hi "+name+", "+"you will be 100 years old in "+hundredBirthdayYear)