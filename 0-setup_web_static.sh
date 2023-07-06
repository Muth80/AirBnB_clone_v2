#!/usr/bin/env bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary folders if they don't exist
folders=(
    "/data/"
    "/data/web_static/"
    "/data/web_static/releases/"
    "/data/web_static/shared/"
    "/data/web_static/releases/test/"
)

for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
    fi
done

# Create a fake HTML file for testing
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html

# Create symbolic link /data/web_static/current
if [ -L "/data/web_static/current" ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
if grep -q "location /hbnb_static/ {" "$config_file"; then
    sed -i "s@location /hbnb_static/ {@location /hbnb_static/ {\n\t\talias /data/web_static/current/;@" "$config_file"
else
    sed -i "/server_name _;/a\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" "$config_file"
fi

# Restart Nginx
service nginx restart

