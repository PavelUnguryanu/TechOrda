sudo systemctl start nginx

Установка ufw:
sudo apt install ufw -y

Разрешаем HTTP (80) и HTTPS (443):
sudo ufw allow 80
sudo ufw allow 443

Запрещаем все входящие соединения по умолчанию:
sudo ufw default deny incoming

Разрешаем все исходящие соединения:
sudo ufw default allow outgoing

Отключаем доступ к порту 9090 для IPv4 и IPv6:
sudo ufw deny 9090

Включаем ufw:
sudo ufw enable

Проверка статус ufw
sudo ufw status

Состояние: активен

В                          Действие    Из
-                          --------    --
80                         ALLOW       Anywhere                  
443                        ALLOW       Anywhere                  
9090                       DENY        Anywhere                  
80 (v6)                    ALLOW       Anywhere (v6)             
443 (v6)                   ALLOW       Anywhere (v6)             
9090 (v6)                  DENY        Anywhere (v6)   
