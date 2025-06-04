def create_ec2_instance(ec2_client, instance_type, key_name, security_group_id, userdata):
    response = ec2_client.run_instances(
        ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux 2023 AMI ID (example, please verify)
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        UserData=userdata,
        MinCount=1,
        MaxCount=1
    )
    return response['Instances'][0]['InstanceId']

def get_instance_status(ec2_client, instance_id):
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    return response['Reservations'][0]['Instances'][0]['State']['Name']

def terminate_ec2_instance(ec2_client, instance_id):
    ec2_client.terminate_instances(InstanceIds=[instance_id])