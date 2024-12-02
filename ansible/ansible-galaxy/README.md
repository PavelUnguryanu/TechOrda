Отчет по выполнению задания: Настройка Ansible Galaxy и конфигурация Nginx
1. Создание ветки galaxy

Работа велась в ветке galaxy, которая была создана от ветки vault:

git checkout vault
git checkout -b galaxy

2. Установка роли geerlingguy.nginx

Роль была установлена с помощью команды:

ansible-galaxy install geerlingguy.nginx

Роль успешно загружена в систему.
3. Обновление playbook

Роль nginx была заменена на geerlingguy.nginx в playbook.yml. Итоговый код:

---
# Playbook for configuring the application and load balancer

- hosts: lb
  become: true
  vars_files:
    - roles/nginx-configuration/vars/nginx_secret_token.yml
  roles:
    - geerlingguy.nginx
    - nginx-configuration
  vars:
    server_port: 7070
    server_name: jmart-ansible.kz
    secret: "{{ secret_token }}"

- hosts: app
  become: true
  roles:
    - application

4. Создание файла шаблона nginx.conf.j2

Для корректной работы был создан шаблон nginx.conf.j2 в директории roles/nginx-configuration/templates:

server {
    listen {{ server_port }};
    server_name {{ server_name }};

    location /main {
        return 200 "{{ secret }}";
    }
}

5. Настройка задачи деплоя

Задача деплоя шаблона была обновлена для использования модуля template:

- name: Deploy Nginx configuration
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/conf.d/nginx.conf
    owner: root
    group: root
    mode: '0644'
  notify: restart nginx

6. Проверка

После применения playbook выполнены следующие проверки:

    Проверка состояния Nginx:

sudo systemctl status nginx

Проверка синтаксиса конфигурации Nginx:

sudo nginx -t

Тестирование работы через curl:

    curl http://localhost:7070/main

Результат:

Jusan Singularity