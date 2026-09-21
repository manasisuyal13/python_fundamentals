''''
21-09-2026
DAILY HOMEWORK FOR TODAY (Q1)
 Practice Problem: Automated Database Query & Cache Router
Scenario
You are developing a database router that decides how to fulfill a data request. The router determines whether to serve data directly from a Cache, query a Replica DB, query the Primary DB, or Deny Access based on system load, authentication, and request parameters.
Given Starter Code
Copy this starter code directly into your script:
# Database Request Telemetry Data
auth_context = {
    "user_id": 1042,
    "permissions": ["read_data"],
    "is_banned": False
}
cache_data = {}               # Empty dictionary (falsy)
query_payload = "SELECT * FROM orders;"
server_maintenance = False
database_load = 88.5          # Float (load percentage)
Tasks & Instructions
Construct an if-elif-else control flow structure to assign a string to a variable named routing_decision:
Condition 1 (if): Banned User OR Server Maintenance
Check if auth_context["is_banned"] is truthy (True) OR server_maintenance is truthy (True).
If true, set routing_decision to "SERVICE UNAVAILABLE: Request Rejected".
Condition 2 (elif): Invalid Permissions OR Empty Query
Check if "read_data" is missing from auth_context["permissions"] OR query_payload is falsy (empty string).
If true, set routing_decision to "BAD REQUEST: Missing Permission or Empty Query".
Condition 3 (elif): Cache Hit Check
Check if cache_data is truthy (meaning the dictionary contains cached data) AND database_load is greater than or equal to 80.0.
If true, set routing_decision to "SERVE FROM CACHE: High Load Mitigation".
Condition 4 (elif): High Load Replica Routing
Check if database_load is greater than or equal to 80.0 AND cache_data is falsy (cache is empty).
If true, set routing_decision to "ROUTE TO REPLICA: High Load Fallback".
Condition 5 (else): Primary DB Default
Otherwise, set routing_decision to "ROUTE TO PRIMARY: Normal Execution".
Output:
Print routing_decision.

'''

# Database Request Telemetry Data
auth_context = {
    "user_id": 1042,
    "permissions": ["read_data"],
    "is_banned": False
}
cache_data = {}               # Empty dictionary (falsy)
query_payload = "SELECT * FROM orders;"
server_maintenance = False
database_load = 88.5          # Float (load percentage)

if auth_context["is_banned"] or server_maintenance:
    routing_decision = "SERVICE UNAVAILABLE: Rejected"
elif "read_data" not in auth_context["permissions"] or not query_payload:
    routing_decision = "BAD REQUEST: Missing Permission or Empty Query"
elif not cache_data and database_load >= 80:
    routing_decision = "SERVE FROM CACHE: High Load Mitigation"
elif database_load >=80 and not cache_data:
    routing_decision = "ROUTE TO REPLICA: High Load Fallback"
else:
    routing_decision = "ROUTE TO PRIMARY: Normal Execution"

print(routing_decision)
    