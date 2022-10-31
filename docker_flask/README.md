## Установка и запуск

docker build -t pzheleznikova/flaskapp .

docker run --name app -p 8000:8000 pzheleznikova/flaskapp

## Скачивание докер-образа

docker pull pzheleznikova/flaskapp

docker run -p 8000:8000 pzheleznikova/flaskapp
