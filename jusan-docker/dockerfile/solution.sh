#!/bin/bash
# solution.sh - Docker build and run commands for jusan-dockerfile

# Шаг 2: Скачивание файлов
curl -O https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.conf/jusan-dockerfile.conf
curl -O https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.zip/jusan-dockerfile.zip
unzip jusan-dockerfile.zip

# Шаг 3: Создание Dockerfile
echo -e "FROM nginx:mainline\nCOPY jusan-dockerfile.conf /etc/nginx/conf.d/jusan-dockerfile.conf\nCOPY jusan-dockerfile /usr/share/nginx/html" > Dockerfile

# Шаг 5: Проверка образов
docker images

# Шаг 7: Проверка запросов
curl http://localhost:6060
curl http://localhost:6060/dockerfile
curl http://localhost:6060/secret
curl http://localhost:6060/jusan
