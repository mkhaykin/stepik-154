sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepic"
mysql -uroot -e "grant all privileges on stepic.* to 'box'@'localhost' with grant option;"
cd /home/box/web/ask/
python manage.py makemigrations
python manage.py migrate
