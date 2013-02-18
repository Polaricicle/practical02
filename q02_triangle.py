#Filename: q02_triangle.py
#Author: Tan Di Sheng
#Created: 20130129
#Modified: 20130129
#Description: This program reads the three edges of a triangle and determines
#whether the input is valid. The input is valid if the sum of any two edges
#is greater than the third edge. The program will compute the perimeter of
#the triangle if the input is valid. Otherwise, display that the input is
#invalid.

print("""This program reads the three edges of a triangle and determines
whether the input is valid. The input is valid if the sum of any two edges
is greater than the third edge. The program will compute the perimeter of
the triangle if the input is valid. Otherwise, display that the input is
invalid.\n""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    while True:
        oneInput = input("Please enter the first edge of the triangle: ")
        twoInput = input("Please enter the second edge of the triangle: ")
        threeInput = input("Please enter the third edge of the triangle: ")
        try:
            float(oneInput) and float(twoInput) and float(threeInput)
        except:
            print("\nPlease input a number\n")
        else:
            break
        
    oneInput = float(oneInput)
    twoInput = float(twoInput)
    threeInput = float(threeInput)
        
    oneCase = oneInput + twoInput
    twoCase = twoInput + threeInput
    threeCase = oneInput + threeInput
    perimeterOutput = oneCase + threeInput

    if oneCase > threeInput and twoCase > oneInput and threeCase > twoInput:
        print("The perimeter of the triangle is " + perimeterOutput)
    else:
        print("Invalid triangle.")
        
    #gives the user an option to quit the application
    contorquit = input("Continue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
