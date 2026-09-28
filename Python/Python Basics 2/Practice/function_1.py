'''🎯 The Challenge: Smart Command Processor
Write a Python function named process_commands that takes one parameter: max_attempts (which will be an integer representing how many invalid inputs are allowed).

Inside the function:

Maintain a count of invalid attempts made by the user.

Use a while loop to continuously prompt the user with:

input("Enter command: ")

Handle the following command inputs (case-sensitive):

"skip":

Do nothing or skip the rest of the loop body using continue. (Do not count this as an invalid attempt).

"todo":

Use pass as a temporary placeholder for future functionality. (Do not count this as an invalid attempt).

"exit":

Print "Exiting processor." and stop the loop using break.

Any other input (e.g., "hello", "run"):

Treat it as an invalid command.

Increase the invalid attempts counter by 1.

Print "Invalid command! Invalid attempts: X/max_attempts" (where X is the current invalid attempt count).

If the invalid attempts reach max_attempts, print "Too many invalid commands. System locked." and break out of the loop.

💡 Example Function Call to Test Your Code:
Python
# Call your function with a limit of 3 invalid attempts
process_commands(3)
'''

def process_commands(max_attempts):
    invalid_attempts = 0
    while True:
        command = input("Enter command:- ")
        
        if command == "skip":
            continue
        
        elif command == "todo":
            pass
        
        elif command == "exit":
            print("Exiting processor")
            break
        
        else:
            invalid_attempts += 1
            print(f"Invalid command! Invalid attempts: {invalid_attempts}/{max_attempts}")
            
            if (invalid_attempts >= max_attempts):
                print("Too many invalid commands. System locked")
                break
            
process_commands(3)
            