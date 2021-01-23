# site_deploy_py_any_notes
# Деплой Django сайта на PythonAnywhere

## Краткое описание процесса деплоя (действия, команды в консоли etc.)

### 1. Создаем виртуальное окружение

mkvirtualenv --python=python3.8 <virtualenv_name>

workon <virtualenv_name> - активация виртуального окружения
deactivate - деактивация

### 2. Проверка инсталляции встроенного установщика пакетов и админской части  
which pip
which django-admin.py

### 3. Устанавливаем необходимые для работы вашего сайта или приложения пакеты
a) pip install <имя пакета>
или
b) pip freeze > requirements.txt - для выгрузки всех пакетов из среды разработки
Далее на PythonAnywhere, запускаем
pip install -r requirements.txt

### 4.Проверяем наличие пакетов
pip list

В моем случае это следующие пакеты:
#----- ----- ----- ----- -----
appdirs                   1.4.4
asgiref                   3.3.1
attrs                     20.3.0
bcrypt                    3.2.0
certifi                   2020.12.5
cffi                      1.14.4
chardet                   4.0.0
cryptography              3.3.1
defusedxml                0.7.0rc2
distlib                   0.3.1
Django                    3.1.5
django-appconf            1.0.4
django-bootstrap-toolkit  2.15.0
django-bootstrap3         14.2.0
django-crispy-forms       1.10.0
django-forms-bootstrap    3.1.0
django-registration-redux 2.9
django-taggit             1.3.0
django-user-accounts      3.0.2
filelock                  3.0.12
idna                      2.10
jsonschema                3.2.0
Markdown                  3.3.3
oauthlib                  3.1.0
pbr                       5.5.1
Pillow                    8.1.0
pip                       20.3.3
psycopg2                  2.8.6
pycparser                 2.20
PyJWT                     2.0.1
pyrsistent                0.17.3
python3-openid            3.2.0
pytz                      2020.5
requests                  2.25.1
requests-oauthlib         1.3.0
setuptools                51.3.3
six                       1.15.0
social-auth-app-django    4.0.0
social-auth-core          3.3.3
sqlparse                  0.4.1
stevedore                 3.3.0
urllib3                   1.26.2
virtualenv                20.4.0
virtualenv-clone          0.5.4
virtualenvwrapper         4.8.4
wheel                     0.36.2
#----- ----- ----- ----- -----

### 5. Клонируем git-репо с вашим проектом или копируем все файлы вручную на сервис PythonAnywhere
#Cloning your Git Repository
а) git clone https://github.com/<git_user_name>/<repo_name>.git

б) для приватных репо
#To private
cd git_repo
git clone https://<git_user_name>:<pass>@github.com/<git_user_name>/<repo_name>.git

### 6. Команды для миграциии моделей (сущностей) в БД и разворачивания вашего сайта-приложения на облачном сервисе PythonAnywhere
Following commands, ex:
(prdsite) 16:55 ~/prdsite/prdsite_proj $ python manage.py makemigrations <application_name>
(prdsite) 16:55 ~/prdsite/prdsite_proj $ python manage.py migrate
(prdsite) 16:56 ~/prdsite/prdsite_proj $ python populate_mblog.py
(prdsite) 16:57 ~/prdsite/prdsite_proj $ python manage.py createsuperuser

python manage.py collectstatic

### 7. Настриваем Web-сервис | PythonAnywhere
a) WSGI - user_name_pythonanywhere_com_wsgi.py (см. данный git-репо)
b) необходимые рабочие директории (с кодом, со статикой, медиа) и др. в разеделе Web на облачном сервисе PythonAnywhere

### 8. Донастраиваем settings.py под ваши нужды
Зависит от функционала сайта.

### 9. Пример получившегося деплоя сайта-блога
nicholasid7.pythonanywhere.com

Всем, peace! 
Congratulations!
