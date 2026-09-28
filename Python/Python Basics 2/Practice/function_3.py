'''
🎯 The Challenge: ATM Deposit & Security Monitoring
Write a Python function named atm_system that takes three parameters:

account_holder (a string, e.g., "Shaafi")

correct_pin (a string, e.g., "9876")

balance (a float/int starting value, e.g., 1000.0)

📋 Function Logic Requirements:
PIN Security Check:

Prompt the user for a PIN using input("Enter PIN: ").

Allow up to 3 attempts.

If an invalid PIN is entered, print "Invalid PIN. Attempts left: X".

If all 3 attempts fail, print "Account locked due to multiple failed attempts." and return "LOCKED".

Transaction Menu:
Once the PIN is correct, print "Welcome, <account_holder>!" and enter a while loop with four options:

"deposit":

Prompt: input("Enter deposit amount: ")

If the amount is less than or equal to 0, print "Invalid deposit amount!" and use continue to restart the loop.

Otherwise, add the amount to balance and print "Deposit successful! New balance: <balance>".

"withdraw":

Prompt: input("Enter withdrawal amount: ")

If the amount is greater than balance, print "Insufficient funds!".

Otherwise, deduct the amount from balance and print "Withdrawal successful! Remaining balance: <balance>".

"passcode":

Use pass as a placeholder for a feature you plan to build later (e.g., changing PIN).

"exit":

Print "Session closed. Have a great day!" and return balance.

Any other command:

Print "Command not recognized, try again."

💡 Example Call to Test Your Code:
Python
final_status = atm_system("Shaafi", "9876", 1500.0)
print("Result:", final_status)

'''

def atm_system(account_holder, correct_pin, balance):
    attempt = 3
        
    while attempt > 0:
        pin = input("Enter PIN: ")
        if pin == correct_pin:
            print("Access Granted!")
            print(f"Welcome, {account_holder}!")
            break
        attempt -= 1
        if attempt > 0:
            print(f"Invalid PIN. Attempts left: {attempt}")
        else:
            print("Account locked due to multipe failed attempts")
            return "LOCKED"
    
    while True:
        command = input("Enter command: (deposit/ withdraw/ passcode/ exit)")
        if command == "deposit":
            amount = float(input("Enter deposit amount: "))
            if amount < 0:
                print("Invalid deposit amount!")
            balance += amount
            print(f"Deposit successful! New balance: {balance}")
            
        elif command == "withdraw":
            amount = float(input("Enter withdraw amount: "))
            if amount > balance:
                print("Insufficient funds!")
            balance -= amount
            print(f"Withdrawal successful! Remaining balance: {balance}")
        
        elif command == "passcode":
            pass
        
        elif command == "exit":
            print(f"Session closed. Have a great day!")
            return balance
        else:
            print("Command not recognized, try again.")


final_status = atm_system("Shaafi", 9876, 10000000.0)
print("Result:", final_status)