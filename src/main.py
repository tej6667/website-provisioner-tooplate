from config import AWS_REGION, INSTANCE_TYPE, TEMPLATE_NAME
from key_pair import create_key_pair
from security_group import create_security_group
from ec2 import launch_ec2_instance
from alb import create_alb, register_instance_with_alb

def main():
    key_pair_name = create_key_pair(TEMPLATE_NAME)
    security_group_id = create_security_group(TEMPLATE_NAME)
    instance_id = launch_ec2_instance(key_pair_name, security_group_id)
    alb_arn = create_alb(TEMPLATE_NAME)
    register_instance_with_alb(alb_arn, instance_id)

if __name__ == "__main__":
    main()