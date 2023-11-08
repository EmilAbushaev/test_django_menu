# Тестовое задание

## Используемые технологии и библиотеки:
* Python 3.12
* asgiref 3.7.2
* Django 4.2.7
* django-js-asset 2.1.0
* django-mptt 0.15.0
* sqlparse 0.4.4


## Установка и настройки
### Создание и активирование виртуального окружения:
```
python -m venv env
```
```
source venv/test_django_menu/activate
``` 
### Установка зависимостей:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
### Применение миграций:
```
python3 manage.py migrate
```
### Запуск django сервера:
```
python manage.py runserver
```