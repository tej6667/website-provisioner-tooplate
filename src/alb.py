def create_alb(client, template_name, vpc_id):
    response = client.create_load_balancer(
        Name=f"{template_name}-alb",
        Subnets=[vpc_id],  # Replace with actual subnet IDs
        SecurityGroups=[f"{template_name}-alb-sg"],
        Scheme='internet-facing',
        Tags=[
            {
                'Key': 'Name',
                'Value': f"{template_name}-alb"
            },
        ],
        Type='application',
    )
    return response['LoadBalancers'][0]['LoadBalancerArn']


def register_ec2_with_alb(client, alb_arn, instance_id):
    response = client.register_targets(
        TargetGroupArn=alb_arn,
        Targets=[
            {
                'Id': instance_id,
            },
        ]
    )
    return response


def create_target_group(client, template_name):
    response = client.create_target_group(
        Name=f"{template_name}-tg",
        Protocol='HTTP',
        Port=80,
        VpcId='vpc-xxxxxx',  # Replace with actual VPC ID
        HealthCheckProtocol='HTTP',
        HealthCheckPort='80',
        HealthCheckPath='/',
        HealthCheckIntervalSeconds=30,
        HealthCheckTimeoutSeconds=5,
        HealthyThresholdCount=2,
        UnhealthyThresholdCount=2,
        Tags=[
            {
                'Key': 'Name',
                'Value': f"{template_name}-tg"
            },
        ],
    )
    return response['TargetGroups'][0]['TargetGroupArn']