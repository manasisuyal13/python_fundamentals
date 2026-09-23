'''
Practice Problem: Batch Transaction Validator & ClassifierScenarioYou are writing a core transaction filter module for a payment engine. The engine receives a batch of transaction records and must audit each transaction using strict validation rules, logical operators, truthy/falsy checks, and comparison bounds before classifying it.Given Starter CodeCopy this exact starter code directly into your script:Python# Each record: (tx_id, payload_note, amount, is_flagged, authorized_roles)
transactions = [
    ("TX_1001", "subscription renewal", 45.0, False, ["user", "billing"]),
    ("TX_1002", "", 0.0, False, ["user"]),
    ("TX_1003", "refund override", 150.0, True, ["admin"]),
    ("TX_1004", "hardware purchase", 850.0, False, ["user", "vendor"]),
    ("TX_1005", "disputed charge", 300.0, False, ["member"]),
]

processed_summary = {
    "approved": 0,
    "manual_review": 0,
    "rejected": 0,
}
Instructions
Write a Python script that iterates through transactions using a single for loop and applies conditional logic to validate each transaction and update processed_summary:   
Loop Structure:Iterate over transactions using a for loop.   
Inside the loop, unpack each tuple into: tx_id, payload_note, amount, is_flagged, and authorized_roles.   Classification Logic (if / elif / else):
Reject Condition (if):
A transaction must be rejected if is_flagged is truthy, OR if amount is falsy (i.e., zero or empty), OR if payload_note is falsy (empty string).
If met: print f"[{tx_id}] REJECTED: Invalid payload or flagged" and increment processed_summary["rejected"] by 1.

Manual Review Condition (elif):
If not rejected, a transaction requires manual review if amount is greater than or equal to 500.0, OR if "admin" is not in authorized_roles AND "billing" is not in authorized_roles.   If met: print f"[{tx_id}] REVIEW: High value or unverified role" and increment processed_summary["manual_review"] by 1.Approved Condition (else):Otherwise, the transaction passes validation.   Print f"[{tx_id}] APPROVED: Cleared for processing" and increment processed_summary["approved"] by 1.
Final Output:
Outside the for loop, print the final processed_summary dictionary.
'''


transactions = [
    ("TX_1001", "subscription renewal", 45.0, False, ["user", "billing"]),
    ("TX_1002", "", 0.0, False, ["user"]),
    ("TX_1003", "refund override", 150.0, True, ["admin"]),
    ("TX_1004", "hardware purchase", 850.0, False, ["user", "vendor"]),
    ("TX_1005", "disputed charge", 300.0, False, ["member"]),
]

processed_summary = {
    "approved": 0,
    "manual_review": 0,
    "rejected": 0,
}

for tx_id, payload_note, amount, is_flagged, authorized_roles in transactions:

    if is_flagged or not amount or not payload_note:
        print(f"[{tx_id}] REJECTED: Invalid payload or flagged")
        processed_summary["rejected"] += 1

    elif amount >= 500.0 or ("admin" not in authorized_roles and "billing" not in authorized_roles):
        print(f"[{tx_id}] REVIEW: High value or unverified role")
        processed_summary["manual_review"] += 1

    else:
        print(f"[{tx_id}] APPROVED: Cleared for processing")
        processed_summary["approved"] += 1

print(processed_summary)