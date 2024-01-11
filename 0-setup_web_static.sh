#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
sh -c "echo '<html>
  <head>
  </head>
  <body>
    Welcome to you !
  </body>
</html>' | sudo tee /data/web_static/releases/test/index.html"
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo tee /etc/nginx/sites-available/default << EOF
server {
  listen 80;
  location /hbnb_static {
    alias /data/web_static/current/;
   }
}
EOF
sudo service nginx restart
