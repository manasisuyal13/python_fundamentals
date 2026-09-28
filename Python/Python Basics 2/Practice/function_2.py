'''
🎯 The Challenge: Pin Verification & Balance System
Write a Python function named bank_transaction that takes two parameters:

correct_pin (a string, e.g., "4321")

balance (an integer or float, e.g., 500)

Inside the function:

Allow the user up to 3 attempts to enter their PIN using input("Enter PIN: ").

If the user enters the wrong PIN:

Print "Incorrect PIN!".

Deduct 1 attempt.

If attempts reach 0, print "Card Blocked!" and return 0 immediately.

If the user enters the correct PIN, print "Access Granted!" and enter a second while loop for transactions with the following command options:

"check": Print the current balance and use continue to ask for the next command.

"withdraw": Prompt for an amount using input("Enter amount to withdraw: ") (convert to integer/float).

If the amount is less than or equal to balance, deduct it from balance and print "Withdrawal successful!".

If the amount is greater than balance, print "Insufficient funds!".

"exit": Print "Thank you for banking with us." and return balance (exiting the function with the final remaining balance).

Any other command: Use pass or print "Invalid command" to prompt again.

💡 Example Function Call to Test:
Python
final_balance = bank_transaction("4321", 500)
print(f"Final Account Balance: {final_balance}")


'''

def bank_transaction(correct_pin, balance):
    attempt = 3
    
    while attempt > 0:
        pin = input("Enter PIN: ")
        if pin == correct_pin:
            print("Access Granted!")
            break
        else:
            print("Incorrect PIN!")
            attempt -= 1  
            if attempt == 0:
                print("Card Blocked!")
                return 0
        
    while True:
        command = input("Enter command: (check/withdraw/exit)")

        if command == "check":
            print(f"Current balance: {balance}")
            continue

        elif command == "withdraw":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= balance:
                balance -= amount
                print("Withdrawal successful!")
            else:
                print("Insufficient funds!")
        elif command == "exit":
            print("Thank you for banking with us!")
            return balance
        else:
            print("Invalid command")
            
final_balance = bank_transaction("4321", 500000)
print(f"Final Account Balance: {final_balance}")