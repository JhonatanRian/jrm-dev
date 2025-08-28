#!/bin/bash

# reiniciando nginx
#rm /etc/nginx/sites-enabled/default
#/etc/init.d/nginx restart

echo "Rodando migrações projeto...";
uv run manage.py migrate;

echo "Rodando fixtures...";
uv run manage.py loaddata users__00 portifolio;

echo "Iniciando o servidor uwsgi";
uv run uwsgi --ini ./conf/uwsgi.ini
