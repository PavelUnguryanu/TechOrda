# Установите базовый образ Python
FROM python:3.9-slim

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы проекта
COPY . .

# Установите зависимости
RUN pip install fastapi uvicorn prometheus_client

# Запустите приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]

