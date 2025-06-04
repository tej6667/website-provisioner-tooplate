#!/bin/bash
# Update the package manager and install necessary packages
yum update -y
yum install -y wget

# Download the website template from tooplate.com
wget -O /var/www/html/template.zip https://www.tooplate.com/zip/template.zip

# Unzip the downloaded template
unzip /var/www/html/template.zip -d /var/www/html/

# Start a simple HTTP server to serve the template
cd /var/www/html/template
python3 -m http.server 80 &

# Clean up the downloaded zip file
rm /var/www/html/template.zip