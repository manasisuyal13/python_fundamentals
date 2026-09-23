'''Practice Problem: Email Notification Filtering System
Scenario
You are building an automated notification system for a platform. You have a list of user message dictionaries. You need to loop through all messages and categorize them into different email notification lists based on priority, subject availability, and spam flags.

Given Starter Code
Copy this starter code directly into your script:

Python
# List of Incoming User Messages
messages = [
    {"user": "Alice", "subject": "Urgent: Payment Failed", "is_spam": False},
    {"user": "Bob", "subject": "", "is_spam": False},  # Empty subject string
    {"user": "Charlie", "subject": "Win $1000 NOW!", "is_spam": True},
    {"user": "Diana", "subject": "Weekly Newsletter", "is_spam": False}
]

# Output Buckets
high_priority_emails = []
standard_emails = []
review_folder = []
Tasks & Instructions
Write a for loop that iterates through each msg dictionary inside messages. Inside the loop, construct an if-elif-else control flow structure:

Condition 1 (if): Spam Check

Check if msg["is_spam"] is truthy (True).

If true, append msg["user"] to the review_folder list.

Condition 2 (elif): Missing Subject Check

Check if msg["subject"] is falsy (empty string "").

If true, append msg["user"] to the review_folder list as well.

Condition 3 (elif): Urgent Priority Check

Check if "Urgent" is inside msg["subject"].

If true, append msg["user"] to the high_priority_emails list.

Condition 4 (else): Standard Email

Otherwise, append msg["user"] to the standard_emails list.

Output:

Outside the loop, print all three output lists (high_priority_emails, standard_emails, review_folder).

'''

# List of Incoming User Messages
messages = [
    {"user": "Alice", "subject": "Urgent: Payment Failed", "is_spam": False},
    {"user": "Bob", "subject": "", "is_spam": False},
    {"user": "Charlie", "subject": "Win $1000 NOW!", "is_spam": True},
    {"user": "Diana", "subject": "Weekly Newsletter", "is_spam": False}
]

high_priority_emails = []
standard_emails = []
review_folder = []

for msg in messages:

    if msg["is_spam"]:
        review_folder.append(msg["user"])

    elif not msg["subject"]:
        review_folder.append(msg["user"])

    elif "Urgent" in msg["subject"]:
        high_priority_emails.append(msg["user"])

    else:
        standard_emails.append(msg["user"])

print("High priority emails:", high_priority_emails)
print("Standard emails:", standard_emails)
print("Review folder:", review_folder)