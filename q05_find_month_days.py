#Filename: q05_find_month_days.py
#Author: Tan Di Sheng
#Created: 20130129
#Modified: 20130129
#Description: This program prompts the user to enter the month and year,
#and displays the number of days in the month.

print("""This program prompts the user to enter the month and year,
and displays the number of days in the month.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    while True:
        monthInput = input("\nEnter month: ")
        yearInput = input("Enter year: ")
        try:
            int(yearInput) and int(monthInput)
        except:
            print("\nPlease input an integer between 1 and 12")
        else:
            if 1 <= int(monthInput) <= 12:
                break
            else:
                print("\nPlease input an integer between 1 and 12")

    yearInput = str(yearInput)
    monthInput = int(monthInput)
    print()
    
    if monthInput == 1:
        print("January " + yearInput + " has 31 days")
    elif monthInput == 3:
        print("March " + yearInput + " has 31 days")
    elif monthInput == 5:
        print("May " + yearInput + " has 31 days")
    elif monthInput == 7:
        print("July " + yearInput + " has 31 days")
    elif monthInput == 8:
        print("August " + yearInput + " has 31 days")
    elif monthInput == 10:
        print("October " + yearInput + " has 31 days")
    elif monthInput == 12:
        print("December " + yearInput + " has 31 days")
    elif monthInput == 4:
        print("April " + yearInput + " has 30 days")
    elif monthInput == 6:
        print("June " + yearInput + " has 30 days")
    elif monthInput == 9:
        print("September " + yearInput + " has 30 days")
    elif monthInput == 11:
        print("November " + yearInput + " has 30 days")
    elif monthInput == 2:
        #checks for leap year
        yearInput = int(yearInput)
        if yearInput % 400 == 0:
            print("February " + str(yearInput) + " has 29 days")
        elif yearInput % 4 == 0 and yearInput % 100 != 0:
            print("February " + str(yearInput) + " has 29 days")
        else:
            print("February " + str(yearInput) + " has 28 days")
    
    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
