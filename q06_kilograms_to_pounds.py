#Filename: q06_kilograms_to_pounds.py
#Author: Tan Di Sheng
#Created: 20130130
#Modified: 20130130
#Description: This program changes the input from kilograms to pounds

print("This program displays the conversion rate from kilograms to pounds\n")

print("Kilograms Pounds")
for i in range(1, 11):
    pounds = i * 2.2
    i = str(i)
    print("{0:10}{1:<.1f}".format(i,pounds))

