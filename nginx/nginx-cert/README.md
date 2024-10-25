Подготовка SSL сертификатов:
sudo mkdir -p /etc/nginx/ssl
sudo cp /var/www/track-devops.crt /etc/nginx/ssl/
sudo cp /var/www/track-devops.key /etc/nginx/ssl/

Создаем файла с параметром ssl_dhparam:
sudo openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048

Настройка NGINX:
sudo nano /etc/nginx/sites-available/jusan.kz

Добавляем следующий серверный блок:
server {
    listen 443 ssl;  # Настраиваем прослушивание на порту 443 для HTTPS
    server_name jusan.kz;

    ssl_certificate /etc/nginx/ssl/track-devops.crt;  # Путь к SSL сертификату
    ssl_certificate_key /etc/nginx/ssl/track-devops.key;  # Путь к приватному ключу
    ssl_dhparam /etc/nginx/ssl/dhparam.pem;  # Путь к файлу dhparam для безопасности

    # SSL параметры для лучшей безопасности
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location /secret_word {
        add_header Content-Type text/plain;
        return 201 "jusan-nginx-cert";  # Возвращаем строку со статусом 201
    }
}

# Настроим редирект с HTTP на HTTPS
server {
    listen 80;
    server_name jusan.kz;
    return 301 https://$host$request_uri;  # Перенаправляем HTTP на HTTPS
}


sudo nginx -t

sudo systemctl restart nginx

Проверка:
curl -H "Host: jusan.kz" -k https://localhost/secret_word

