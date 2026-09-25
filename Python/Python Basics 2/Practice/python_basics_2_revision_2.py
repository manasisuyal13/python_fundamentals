'''

Home Work - 25-09-2026 
# Raw microservice logs across clusters
# Format: (service_name, cluster_id, error_count, response_times_ms, auth_data, is_under_maintenance)
microservice_logs = [
    ("auth-service", "cluster_alpha", 0, [45.0, 52.1, 48.0], {"token": "valid_rsa_key", "roles": ["admin"]}, False),
    ("payment-service", "cluster_beta", 12, [120.0, 850.0, 990.0], {"token": "", "roles": ["billing"]}, False),
    ("user-service", "cluster_alpha", 0, [], {"token": "valid_key", "roles": ["user"]}, False),
    ("log-service", "cluster_gamma", 5, [15.2, 18.0], {}, True),
    ("data-pipeline", "cluster_beta", 0, [320.0, 410.0, 290.0], {"token": "valid_key", "roles": ["data_admin"]}, False),
    ("inventory-service", "cluster_alpha", 2, [50.0, 60.0], {"token": "valid_key", "roles": []}, False),
    ("notification-service", "cluster_gamma", 0, [88.0, 92.0], {"token": "valid_key", "roles": ["admin", "notify"]}, False)
]

# Operational Action Queues
quarantine_queue = []
performance_alert_queue = []
normal_operations = []


'''

# Raw microservice logs across clusters
# Format: (service_name, cluster_id, error_count, response_times_ms, auth_data, is_under_maintenance)
microservice_logs = [
    ("auth-service", "cluster_alpha", 0, [45.0, 52.1, 48.0], {"token": "valid_rsa_key", "roles": ["admin"]}, False),
    ("payment-service", "cluster_beta", 12, [120.0, 850.0, 990.0], {"token": "", "roles": ["billing"]}, False),
    ("user-service", "cluster_alpha", 0, [], {"token": "valid_key", "roles": ["user"]}, False),
    ("log-service", "cluster_gamma", 5, [15.2, 18.0], {}, True),
    ("data-pipeline", "cluster_beta", 0, [320.0, 410.0, 290.0], {"token": "valid_key", "roles": ["data_admin"]}, False),
    ("inventory-service", "cluster_alpha", 2, [50.0, 60.0], {"token": "valid_key", "roles": []}, False),
    ("notification-service", "cluster_gamma", 0, [88.0, 92.0], {"token": "valid_key", "roles": ["admin", "notify"]}, False)
]

# Operational Action Queues
quarantine_queue = []
performance_alert_queue = []
normal_operations = []

for log_idx, (service_name, cluster_id, error_count, response_times_ms, auth_data, is_under_maintenance) in enumerate(microservice_logs):
    total_response_time = 0.0

    for i in range(len(response_times_ms)):
        total_response_time += response_times_ms[i]

    if response_times_ms:
        avg_response_time = total_response_time / len(response_times_ms)
    else:
        avg_response_time = 0.0

    if is_under_maintenance or not auth_data or not auth_data.get("token") or not auth_data.get("roles") or error_count > 10:
        quarantine_queue.append(f"Log {log_idx} [{service_name}]: Quarantined")
    elif (cluster_id == "cluster_alpha" or cluster_id == "cluster_beta") and (not response_times_ms or avg_response_time > 300.0) and "admin" not in auth_data.get("roles", []):
        performance_alert_queue.append(f"Log {log_idx} [{service_name}]: Performance Alert")
    else:
        normal_operations.append(f"Log {log_idx} [{service_name}]: Operational")

print("Quarantine Queue:", quarantine_queue)
print("Performance Alert Queue:", performance_alert_queue)
print("Normal Operations:", normal_operations)