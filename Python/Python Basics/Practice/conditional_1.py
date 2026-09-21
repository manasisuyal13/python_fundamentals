'''
Scenario
You are writing a backend verification script that checks whether a user can access a premium feature based on their account details and role profile.

Given Starter Code
Copy this starter code directly into your Python file:

Python
# User Profile Telemetry Data
username = "  alex_dev  "
account_balance = 0.0
roles = ["editor"]
banned_users = []
session_token = None
Tasks & Instructions
Data Preparation:

Clean username by removing leading and trailing whitespace using .strip() and store it back in username.

Conditional Logic & Truthy / Falsy Checks:
Construct an if-elif-else control flow structure to assign a string to a variable named access_status:

Condition 1 (if): Check for Banned Users

Use the truthy/falsy nature of the banned_users list to check if there are any banned users AND check if username is present in banned_users.

If true, set access_status to "ACCESS DENIED: Account Banned".

Condition 2 (elif): Active Session Verification

Check if session_token evaluates to falsy.

If it is falsy, set access_status to "ACCESS DENIED: Invalid Session".

Condition 3 (elif): Role & Balance Authorization

Check if "admin" is inside roles OR ("editor" is inside roles AND account_balance is truthy).

If true, set access_status to "ACCESS GRANTED: Premium Access".

Condition 4 (else): Default Fallback

If none of the conditions above are met, set access_status to "ACCESS DENIED: Insufficient Privileges".

Output:

Print access_status.

'''


# User Profile Telemetry Data
username = "  alex_dev  "
account_balance = 0.0
roles = ["editor"]
banned_users = []
session_token = None
access_status = ""

username = username.strip()
#print(username)

if banned_users and username in banned_users:
    access_status = "ACCESS DENIED: Account Banned"
elif not session_token:
    access_status = "ACCESS DENIED: Invalid Session"
elif "admin" in roles or ("editor" in roles and account_balance):
    access_status = "ACCESS GRANTED: Premium Access"
else:
    access_status = "ACCESS DENIED: Insufficient Privileges"
    
print(access_status)
    