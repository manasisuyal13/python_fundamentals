'''
Q1 HOMEWORK FOR 23/9/2026
Challenge: Transaction Risk Classifier
You are given:
transactions = [
    ("TX_2001", "login from new device", 0.0, False, ["user"]),
    ("TX_2002", "password reset", 0.0, True, ["user"]),
    ("TX_2003", "invoice payment", 1200.0, False, ["billing", "admin"]),
    ("TX_2004", "", 500.0, False, ["user"]),
    ("TX_2005", "privilege escalation", 50.0, True, ["admin"]),
    ("TX_2006", "subscription renewal", 75.0, False, ["user", "billing"]),
    ("TX_2007", "vendor payout", 2500.0, False, ["vendor"]),
]

processed_summary = {
    "approved": 0,
    "manual_review": 0,
    "rejected": 0,
}
Your task is to process every transaction.
Rules
 1. REJECT
Reject the transaction if any of these are true:
is_flagged is truthy
amount is falsy
payload_note is falsy
Print:
[TX_ID] REJECTED
and increment:
processed_summary["rejected"]

 2. MANUAL REVIEW
If the transaction wasn't rejected, send it for manual review if:
amount >= 1000
OR "admin" is NOT among authorized_roles AND the transaction amount is greater than 100
Print:
[TX_ID] MANUAL REVIEW
and increment the appropriate counter.
 Be careful with operator precedence here. Don't blindly add parentheses without thinking about what the condition actually means.

 3. APPROVED
Anything that survives both previous checks is approved.
Print:
[TX_ID] APPROVED
and increment:
processed_summary["approved"]

 Extra Hard Mode
After processing all transactions, print:
Final Summary:
{'approved': X, 'manual_review': Y, 'rejected': Z}
Then print the transaction IDs of all approved transactions.

'''



transactions = [
    ("TX_2001", "login from new device", 0.0, False, ["user"]),
    ("TX_2002", "password reset", 0.0, True, ["user"]),
    ("TX_2003", "invoice payment", 1200.0, False, ["billing", "admin"]),
    ("TX_2004", "", 500.0, False, ["user"]),
    ("TX_2005", "privilege escalation", 50.0, True, ["admin"]),
    ("TX_2006", "subscription renewal", 75.0, False, ["user", "billing"]),
    ("TX_2007", "vendor payout", 2500.0, False, ["vendor"]),
]

processed_summary = {
    "approved": 0,
    "manual_review": 0,
    "rejected": 0,
}

approved_transaction_ids = []

for tx_id, payload_note, amount, is_flagged, authorized_roles in transactions:

    if is_flagged or not amount or not payload_note:
        print(f"[{tx_id}] REJECTED")
        processed_summary["rejected"] += 1

    elif amount >= 1000 or ("admin" not in authorized_roles and amount > 100):
        print(f"[{tx_id}] MANUAL REVIEW")
        processed_summary["manual_review"] += 1

    else:
        print(f"[{tx_id}] APPROVED")
        processed_summary["approved"] += 1
        approved_transaction_ids.append(tx_id)

print("Final Summary:")
print(processed_summary)

print("Approved Transaction IDs:")
print(approved_transaction_ids)