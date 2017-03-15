#!/usr/bin/env bash
# Script to set up web servers for deployment of 'web_static' project
sudo apt-get -y install nginx
mkdir -p /data/web_static/{releases,shared,current}
mkdir -p /data/web_static/releases/test
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/current/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sudo sed -i '37i\\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
