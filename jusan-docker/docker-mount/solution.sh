#!/bin/bash
# solution.sh - Docker run solution for jusan-docker-mount

# Скачиваем конфигурационный файл
curl -o jusan-docker-mount.conf URL_КОНФИГУРАЦИОННОГО_ФАЙЛА

# Скачиваем и распаковываем архив
curl -o jusan-docker-mount.zip URL_АРХИВА
unzip jusan-docker-mount.zip -d ./jusan-docker-mount

# Запускаем контейнер с монтированными файлами
docker run -d --name jusan-docker-mount -p 9999:80 \
    -v $(pwd)/jusan-docker-mount.conf:/etc/nginx/conf.d/jusan-docker-mount.conf \
    -v $(pwd)/jusan-docker-mount:/usr/share/nginx/html \
    nginx:mainline

