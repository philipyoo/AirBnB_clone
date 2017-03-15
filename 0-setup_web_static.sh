#!/usr/bin/env bash
# Script to set up web servers for deployment of 'web_static' project
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '37i\\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
