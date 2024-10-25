# 1: Установка openssl
sudo apt update
sudo apt install openssl
# 2: Создание файла с паролями

openssl passwd SomePassword1993
# получаем
$1$b9Xa1yQM$PC8hOheuE8dPQYcQE1qYW0

# файл с паролями:


sudo nano /etc/nginx/conf.d/passwd

pavel:$1$b9Xa1yQM$PC8hOheuE8dPQYcQE1qYW0

# 3: настройка Nginx для базовой аутентификации /etc/nginx/sites-available/default:

sudo nano /etc/nginx/sites-available/default
блок location:

server {
    listen 80;
    server_name localhost;

    location / {
        auth_basic "Приватный сайт";  # Это сообщение будет показано во всплывающем окне аутентификации
        auth_basic_user_file /etc/nginx/conf.d/passwd;  # Путь к файлу с паролями
    }

    location /api/ {
        proxy_pass http://127.0.0.1:9090;  # Проксирование на API
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# 4: Проверить конфигурацию Nginx
sudo nginx -t

# 5: Перезапустить Nginx

sudo systemctl restart nginx
# 6: Тестирование

curl --user pavel:SomePassword1993 http://localhost/

# ответ

<html><body><h1>Welcome to Nginx Reverse Proxy!</h1></body></html>
