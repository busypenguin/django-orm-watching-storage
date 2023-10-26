# Пульт охраны банка

Проект создан для поимки вора и отслеживания посетителей в хранилище банка "Сияние"

### Как установить

Создайте файл .env и запишите туда переменные окружения(DB_HOST, DB_PORT,DB_NAME, DB_USER, DB_PASSWORD, SECRET_KEY, DEBUG, ALLOWED_HOSTS) и их значения.

Например:

```DB_HOST = checkpoint.devman.org```

```DB_PORT = 1234```

```DB_NAME = checkpoint```

```DB_USER = gjacuard```

```DB_PASSWORD = the_best_password_ever```

```SECRET_KEY = SECRET```

```DEBUG = False```


Затем запустите файл manage.py, написав в терминале:

```python3 manage.py runserver 0.0.0.0:8000```



Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
