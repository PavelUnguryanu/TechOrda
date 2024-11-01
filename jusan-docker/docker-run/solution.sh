#!/bin/bash
# solution.sh - Docker run solution for task

# Запускаем контейнер NGINX на порту 8888
docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline

# Выводим список активных контейнеров
docker ps

# Останавливаем контейнер
docker stop jsn-dkr-run

# Проверяем, что контейнер больше не активен
docker ps

# Выводим список всех контейнеров, включая остановленные
docker ps -a
