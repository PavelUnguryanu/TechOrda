#!/bin/bash
# solution.sh - Docker run solution for task

# Скачиваем nginx.conf
curl -o nginx.conf https://github.com/Smagicom/TechOrda/blob/main/docker/docker-bind/nginx.conf

# Запускаем контейнер NGINX с параметрами
docker run -d --name jusan-docker-bind -p 7777:80 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf nginx:mainline

# Вывод списка запущенных контейнеров
docker ps

# Просмотр логов NGINX
docker logs jusan-docker-bind
