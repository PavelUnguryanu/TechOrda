# Используем базовый образ nginx:mainline
FROM nginx:mainline

# Копируем файл конфигурации Nginx
COPY jusan-dockerfile.conf /etc/nginx/conf.d/jusan-dockerfile.conf

# Копируем содержимое распакованного архива в нужный каталог
COPY jusan-dockerfile /var/www/jusan-dockerfile
