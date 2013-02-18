#Filename: q03_determine_grade.py
#Author: Tan Di Sheng
#Created: 20130129
#Modified: 20130129
#Description: This program prompts the user to enter a score between 0 and 100
#inclusive and returns the grade accordingly

print("""This program prompts the user to enter a score between
0 and 100 inclusive and returns the grade accordingly""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    while True:
        numberInput = input("\nEnter number: ")
        try:
            float(numberInput)
        except:
            print("\nPlease input an integer between 0 and 100")
        else:
            if 0 <= float(numberInput) <= 100:
                break
            else:
                print("Please input an integer between 0 and 100")       

    numberInput = float(numberInput)
    
    grades = ["A", "B", "C", "D", "E", "S", "U"]

    if numberInput >= 70:
        print(grades[0])
    elif numberInput >= 60:
        print(grades[1])
    elif numberInput >= 55:
        print(grades[2])
    elif numberInput >= 50:
        print(grades[3])
    elif numberInput >= 45:
        print(grades[4])
    elif numberInput >= 35:
        print(grades[5])
    else:
        print(grades[6])

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
