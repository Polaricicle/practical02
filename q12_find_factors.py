#Filename: q12_find_factors.py
#Author: Tan Di Sheng
#Created: 20130130
#Modified: 20130130
#Description: This program reads the integer input and displays all its
#smallest factors

print("""This program reads the integer input and displays all its
smallest factors.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    while True:
        numberInput = input("\nEnter the integer: ")
        try:
            int(numberInput)
        except:
            print("\nPlease input integer values.")
        else:
            break

    numberInput = int(numberInput)
    i = 2
    
    while (numberInput != 1):
        if (numberInput % i == 0):
            print(i)
            numberInput = numberInput / i
        else:
            i = i + 1
            
            
    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
