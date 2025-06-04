import boto3
import time
from utils import get_my_ip

def create_ec2_instance(key_name, security_group_id):
    """
    Create an EC2 instance with Amazon Linux 2023 AMI, t2.micro instance type,
    specified key pair, and security group. It also sets up a user data script
    to install a website from tooplate.com.

    Parameters:
    key_name (str): The name of the key pair to use for the instance.
    security_group_id (str): The ID of the security group to associate with the instance.

    Returns:
    str: The public DNS of the created EC2 instance.
    """
    ec2 = boto3.resource('ec2')

    # Amazon Linux 2023 AMI ID (replace with the correct ID for your region)
    ami_id = 'ami-0abcdef1234567890'  # Example AMI ID, update as necessary
    instance_type = 't2.micro'

    # User data script to set up the website
    user_data_script = """#!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo '<h1>Welcome to the Tooplate Website</h1>' > /var/www/html/index.html
    """

    # Create the EC2 instance
    instance = ec2.create_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        UserData=user_data_script,
        MinCount=1,
        MaxCount=1
    )[0]

    # Wait for the instance to be in running state
    instance.wait_until_running()

    # Reload the instance attributes
    instance.reload()

    return instance.public_dns_name

# Example usage (to be called from another module):
# my_ip = get_my_ip()
# key_name = 'your_key_pair_name'
# security_group_id = 'your_security_group_id'
# dns = create_ec2_instance(key_name, security_group_id)
# print(f'EC2 Instance DNS: {dns}')