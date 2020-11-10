# foodgram-project


Проект — сайт «Продуктовый помощник»

### Описание
«Продуктовый помощник» -это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.


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
