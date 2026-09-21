''''
21-09-2026
DAILY HOMEWORK FOR TODAY (Q2)

Practice Problem: Microservice Deployment Validator
Scenario
You are writing a deployment verification script for a Continuous Deployment (CI/CD) pipeline. The script checks a service configuration object before spinning up containers in a production cluster.
Given Starter Code
Copy this starter code directly into your script:
# Deployment Telemetry Data
service_config = {
    "service_name": "auth-service",
    "environment": "production",
    "required_env_vars": ["DB_HOST", "SECRET_KEY"],
    "missing_env_vars": []
}

ssl_certificate = "cert_rsa_2048_valid"
cpu_limit = 0.0          # 0.0 means unassigned
debug_mode = True
is_canary_release = False
Tasks & Instructions
Construct an if-elif-else control flow structure to assign a string to a variable named deploy_status:
Condition 1 (if): Critical Safety Check (Debug Mode in Production)
Check if debug_mode is truthy AND service_config["environment"] == "production".
If true, set deploy_status to "ABORT: Debug mode cannot run in production".
Condition 2 (elif): Missing Environment Variables OR Missing SSL
Check if service_config["missing_env_vars"] is truthy (meaning there are missing variables recorded) OR ssl_certificate is falsy (missing / empty).
If true, set deploy_status to "ABORT: Missing critical credentials or environment variables".
Condition 3 (elif): Unassigned CPU Limits
Check if cpu_limit is falsy (meaning it is zero or not set).
If true, set deploy_status to "HOLD: CPU resources must be defined".
Condition 4 (elif): Canary or Staging Promotion
Check if is_canary_release is truthy OR service_config["environment"] == "staging".
If true, set deploy_status to "PROCEED: Canary or staging deployment started".
Condition 5 (else): Default Full Rollout
Otherwise, set deploy_status to "PROCEED: Standard production rollout".
Output:
Print deploy_status.

'''

# Deployment Telemetry Data
service_config = {
    "service_name": "auth-service",
    "environment": "production",
    "required_env_vars": ["DB_HOST", "SECRET_KEY"],
    "missing_env_vars": []
}

ssl_certificate = "cert_rsa_2048_valid"
cpu_limit = 0.0          # 0.0 means unassigned
debug_mode = True
is_canary_release = False

if debug_mode and service_config["environment"] == "production":
    deploy_status = "ABORT: Debug mode cannot run in production"
elif service_config["missing_env_vars"] or not ssl_certificate:
    deploy_status = "ABORT: Missing critical credentials or environment variables"
elif not cpu_limit:
    deploy_status = "HOLD: CPU resources must be defined"
elif is_canary_release or service_config["environment"] == "staging":
    deploy_status = "PROCEED: Canary or staging deployment started"
else:
    deploy_status = "PROCEED: Standard production rollout"

print(deploy_status)