#1: Подготовка файлов и каталогов
Каталог для index.html:

sudo mkdir -p /var/www/example.com
 
sudo mkdir -p /var/www/example.com/images
sudo mkdir -p /var/www/example.com/gifs

sudo unzip ~/cats.zip -d /var/www/example.com/images/
sudo unzip ~Загрузки/gifs.zip -d /var/www/example.com/gifs/
 
openssl passwd SteveJobs1955
Повторить то же самое для учетной записи marketing:marketingP@ssword:

 
openssl passwd marketingP@ssword
Создать файл с паролями для каждой учетной записи:

Для design:

 
sudo nano /etc/nginx/conf.d/design_passwd
Добавить строку:

 
design:$6$...  # Здесь должен быть зашифрованный пароль
Для marketing:

 
sudo nano /etc/nginx/conf.d/marketing_passwd
Добавить строку:

 
marketing:$6$...  # Здесь должен быть зашифрованный пароль
#2: Настройка Nginx
Откройте файл конфигурации Nginx для редактирования:

 
sudo nano /etc/nginx/sites-available/example.com
Добавить следующую конфигурацию:

nginx
Копировать код
server {
    listen 8080;
    server_name example.com;

    # Location для корневого пути, обслуживающего файл index.html
    location / {
        root /var/www/example.com;
        index index.html;
    }

    # Location для /images с базовой аутентификацией для design
    location /images {
        auth_basic "Restricted Access - Images";
        auth_basic_user_file /etc/nginx/conf.d/design_passwd;
        root /var/www/example.com/images;
    }

    # Location для /gifs с базовой аутентификацией для marketing
    location /gifs {
        auth_basic "Restricted Access - GIFs";
        auth_basic_user_file /etc/nginx/conf.d/marketing_passwd;
        root /var/www/example.com/gifs;
    }
}
Описание:
listen 8080;: Указывает, что Nginx будет слушать на порту 8080.
server_name example.com;: Устанавливает example.com как доменное имя сервера.
location / { ... }: Обслуживает корневой путь и файл index.html.
location /images { ... }: Обслуживает файлы из каталога /images и защищен базовой аутентификацией для учетной записи design.
location /gifs { ... }: Обслуживает файлы из каталога /gifs и защищен базовой аутентификацией для учетной записи marketing.
Сохранить файл и закрыть редактор.

#3: Активация конфигурации и перезапуск Nginx
Создать символическую ссылку на файл конфигурации в директории sites-enabled:

 
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
Проверить конфигурацию Nginx на ошибки:

 
sudo nginx -t
Перезапустить Nginx для применения изменений:

 
sudo systemctl restart nginx
#4: Тестирование
Проверка доступа к / (корневой путь): Запрос должен вернуть страницу с index.html:

 
curl http://localhost:8080/
Проверка доступа к /images (логин design): При доступе к /images потребуется ввести учетные данные:

 
curl --user design:SteveJobs1955 http://localhost:8080/images/
Проверка доступа к /gifs (логин marketing): При доступе к /gifs потребуется ввести учетные данные:

 
curl --user marketing:marketingP@ssword http://localhost:8080/gifs/

