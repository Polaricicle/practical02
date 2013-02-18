#Filename: q09_find_smallest.py
#Author: Tan Di Sheng
#Created: 20130130
#Modified: 20130130
#Description: This program uses a while loop to find the smallest integer n
#such that n^2 is greater than 12,000.

print("""This program finds the smallest integer n such that n^2
is greater than 12,000.""")

sInteger = 1

while (sInteger**2 < 12000):
    sInteger = sInteger + 1

print("\nThe smallest integer is: " + str(sInteger))
