#!/bin/bash

# reiniciando nginx
#rm /etc/nginx/sites-enabled/default
#/etc/init.d/nginx restart

echo "Rodando migrações projeto...";
uv run manage.py migrate;

echo "Rodando fixtures...";
uv run manage.py loaddata users__00 stack__01 groupstack__02 project__03 sectionhero__04 portifolio__05;

echo "Iniciando o servidor uwsgi";
uv run uwsgi --ini ./conf/uwsgi.ini
