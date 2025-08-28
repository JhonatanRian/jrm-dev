#!/bin/bash

# reiniciando nginx
#rm /etc/nginx/sites-enabled/default
#/etc/init.d/nginx restart

echo "Rodando migrações projeto...";
uv run manage.py migrate;

echo "Rodando fixtures users...";
uv run manage.py loaddata users__00;
echo "Rodando fixtures stack...";
uv run manage.py loaddata stack__01;
echo "Rodando fixtures groupstack...";
uv run manage.py loaddata groupstack__02;
echo "Rodando fixtures project...";
uv run manage.py loaddata project__03;
echo "Rodando fixtures sectionhero...";
uv run manage.py loaddata sectionhero__04;
echo "Rodando fixtures portifolio...";
uv run manage.py loaddata portifolio__05;

echo "Iniciando o servidor uwsgi";
uv run uwsgi --ini ./conf/uwsgi.ini
