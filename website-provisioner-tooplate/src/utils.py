def log_message(message):
    print(f"[INFO] {message}")

def log_error(message):
    print(f"[ERROR] {message}")

def validate_ip(ip_address):
    import re
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(pattern, ip_address) is not None

def get_current_ip():
    import requests
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except Exception as e:
        log_error(f"Failed to get current IP: {e}")
        return None