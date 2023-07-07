#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

# Install nginx if it's not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Make required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, delete it if it already exists
[ -e /data/web_static/current ] && sudo unlink /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
update="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "48i $update" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
```
