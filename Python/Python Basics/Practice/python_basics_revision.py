# --- RAW DATA INPUTS ---

# Task 1. Raw Telemetry Log String
telemetry_log = "  LOG_ID:9876543210_KEY:X9A8B7C6D5_METRIC:0048.50_QTY:004  "


clean_log = telemetry_log.replace(" ","")
#print(clean_log) # Output: LOG_ID:9876543210_KEY:X9A8B7C6D5_METRIC:0048.50_QTY:004

key_code = clean_log[21:31]
key_code = key_code[::-1]

metric_str = clean_log[-15:-8]
#print(metric_str)
metric_val = float(metric_str)

qty_str = clean_log[-3:]
qty_val = int(qty_str)

#c
subtotal = metric_val * qty_val
#print(subtotal)

#d
discount = subtotal % 10
subtotal -=discount
final_metric_total = subtotal
#print(final_metric_total)

# Task 3. Multidimensional Matrix (Sensor Readings)
sensor_matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]             

center_element = sensor_matrix[1][1]
#print(center_element) # 50
bottom_right_element = sensor_matrix[2][2]
#print(bottom_right_element)

matrix_score = center_element + bottom_right_element * 2 ** 2//4 - abs(-15)
#print(matrix_score)

# Task 3. Access Permission Sets
network_permissions = ["read", "write", "execute", "firewall", "write", "audit"]
cloud_permissions = ["write", "deploy", "firewall", "backup", "deploy"]
ir_permissions = ["monitor", "isolate", "dump_memory", "read"]

net_set = set(network_permissions)
cloud_set = set(cloud_permissions)
ir_set = set(ir_permissions)

net_set.add("sudo")
#print(net_set)

net_backup = net_set.copy()
net_backup.clear()

shared_access = net_set.intersection(cloud_set)
exclusive_net =  net_set.difference(cloud_set)
net_set.difference_update(ir_set)

is_separated = cloud_set.isdisjoint(ir_set)
#print(is_separated)

is_super = net_set.issuperset({"write", "sudo"})

# Task 4. Incoming User Session Log (Tuples: user_id, session_hours, role)
session_log = [
    ("usr_101", 2.5, "admin"),
    ("usr_102", 4.0, "member"),
    ("usr_101", 1.5, "admin"),
    ("usr_103", 3.0, "member"),
    ("usr_102", 1.0, "member")
]
#empty dictionary
user_summary = {}

#accessing tuples

#session 1
user_id, hours, role = session_log[0]
user_summary[user_id] = { 
                         "hours" : hours,
                         "role" : role
                         }
#print(user_summary)

#session 2
user_id, hours, role = session_log[1]
user_summary[user_id] = { 
                         "hours" : hours,
                         "role" : role
                         }
#print(user_summary)

#session 3
user_id, hours, role = session_log[2]
user_summary[user_id]["hours"] += hours
#print(user_summary)

#session 4
user_id, hours, role = session_log[3]
user_summary[user_id] = { 
                         "hours" : hours,
                         "role" : role
                         }
#print(user_summary)

#session 5
user_id, hours, role = session_log[4]
user_summary[user_id]["hours"] += hours
#print(user_summary)

usr_101_info = user_summary.get("usr_101")
#print(usr_101_info)

usr_101_hours = usr_101_info.get("hours")
#print(usr_101_hours)

# Task 5
final_metric_total = f"=== DATA ENGINE AUDIT REPORT === \n Login Metrics: \n -Reversed Key: {key_code} \n - Final Metric Total: ${final_metric_total} \n Matrix Precedence Score: {matrix_score} \n \n Security Audit: \n Shared Access: {shared_access} \n - Exclusive Network Permissions: {exclusive_net} \n - Disjoint Operations: {is_separated} | Super Admin: {is_super} \n \n User Summary: \n - User 101 Total Hours: {usr_101_hours}"
print(final_metric_total)