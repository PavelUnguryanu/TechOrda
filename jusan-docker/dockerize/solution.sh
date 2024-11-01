#!/bin/bash

# Шаг 3: Собираем Docker-образ
docker build -t jusan-fastapi-final:dockerized .

# Шаг 4: Проверяем наличие образа
docker images

# Шаг 5: Запускаем контейнер с заданными параметрами
docker run -d -p 8080:8080 --name jusan-dockerize jusan-fastapi-final:dockerized
