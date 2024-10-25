Открыть конфигурационный файл Nginx для редактирования:
sudo nano /etc/nginx/sites-available/example.com

Добавим следующую конфигурацию в файл: 
server {
    listen 8080;
    server_name example.com;

    # Блок location для /secret_word
    location /secret_word {
        allow 192.0.0.1/20;      # Разрешаем доступ из диапазона 192.0.0.1/20
        deny 192.0.0.1;          # Запрещаем доступ конкретному IP 192.0.0.1
        deny all;                # Запрещаем всем остальным

        add_header Content-Type text/plain;
        return 203 "jusan-nginx-ip";  # Возвращаем строку со статусом 203
    }
}

После внесения изменений проверим конфигурацию Nginx на наличие ошибок:
sudo nginx -t

Перезапустим Nginx:
sudo systemctl restart nginx
 
Проверка:
curl -I http://localhost:8080/secret_word

