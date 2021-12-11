sudo rm -rf /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo ln -sf /home/box/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/etc/gunicorn_django.conf /etc/gunicorn.d/django


sudo /etc/init.d/nginx restart
sudo service gunicorn restart