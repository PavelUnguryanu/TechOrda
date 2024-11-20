#!/bin/bash

# Запускаем контейнер с перенаправлением портов 22 и 80
echo "Запускаем контейнер..."
docker run -d --name local-vps-22 -p 22:22 -p 80:80 atlekbai/local-vps

# Проверяем, что контейнер запущен
if [[ $? -ne 0 ]]; then
    echo "Ошибка: не удалось запустить контейнер!"
    exit 1
fi

# Ждем, пока контейнер полностью запустится
echo "Ждем 10 секунд для инициализации контейнера..."
sleep 10

# Генерация SSH-ключа
echo "Генерируем SSH-ключ..."
ssh-keygen -t rsa -b 2048 -N "" -f temp_key -q
if [[ ! -f temp_key ]]; then
    echo "Ошибка: файл ключа temp_key не создан!"
    exit 1
fi

# Копируем ключ в контейнер
echo "Копируем SSH-ключ в контейнер..."
ssh-keyscan -H 127.0.0.1 >> ~/.ssh/known_hosts
docker exec -it local-vps-22 /bin/bash -c "mkdir -p /root/.ssh && echo $(cat $(pwd)/temp_key.pub) >> /root/.ssh/authorized_keys"
if [[ $? -ne 0 ]]; then
    echo "Ошибка: не удалось скопировать SSH-ключ в контейнер!"
    exit 1
fi

# Проверяем доступ по SSH
echo "Проверяем подключение по SSH..."
ssh -i temp_key -o StrictHostKeyChecking=no root@127.0.0.1 "echo 'SSH доступ работает!'"
if [[ $? -ne 0 ]]; then
    echo "Ошибка: не удалось подключиться к контейнеру по SSH!"
    exit 1
fi

echo "Настройка завершена. Вы можете использовать SSH с файлом temp_key для подключения к контейнеру."
