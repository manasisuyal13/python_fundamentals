'''
Scenario
You are building an API gateway for an enterprise cloud platform. Every incoming request carries a user context, payload metadata, and system flags. You need to determine whether to Allow, Throttle, or Block the incoming request.

Given Starter Code
Copy this starter code directly into your script:

Python
# API Request Telemetry Data
request_headers = {
    "api_key": "key_789xyz",
    "user_agent": "Mozilla/5.0"
}
user_profile = {
    "username": "coder_pro",
    "roles": ["developer"],
    "suspended_flags": []
}
request_payload = ""           # Empty string
rate_limit_exceeded = False
is_internal_network = False
Tasks & Instructions
Construct an if-elif-else control flow structure to assign a string to a variable named gateway_action:

Condition 1 (if): Suspended User OR Rate Limit Exceeded

Check if user_profile["suspended_flags"] is truthy (i.e., contains any suspension flags) OR rate_limit_exceeded is truthy.

If true, set gateway_action to "BLOCK: Account Suspended or Rate Limit Exceeded".

Condition 2 (elif): Missing API Key or Missing User Agent

Check if "api_key" is missing from request_headers (or its value is falsy) OR "user_agent" is falsy / missing.

Hint: Use .get("key_name") or not request_headers.get("key_name") for safe dictionary checks!

If true, set gateway_action to "BLOCK: Invalid Request Headers".

Condition 3 (elif): Admin Access OR Internal Network Exemption

Check if "admin" is inside user_profile["roles"] OR is_internal_network is truthy.

If true, set gateway_action to "ALLOW: Full Privileged Access".

Condition 4 (elif): Developer Access with Valid Payload

Check if "developer" is inside user_profile["roles"] AND request_payload is falsy (meaning the payload is empty).

If true, set gateway_action to "REJECT: Empty Request Payload".

Condition 5 (else): Default Fallback

Otherwise, set gateway_action to "ALLOW: Standard Request Processing".

Output:

Print gateway_action.

💡 Keys to Keep in Mind:
Dictionary .get(): request_headers.get("api_key") safely checks a dictionary key without crashing if the key is missing.

Falsy Check: not request_payload checks if the string is empty "".

Truthy Check: if user_profile["suspended_flags"]: checks if the list has elements inside it.n


'''



# API Request Telemetry Data
request_headers = {
    "api_key": "key_789xyz",
    "user_agent": "Mozilla/5.0"
}
user_profile = {
    "username": "coder_pro",
    "roles": ["developer"],
    "suspended_flags": []
}
request_payload = ""           # Empty string
rate_limit_exceeded = False
is_internal_network = False

if user_profile["suspended_flags"] or rate_limit_exceeded:
    gateway_action = "BLOCK: Account Suspended or Rate Limit Exceeded"
elif not request_headers.get("api_key") or not request_headers.get("user_agent"):
    gateway_action = "BLOCK: Invalid Request Headers"
elif "admin" in user_profile["roles"] or is_internal_network:
    gateway_action = "ALLOW: Full Privileged Access"
elif "developer" in user_profile["roles"] and not request_payload:
    gateway_action = "REJECT: Empty Request Payload"
else:
    gateway_action = "ALLOW: Standard Request Processing"

print(gateway_action)
