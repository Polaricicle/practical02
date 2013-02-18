#Filename: q01_check_even.py
#Author: Tan Di Sheng
#Created: 20130129
#Modified: 20130129
#Description: This program reads an integer and checks whether it is even

print("This program reads an integer and checks whether it is even.\n")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    while True:
        numberInput = input("Enter number: ")
        try:
            int(numberInput)
        except:
            print("\nPlease input an integer\n")
        else:
            break
        
    numberInput = int(numberInput)
    
    #checks if the number is even or odd
    if numberInput % 2 == 0:
        print("The number " + str(numberInput) + " is even.\n")
    elif numberInput % 2 == 1:
        print("The number " + str(numberInput) + " is odd.\n")
        
    #gives the user an option to quit the application
    contorquit = input("Continue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
