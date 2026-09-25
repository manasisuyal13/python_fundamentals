'''

===============================================================================
PROBLEM TITLE: Enterprise User Access & Subscription Telemetry Auditor
===============================================================================

SCENARIO:
You are developing an automated security auditor for an enterprise SaaS platform.
You are given a list of raw user telemetry logs. Each user record is represented 
as a tuple: (user_id, account_tier, activity_score, permissions_list, is_flagged)

YOUR GOAL:
Iterate over the user logs using a for loop with enumerate() to track indices.
Construct conditional logic (if / elif / else) combining comparison operators, 
logical operators (and / or / not), and truthy/falsy evaluations to categorize 
and route each user ID into one of three audit lists:

1. 'flagged_accounts':
   - Route here if 'is_flagged' is truthy
   - OR if 'activity_score' is falsy (e.g., 0 or 0.0)
   - OR if 'permissions_list' is falsy (an empty list)

2. 'vip_access_queue':
   - Route here if the account wasn't flagged AND:
     * 'account_tier' is equal to "enterprise" OR "premium"
     * AND 'activity_score' is greater than or equal to 75.0
     * AND "admin" is inside 'permissions_list'

3. 'standard_audit_queue':
   - Route all remaining unflagged accounts here.

When appending to any of the three queues, format the string as:
f"Index {i}: {user_id}"

===============================================================================
INPUT DATA
===============================================================================
"""

users_telemetry = [
    ("usr_101", "enterprise", 85.0, ["read", "write", "admin"], False),
    ("usr_102", "free", 0.0, ["read"], False),                         # Falsy activity score
    ("usr_103", "premium", 90.0, ["read", "write"], True),             # Flagged user
    ("usr_104", "premium", 78.5, ["read", "admin"], False),            # VIP Queue
    ("usr_105", "standard", 45.0, ["read"], False),                    # Standard Queue
    ("usr_106", "enterprise", 60.0, [], False),                        # Falsy permissions list
    ("usr_107", "enterprise", 95.0, ["read", "write", "admin"], False) # VIP Queue
]

# 1. Initialize destination lists
flagged_accounts = []
vip_access_queue = []
standard_audit_queue = []

# ===============================================================================
# WRITE YOUR CODE BELOW THIS LINE
# ===============================================================================

# Step 2: Loop through users_telemetry using enumerate() to get index 'i' and tuple 'user'
for i, user in enumerate(users_telemetry):
    # Step 3: Unpack the tuple into individual variables
    user_id, account_tier, activity_score, permissions_list, is_flagged = user

    # Step 4: Construct conditional logic using truthy/falsy checks and operators
    if is_flagged or not activity_score or not permissions_list:
        flagged_accounts.append(f"Index {i}: {user_id}")
    elif (account_tier == "enterprise" or account_tier == "premium") and activity_score >= 75.0 and "admin" in permissions_list:
        vip_access_queue.append(f"Index {i}: {user_id}")
    else:
        standard_audit_queue.append(f"Index {i}: {user_id}")

# Step 5: Print final results
print("Flagged Accounts:", flagged_accounts)
print("VIP Access Queue:", vip_access_queue)
print("Standard Audit Queue:", standard_audit_queue)
```eof

### Key Concepts Covered:
1. **For Loops & Iterables**: Iterating through the `users_telemetry` sequence.
2. **`enumerate()`**: Tracking zero-based index `i` along with each item.
3. **Tuple Unpacking**: Unpacking each tuple directly into descriptive variables.
4. **Truthy / Falsy Checks**: Evaluating `not activity_score` (checking for `0.0`) and `not permissions_list` (checking for empty `[]`).
5. **Logical & Comparison Operators**: Combining `or`, `and`, `in`, `==`, and `>=`.
6. **Conditional Logic**: Structuring priority evaluation with `if`, `elif`, and `else`.

Give this problem a try! Write out your implementation in your environment or editor to practice these Python Basics II concepts.

'''
users_telemetry = [
    ("usr_101", "enterprise", 85.0, ["read", "write", "admin"], False),
    ("usr_102", "free", 0.0, ["read"], False),
    ("usr_103", "premium", 90.0, ["read", "write"], True),
    ("usr_104", "premium", 78.5, ["read", "admin"], False),
    ("usr_105", "standard", 45.0, ["read"], False),
    ("usr_106", "enterprise", 60.0, [], False),
    ("usr_107", "enterprise", 95.0, ["read", "write", "admin"], False)
]

flagged_accounts = []
vip_access_queue = []
standard_audit_queue = []

for i, (user_id, account_tier, activity_score, permissions_list, is_flagged) in enumerate(users_telemetry):
    if is_flagged or not activity_score or not permissions_list:
        flagged_accounts.append(f"Index {i}: {user_id}")
    elif (account_tier == "enterprise" or account_tier == "premium") and activity_score >= 75.0 and "admin" in permissions_list:
        vip_access_queue.append(f"Index {i}: {user_id}")
    else:
        standard_audit_queue.append(f"Index {i}: {user_id}")
        
print("Flagged Accounts:", flagged_accounts)
print("VIP Access Queue:", vip_access_queue)
print("Standard Audit Queue:", standard_audit_queue)