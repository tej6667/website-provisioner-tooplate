def create_security_group(ec2_client, template_name, my_ip):
    security_group_name = f"{template_name}-sg"
    description = f"Security group for {template_name}"

    # Create the security group
    response = ec2_client.create_security_group(
        GroupName=security_group_name,
        Description=description
    )
    security_group_id = response['GroupId']

    # Allow SSH access from my IP
    ec2_client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': f"{my_ip}/32"}]
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            }
        ]
    )

    return security_group_id