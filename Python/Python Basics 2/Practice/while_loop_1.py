'''
Write a Python program that continuously asks the user to enter a password using input().

If the user types python123, print "Access Granted!" and exit the loop using break.

If the user types anything else, print "Incorrect password, try again." and let the loop continue asking.

'''

while True:
    password = input("Enter the password:")
    if password == "python123":
        print("Access Granted!")
        break
    else:
        print("Incorrect password, try again.")