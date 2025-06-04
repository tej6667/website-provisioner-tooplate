# Boto3 EC2 and ALB Provisioner

This project automates the provisioning of an EC2 instance with Amazon Linux 2023, a key pair, and a security group using Boto3. It also sets up an Application Load Balancer (ALB) and registers the EC2 instance with it.

## Project Structure

```
boto3-ec2-alb-provisioner
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── ec2.py
│   ├── alb.py
│   ├── security_group.py
│   ├── key_pair.py
│   ├── userdata
│   │   └── template_userdata.sh
│   └── utils.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.x
- Boto3

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd boto3-ec2-alb-provisioner
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure your AWS credentials. You can do this by setting up the `~/.aws/credentials` file or by exporting environment variables.

4. Update the `src/config.py` file with your desired AWS region, instance type, and the template name from tooplate.com.

## Usage

To provision the resources, run the following command:
```
python src/main.py
```

This will create the necessary resources including:
- A key pair for the EC2 instance.
- A security group allowing SSH (port 22) from your IP and HTTP (port 80) from anywhere.
- An EC2 instance running Amazon Linux 2023.
- An Application Load Balancer (ALB) that routes traffic to the EC2 instance.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.