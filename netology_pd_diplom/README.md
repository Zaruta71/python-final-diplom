# API Сервис заказа товаров для розничных сетей

1. Запускаем контейнер:
```docker-compose up -d --build```
2. Проверяем, запустилась ли база данных и применились ли миграции:
```docker-compose exec web python manage.py migrate --noinput  ```
3. Создаем суперпользователя
```docker-compose exec web python manage.py createsuperuser```

### Проверить работоспособность

Отправить запрос на ```http://localhost/admin/```
Документация: ```http://localhost/openapi/```
