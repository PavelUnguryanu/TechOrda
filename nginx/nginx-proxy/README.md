#Открываем в редакторе конфигурацию nginx
sudo nano /etc/nginx/sites-available/default
#настроим блок location
server {
    listen 80;
    server_name localhost;

    # Location для корневого пути, обслуживающего файл index.html
    location / {
        root /var/www/html;   # Директория, где хранится index.html
        index index.html;
    }

    # Location для /api, удаляющий /api из URI и проксирующий запросы на API
    location /api/ {
        rewrite ^/api/(.*)$ /$1 break;  # Удаление префикса /api из URI
        proxy_pass http://127.0.0.1:9090;  # Проксирование на API на порту 9090
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

#провеим конфигурацию nginx на наличие ошибок
sudo nginx -t
#перезапустим nginx
sudo systemctl restart nginx
#проверим пути
curl http://localhost/
# location /: Этот блок обслуживает файл index.html 
curl http://localhost/api/

#Этот блок переписывает URI, удаляя префикс /api из пути запроса, и перенаправляет запрос на локально работающий API, который доступен на http://127.0.0.1:9090/
