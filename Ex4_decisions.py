# -------------------------------------------
# Exercise 4: Decision-Making Program
# -------------------------------------------
# In this exercise, you will write a program that makes decisions based on user input.
# You will practice combining Boolean logic with conditional statements.
#
# Goals:
# - Ask the user for input
# - Use conditions to decide what to do
# - Print messages based on the conditions
# - Test your program with different inputs

# -------------------------------------------
# Task 1: Simple decision
# -------------------------------------------
# Note: Read all of the instructions below first before starting!

# Ask the user to enter a number.
# Decide something about the number using an if statement.

# Example of syntax (no answer given):
# if some_condition:
#     print("Message for True condition")

# TODO:
# 1. Ask the user to type a number and store it in a variable.
# 2. Use an if statement to check something about the number.
# 3. Print a message if the condition is True.

# Write your code below:

number = int(input("Enter a number \n"))
if number > 50:
   print ("That is a big number.")
# -------------------------------------------
# Task 2: Add else
# -------------------------------------------
# Note: Read all of the instructions below first before starting!

# Sometimes we need to print a different message if the condition is False.

# Example of syntax (no answer given):
# if some_condition:
#     print("Message if True")
# else:
#     print("Message if False")

# TODO:
# 1. Add an else statement to your code from Step 1.
# 2. Print a different message if the number does not meet your condition.

# Write your code below:

number = int(input("Enter a number \n"))
if number > 50:
   print ("That is a big number.")
else:
   print("That is a small number.")

# -------------------------------------------
# Task 3: Multiple conditions
# -------------------------------------------
# Note: Read all of the instructions below first before starting!

# You can check more than one condition using elif or Boolean operators.

# Example of syntax (no answer given):
# if condition1:
#     print("Message 1")
# elif condition2:
#     print("Message 2")
# else:
#     print("Message 3")

# TODO:
# 1. Extend your program to check multiple conditions.
# 2. Print different messages for each case.
# 3. Test your program with different inputs to see all possible messages.

# Write your code below:

number = int(input("Enter a number \n"))
if number > 50:
   print ("That is a big number.")
elif number == 50:
   print ("That is exactly same number.")
else:
   print("That is a small number.")
# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run the following commands:
#    git add Ex4_decisions.py
#    git commit -m "Completed decision-making program exercise"
#    git push origin main
# Check GitHub to see your changes.
# -------------------------------------------

# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1:
# Ask the user for a number and a word.
# Use conditions to print a message only if the number is greater than a value
# AND the word matches a stored word.

stored_number = 50
stored_word = "hello"
number = int(input("Enter a number: "))
word = input("Enter a word: ")
if number > stored_number and word == stored_word:
    print("Both conditions are true.")
else:
    print("Both conditions not met.")    
# Extension 2:
# Ask the user for a number.
# Print different messages depending on:
# - number is positive
# - number is zero
# - number is negative

number = int(input("Enter a number: "))
if number > 0:
    print("number is positive. ")
elif number == 0:
    print ("number is zero.")
else:
    print("number is negative.") 


# Extension 3 (more challenging):
# Create a small quiz:
# - Ask the user a multiple-choice question.
# - Check their answer and print "Correct!" or "Try again!".
# - Add another condition to give a special message if the answer is partially correct.

# Write your extension code below:


   
print("===Welcome to the Quiz===\n")
print("What is the capital of France?")
print("A) London")
print("B) Berlin")
print("C) Paris")
print("D) Madrid")

answer = input("Your answer: ").upper().strip()
if answer == "C": 
    print("Correct!\n")  
elif answer == "PARIS":
    print("Right answer, but please use the letter next time!\n")     
else :
    print("Incorrect. The answer is (C) Paris.\n")
# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run the following commands:
#    git add Ex4_decisions.py
#    git commit -m "Completed extension activities"
#    git push origin main
# Check GitHub to see your changes.
# -------------------------------------------
