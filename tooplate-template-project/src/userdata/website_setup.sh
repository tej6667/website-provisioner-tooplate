#!/bin/bash
# This script sets up a simple website using a template from tooplate.com

# Update the package repository
sudo yum update -y

# Install Apache web server
sudo yum install -y httpd

# Start the Apache service
sudo systemctl start httpd

# Enable Apache to start on boot
sudo systemctl enable httpd

# Download the website template from tooplate.com
# Replace 'template-url' with the actual URL of the template you want to use
wget -O /var/www/html/index.html "https://www.tooplate.com/templates/your-template-url"

# Set proper permissions for the web directory
sudo chown -R apache:apache /var/www/html

# Restart Apache to apply changes
sudo systemctl restart httpd

# Print a message indicating that the setup is complete
echo "Website setup complete. You can access it via the public IP of the EC2 instance."