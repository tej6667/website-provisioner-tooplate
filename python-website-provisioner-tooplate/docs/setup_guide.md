# Setup Guide for Tooplate Template Project

## Overview
This guide provides step-by-step instructions for setting up the Tooplate Template Project, which automates the creation of AWS resources including an EC2 instance, a security group, a key pair, and an Application Load Balancer (ALB).

## Prerequisites
- An AWS account with appropriate permissions to create EC2 instances, security groups, key pairs, and ALBs.
- Python 3.x installed on your local machine.
- `boto3` library installed. You can install it using pip:

  ```
  pip install boto3
  ```

## Project Structure
The project is organized as follows:

```
tooplate-template-project
├── src
│   ├── __init__.py
│   ├── key_pair.py
│   ├── security_group.py
│   ├── ec2_instance.py
│   ├── alb.py
│   ├── userdata
│   │   └── website_setup.sh
│   └── utils.py
├── docs
│   └── setup_guide.md
├── requirements.txt
├── README.md
```

## Steps to Set Up AWS Resources

1. **Clone the Repository**
   Clone the project repository to your local machine:

   ```
   git clone <repository-url>
   cd tooplate-template-project
   ```

2. **Configure AWS Credentials**
   Ensure your AWS credentials are configured. You can set them up using the AWS CLI:

   ```
   aws configure
   ```

   Provide your AWS Access Key, Secret Key, region, and output format.

3. **Create Key Pair**
   Use the `key_pair.py` module to create a key pair. The key pair name will be derived from the template name from tooplate.com. 

   Example usage:
   ```python
   from src.key_pair import create_key_pair
   key_pair_name = "tooplate_template"
   create_key_pair(key_pair_name)
   ```

4. **Create Security Group**
   Use the `security_group.py` module to create a security group that allows SSH (port 22) from your IP and HTTP (port 80) from anywhere.

   Example usage:
   ```python
   from src.security_group import create_security_group
   security_group_name = "tooplate_template_sg"
   create_security_group(security_group_name)
   ```

5. **Launch EC2 Instance**
   Use the `ec2_instance.py` module to launch an EC2 instance with the Amazon Linux 2023 AMI, t2.micro instance type, the key pair, and the security group created earlier. Pass the user data script for website setup.

   Example usage:
   ```python
   from src.ec2_instance import create_ec2_instance
   ami_id = "ami-xxxxxxxx"  # Replace with the actual AMI ID for Amazon Linux 2023
   instance_type = "t2.micro"
   create_ec2_instance(ami_id, instance_type, key_pair_name, security_group_name)
   ```

6. **Create Application Load Balancer (ALB)**
   Use the `alb.py` module to create an ALB and add the EC2 instance to the target group.

   Example usage:
   ```python
   from src.alb import create_alb
   alb_name = "tooplate_template_alb"
   create_alb(alb_name)
   ```

7. **Retrieve ALB DNS**
   After creating the ALB, retrieve its DNS name to access the website.

   Example usage:
   ```python
   # Assuming the create_alb function returns the ALB DNS
   alb_dns = create_alb(alb_name)
   print(f"Access your website at: http://{alb_dns}")
   ```

## Conclusion
Follow these steps to set up your AWS resources using the Tooplate Template Project. Ensure to replace placeholder values with actual data where necessary. For further details, refer to the individual module documentation in the `src` directory.