sudo nano /etc/nginx/sites-available/example.com

# Добовляем блок конфигурации
server {
    listen 8080;
    server_name example.com;

    # Location для корневого пути, обслуживающего файл index.html
    location / {
        root /var/www/example.com;
        index index.html;
    }

    # Location для /images, обслуживающего файлы из архива cats.zip
    location /images/ {
        alias /var/www/example.com/images/;
    }

    # Location для /gifs, обслуживающего файлы из архива gifs.zip
    location /gifs/ {
        alias /var/www/example.com/gifs/;
    }

    # Location для /secret_word, возвращающего строку с 201 статусом
    location /secret_word {
        return 201 'jusan-nginx-locations';
    }
}

# Создаем директорию для сайта
sudo mkdir -p /var/www/example.com

sudo cp ~/Загрузки/index.html /var/www/example.com/

sudo mkdir -p /var/www/example.com/images /var/www/example.com/gifs

sudo unzip ~/Загрузки/cats.zip -d /var/www/example.com/images/
sudo unzip ~/Загрузки/gifs.zip -d /var/www/example.com/gifs/

sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/

sudo nginx -t

sudo systemctl restart nginx

# Проверка
curl -H "Host: example.com" http://localhost:8080/
