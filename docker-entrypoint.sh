#!/bin/bash

# reiniciando nginx
#rm /etc/nginx/sites-enabled/default
#/etc/init.d/nginx restart

echo "Coletando arquivos estáticos...";
uv run python manage.py collectstatic --no-input;

echo "Compilando mensagens...";
uv run python manage.py compilemessages;

echo "Rodando migrações projeto...";
uv run manage.py migrate;

echo "Iniciando o servidor uwsgi";
uv run uwsgi --ini ./conf/uwsgi.ini
