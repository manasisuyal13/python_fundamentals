'''
# Order Telemetry Data
flagged_ips = ["192.168.1.1", "10.0.0.4"]
user_ip = "10.0.0.4"
payment_method = "credit_card"
cart = ["laptop", "mouse"]
order_total = 1200.0
promo_code = None
is_verified_user = False
Tasks & Instructions
Construct an if-elif-else chain to set a string variable named order_decision:

Condition 1 (if): Fraud / Blacklist Check

Check if user_ip is present in flagged_ips OR payment_method is falsy (e.g., missing/empty string).

If true, set order_decision to "CANCELLED: High Risk Detected".

Condition 2 (elif): Empty Cart Check

Check if cart is falsy (empty).

If true, set order_decision to "REJECTED: Cart is Empty".

Condition 3 (elif): High-Value Unverified User Check

Check if order_total is greater than 1000.0 AND is_verified_user is falsy.

If true, set order_decision to "HOLD: High Value Unverified Account".

Condition 4 (elif): Approved with Promo Bonus

Check if is_verified_user is True AND promo_code is truthy (not None or empty).

If true, set order_decision to "APPROVED: Premium Discount Applied".

Condition 5 (else): Default Approval

Otherwise, set order_decision to "APPROVED: Standard Processing".

Output:

Print order_decision.

'''



# Order Telemetry Data
flagged_ips = ["192.168.1.1", "10.0.0.4"]
user_ip = "10.0.0.4"
payment_method = "credit_card"
cart = ["laptop", "mouse"]
order_total = 1200.0
promo_code = None
is_verified_user = False

if user_ip in flagged_ips or not payment_method:
    order_decision = "Cancelled: High Risk Detected"
elif not cart:
    order_decision = "REJECTED: Cart is Empty"
elif order_total > 1000.0 and not is_verified_user:
    order_decision = "HOLD: High Value Unverified Account"
elif is_verified_user and promo_code:
    order_decision = "APPROVED: Premium Discount Applied"
else:
    order_decision = "APPROVED: Standard Processing"

print(order_decision)