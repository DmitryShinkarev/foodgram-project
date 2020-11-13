# foodgram-project


![foodgram-project](https://github.com/DmitryShinkarev/foodgram-project/workflows/foodgram-project/badge.svg)

Проект — сайт «Продуктовый помощник»

### Описание
«Продуктовый помощник» - Это сайт где пользователи могут вести свой кулинарный блог добавляя рецепты, делясь ими с другими пользователями а так же подписываясь на других любимых пользователей и добавляя рецепты в "избранное" от куда удобноо можно скачать список покупок для нужных рецептов.

Сайт опубликован по адресу [http://178.154.226.80]


## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- библиотека django-filter - фильтрация запросов
- базы данны - PostgreSQL
- автоматическое развертывание проекта - Docker, docker-compose, Gunicorn, Nginx

### Установка
- склонируйте проект с реппозитория GitHub
    ```
    git clone https://github.com/DmitriyShinkarev/foodgram-project.git
    ```
- перейдите в директорию foodgram-project/
    ```
    cd foodgram-project/
    ```
- запустите docker-compose
    ```
    docker-compose -f docker-compose.yaml up -d
    ```
- Выполнить миграции и собрать статику, выполнив команды:
    ```
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py collectstatic
    docker-compose -f docker-compose.yaml run --rm web python manage.py createsuperuser
    ```
