#Filename: q08_top2_scores.py
#Author: Tan Di Sheng
#Created: 20130130
#Modified: 20130130
#Description: This program prompts the user to enter the number of students
#and each student's name and score, and finally displays the student
#with the highest score and the student with the second-highest score.

print("""This program prompts the user to enter the number of students
and each student's name and score, and finally displays the student
with the highest score and the student with the second-highest score.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:
    
    numberInput = input("\nEnter number of students: ")
    numberInput = int(numberInput)
    firstStudent = ""
    first = 0
    secondStudent = ""
    second = 0
    for i in range(1,(numberInput + 1)):
        nameInput = input("\nStudent's name: ".format(i))
        scoreInput = input(nameInput + "'s score: ".format(i))
        scoreInput = int(scoreInput)
        if (scoreInput > first):
            second = int(first)
            secondStudent = firstStudent
            first = scoreInput
            firstStudent = nameInput 
        if (scoreInput > second) and (scoreInput < first):
            second = scoreInput
            secondStudent = nameInput
            
    print("\nThe highest score is: " + str(first) + " by " + firstStudent)
    print("The 2nd highest score is: " + str(second) + " by " + secondStudent)
        
    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
