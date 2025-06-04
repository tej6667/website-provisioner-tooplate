def create_security_group(ec2_client, template_name, my_ip):
    """
    Create a security group with specified rules.

    Parameters:
    ec2_client (boto3.client): The Boto3 EC2 client.
    template_name (str): The name of the template used for naming the security group.
    my_ip (str): The IP address to allow for SSH access.

    Returns:
    str: The ID of the created security group.
    """
    security_group_name = f"{template_name}SecurityGroup"
    
    # Create the security group
    response = ec2_client.create_security_group(
        GroupName=security_group_name,
        Description='Security group for EC2 instance with SSH and HTTP access'
    )
    
    security_group_id = response['GroupId']
    
    # Add rules to the security group
    ec2_client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': f"{my_ip}/32"}]  # Allow SSH from MY_IP
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Allow HTTP from anywhere
            }
        ]
    )
    
    return security_group_id