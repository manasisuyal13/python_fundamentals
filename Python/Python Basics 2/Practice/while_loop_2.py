'''

Homework 25-09-2026

The Challenge: Login System with Limited Attempts
Write a program that simulates a login system with a maximum of 3 attempts.
Requirements:
Maintain a variable to count the number of attempts used (or remaining).
Use a while loop to prompt the user to enter a password using input().
If the user enters cyber2026:
Print "Access Granted!"
Immediately exit the loop using break.
If the user enters an incorrect password:
Deduct an attempt and inform the user how many attempts they have left (e.g., "Incorrect password. Attempts remaining: 2").
If the user runs out of attempts (reaches 0 remaining):
Print "Account Locked. Too many failed attempts." and stop asking.
Hints (if you need them)
You can control the loop condition using the attempt count (e.g., while attempts > 0:) or use while True: combined with a break when attempts reach zero.
Think carefully about where you place your attempt counter updates relative to the check!


'''
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == "cyber2026":
        print("Access Granted!")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print(f"Incorrect password. Attempts remaining: {attempts}")
        else:
            print("Account Locked. Too many failed attempts.")