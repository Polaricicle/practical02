#Filename: q10_find_largest.py
#Author: Tan Di Sheng
#Created: 20130130
#Modified: 20130130
#Description: This program uses a while loop to find the largest integer n
#such that n^3 is less than 12,000.

print("""This program finds the largest integer n such that n^2
is less than 12,000.""")

lInteger = 1

while not (lInteger**3 > 12000):
    lInteger = lInteger + 1

lInteger = lInteger - 1
print("\nThe largest integer is: " + str(lInteger))
