def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def load_config(file_path):
    """Loads configuration from a specified file."""
    import json
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

def validate_ip(ip_address):
    """Validates the format of an IP address."""
    import re
    pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    return re.match(pattern, ip_address) is not None

def get_ami_id(region):
    """Returns the AMI ID for Amazon Linux 2023 based on the region."""
    ami_map = {
        'us-east-1': 'ami-0abcdef1234567890',
        'us-west-2': 'ami-0abcdef1234567890',
        # Add other regions as necessary
    }
    return ami_map.get(region, None)