#!/usr/bin/env bash
# 0-setup_web_static.sh
# Bash script that  sets up your web servers for the deployment of web_static

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Create folders
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create the fake HTML content and write it to the file
test_file="/data/web_static/releases/test/index.html"
echo "<html>
<head>
    <title>Fake HTML File</title>
</head>
<body>
    <h1>This is a fake HTML file.</h1>
</body>
</html>" | sudo tee "$test_file" > /dev/null

# Create a symbolic link
directory_path="/data/web_static/releases/test/"
symLink="/data/web_static/current"
sudo ln -sf "$directory_path" "$symLink"
sudo chown -R ubuntu:ubuntu /data
myc="\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/\;\n\t}\n"
st="server {"
sudo sed -i "s/^$st/$st$myc/" /etc/nginx/sites-enabled/default
sudo service nginx start
