#Filename: q11_find_gcd.py
#Author: Tan Di Sheng
#Created: 20130130
#Modified: 20130130
#Description: This program finds the greatest common divisor of two integers

print("This program finds the greatest common divisor of two integers.")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    while True:
        firstInput = input("\nEnter the first integer: ")
        secondInput = input("Enter the second integer: ")
        try:
            int(firstInput) and int(secondInput)
        except:
            print("\nPlease input integer values.")
        else:
            break

    min = firstInput
    if (min > secondInput):
        min = secondInput

    firstInput = int(firstInput)
    secondInput = int(secondInput)
    min = int(min)

    while not (min == 1):
        if (firstInput % min == 0) and (secondInput % min == 0):
            break
        min = min - 1

    print("\nThe greatest common divisor of {0} and {1} is {2}".format(firstInput, secondInput, min))
            
    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
