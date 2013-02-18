#Filename: q04_determine_leap_year.py
#Author: Tan Di Sheng
#Created: 20130129
#Modified: 20130129
#Description: This program prompts the user to enter
#a year and determines whether it is a leap year.

print("""This program prompts the user to enter
a year and determines whether it is a leap year.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    while True:
        yearInput = input("\nEnter year: ")
        try:
            int(yearInput)
        except:
            print("\nPlease input an integer")
        else:
            break

    yearInput = int(yearInput)
    
    if yearInput % 1000 == 0:
        print(str(yearInput) + " is a leap year")
    elif yearInput % 100 == 0:
        print(str(yearInput) + " is not a leap year")
    elif yearInput % 4 == 0:
        print(str(yearInput) + " is a leap year")
    else:
        print(str(yearInput) + " is not a leap year")

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
