import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def create_key_pair(key_name):
    """
    Create a new EC2 key pair.

    Parameters:
    key_name (str): The name of the key pair to create.

    Returns:
    str: The private key material for the key pair.
    """
    ec2_client = boto3.client('ec2')

    try:
        response = ec2_client.create_key_pair(KeyName=key_name)
        logging.info(f"Key pair '{key_name}' created successfully.")
        return response['KeyMaterial']
    except Exception as e:
        logging.error(f"Error creating key pair: {e}")
        raise

# Example usage (uncomment to use):
# key_material = create_key_pair('my_key_pair_name')