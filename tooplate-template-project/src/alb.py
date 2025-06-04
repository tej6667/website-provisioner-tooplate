import boto3
from botocore.exceptions import ClientError

def create_alb(alb_name, vpc_id, security_group_id, target_group_name, instance_id):
    """
    Create an Application Load Balancer (ALB) and add the specified EC2 instance to its target group.

    Parameters:
    alb_name (str): The name of the ALB to be created.
    vpc_id (str): The VPC ID where the ALB will be created.
    security_group_id (str): The security group ID for the ALB.
    target_group_name (str): The name of the target group for the ALB.
    instance_id (str): The ID of the EC2 instance to be added to the target group.

    Returns:
    str: The DNS name of the created ALB.
    """
    client = boto3.client('elbv2')

    # Create the target group
    try:
        target_group_response = client.create_target_group(
            Name=target_group_name,
            Protocol='HTTP',
            Port=80,
            VpcId=vpc_id,
            HealthCheckProtocol='HTTP',
            HealthCheckPort='80',
            HealthCheckPath='/',
            HealthCheckIntervalSeconds=30,
            HealthCheckTimeoutSeconds=5,
            HealthyThresholdCount=5,
            UnhealthyThresholdCount=2
        )
        target_group_arn = target_group_response['TargetGroups'][0]['TargetGroupArn']
    except ClientError as e:
        print(f"Error creating target group: {e}")
        return None

    # Register the EC2 instance with the target group
    try:
        client.register_targets(
            TargetGroupArn=target_group_arn,
            Targets=[{'Id': instance_id}]
        )
    except ClientError as e:
        print(f"Error registering targets: {e}")
        return None

    # Create the ALB
    try:
        alb_response = client.create_load_balancer(
            Name=alb_name,
            Subnets=[vpc_id],  # Replace with actual subnet IDs
            SecurityGroups=[security_group_id],
            Scheme='internet-facing',
            Tags=[{'Key': 'Name', 'Value': alb_name}]
        )
        alb_arn = alb_response['LoadBalancers'][0]['LoadBalancerArn']
    except ClientError as e:
        print(f"Error creating ALB: {e}")
        return None

    # Create a listener for the ALB
    try:
        client.create_listener(
            LoadBalancerArn=alb_arn,
            Port=80,
            Protocol='HTTP',
            DefaultActions=[{
                'Type': 'forward',
                'TargetGroupArn': target_group_arn
            }]
        )
    except ClientError as e:
        print(f"Error creating listener: {e}")
        return None

    # Return the DNS name of the ALB
    return alb_response['LoadBalancers'][0]['DNSName']