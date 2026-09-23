'''

Q2 HOMEWORK FOR 23/9/2026
Homework Challenge: Multi-Tenant Cloud Security & Resource Audit Engine
Scenario
You are developing an automated security and resource audit engine for an enterprise cloud platform. You receive a batch of server logs representing different cloud workloads. Each server log contains a server ID, a list of active network ports, security alerts, and resource telemetry.
Your task is to loop through the servers, evaluate their security posture using strict business rules, and route each server ID into the correct operational queue.
Given Starter Code
Copy this starter code directly into your Python file:
# Raw Server Logs (List of Nested Dictionaries)
server_logs = [
    {
        "server_id": "srv_alpha",
        "open_ports": [80, 443],
        "alerts": ["DDoS_ATTACK", "PORT_SCAN"],
        "is_quarantined": False,
        "backup_server": "srv_alpha_bak"
    },
    {
        "server_id": "srv_beta",
        "open_ports": [],                     # Empty list (falsy)
        "alerts": [],                         # Empty list (falsy)
        "is_quarantined": False,
        "backup_server": None                 # None (falsy)
    },
    {
        "server_id": "srv_gamma",
        "open_ports": [22, 80, 8080],
        "alerts": ["CRITICAL_EXPLOIT"],
        "is_quarantined": True,               # Quarantined flag set
        "backup_server": "srv_gamma_bak"
    },
    {
        "server_id": "srv_delta",
        "open_ports": [21, 22, 443],
        "alerts": [],
        "is_quarantined": False,
        "backup_server": "srv_delta_bak"
    },
    {
        "server_id": "srv_epsilon",
        "open_ports": [80],
        "alerts": ["HIGH_LATENCY"],
        "is_quarantined": False,
        "backup_server": ""                   # Empty string (falsy)
    }
]

# Destination Operational Queues
immediate_shutdown = []
maintenance_queue = []
decommission_queue = []
active_monitoring = []

Tasks & Instructions
Write a for loop that iterates through every server dictionary in server_logs. Inside the loop, construct an if-elif-else control flow structure according to the following priorities:
Condition 1 (if): Critical Security Lockdown
Check if server["is_quarantined"] is truthy (True) OR server["alerts"] contains "CRITICAL_EXPLOIT".
If true, append server["server_id"] to the immediate_shutdown list.
Condition 2 (elif): Decommission Inactive Server
Check if server["open_ports"] is falsy (empty list) AND server["backup_server"] is falsy (None or empty string "").
If true, append server["server_id"] to the decommission_queue list.
Condition 3 (elif): Port Security & Maintenance Check
Check if port 22 is inside server["open_ports"] OR server["alerts"] is truthy (contains any alerts).
If true, append server["server_id"] to the maintenance_queue list.
Condition 4 (else): Healthy Server Default
Otherwise, append server["server_id"] to the active_monitoring list.
Output:
Outside the for loop, print all four operational queue lists (immediate_shutdown, decommission_queue, maintenance_queue, active_monitoring).


'''


server_logs = [
    {
        "server_id": "srv_alpha",
        "open_ports": [80, 443],
        "alerts": ["DDoS_ATTACK", "PORT_SCAN"],
        "is_quarantined": False,
        "backup_server": "srv_alpha_bak"
    },
    {
        "server_id": "srv_beta",
        "open_ports": [],
        "alerts": [],
        "is_quarantined": False,
        "backup_server": None
    },
    {
        "server_id": "srv_gamma",
        "open_ports": [22, 80, 8080],
        "alerts": ["CRITICAL_EXPLOIT"],
        "is_quarantined": True,
        "backup_server": "srv_gamma_bak"
    },
    {
        "server_id": "srv_delta",
        "open_ports": [21, 22, 443],
        "alerts": [],
        "is_quarantined": False,
        "backup_server": "srv_delta_bak"
    },
    {
        "server_id": "srv_epsilon",
        "open_ports": [80],
        "alerts": ["HIGH_LATENCY"],
        "is_quarantined": False,
        "backup_server": ""
    }
]

immediate_shutdown = []
maintenance_queue = []
decommission_queue = []
active_monitoring = []

for server in server_logs:
    if server["is_quarantined"] or "CRITICAL_EXPLOIT" in server["alerts"]:
        immediate_shutdown.append(server["server_id"])

    elif not server["open_ports"] and not server["backup_server"]:
        decommission_queue.append(server["server_id"])

    elif 22 in server["open_ports"] or server["alerts"]:
        maintenance_queue.append(server["server_id"])

    else:
        active_monitoring.append(server["server_id"])

print(immediate_shutdown)
print(decommission_queue)
print(maintenance_queue)
print(active_monitoring)