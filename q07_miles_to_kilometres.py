#Filename: q06_kilograms_to_pounds.py
#Author: Tan Di Sheng
#Created: 20130130
#Modified: 20130130
#Description: This program changes the input from miles to kilometres

print("This program displays the conversion rate from miles to kilometres\n")

print("Miles Kilometers Kilometers Miles")
for i in range(1, 11):
    i = int(i)
    miles = i * 1.609
    m = 15 + 5*i
    milestwo = m * 1.609
    print("{0:<6}{1:<11.3f}{2:<11}{3:<.3f}".format(i,miles,m,milestwo))

