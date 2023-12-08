#!/bin/bash

sudo mkdir /opt/test-svc
sudo chown $USER:$USER /opt/test-svc
cp -r test_task /opt/test-svc/test_task

cd /opt/test-svc
#python -m virtualenv venv
python3 -m venv venv
/opt/test-svc/venv/bin/pip install -r /opt/test-svc/test_task/requirements.txt
crontab -l > mycron
echo "*/10 * * * * /opt/test-svc/venv/bin/python /opt/test-svc/test_task/manage.py logingstatus" >> mycron
crontab mycron
rm mycron

read -p "Введите адрес проверяемого сервера с http://: " remote_server
read -p "Введите порт проверяемого сервера: " remote_port

echo "REMOTE_SERVER='$remote_server'" >> /opt/test-svc/test_task/test_task/settings_local.py
echo "REMOTE_PORT='$remote_port'" >> /opt/test-svc/test_task/test_task/settings_local.py
