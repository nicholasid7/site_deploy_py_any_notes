# site_deploy_py_any_notes
## Деплой Django сайта на PythonAnywhere

Видео с некоторыми деталями деплоя и конфигурирования вашего сайта:
[![NoIco](http://www.sherpis.com/prdsite/static/mblog/images/yt.thumb.png)](https://youtu.be/MTBgioO0XcM)

### Краткое описание процесса деплоя (действия, команды в консоли etc.)

### 0. Регаемся в облачном сервисе PythonAnywhere 

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

### 4. Проверяем наличие пакетов
pip list

<details>
  <summary>В моем случае это следующие основные пакеты:</summary>
<ui>
<li>appdirs 1.4.4</li>

<li>asgiref 3.3.1</li>

<li>attrs 20.3.0</li>

<li>bcrypt 3.2.0</li>

<li>certifi 2020.12.5</li>

<li>cffi 1.14.4</li>

<li>chardet 4.0.0</li>

<li>cryptography 3.3.1</li>

<li>defusedxml 0.7.0rc2</li>

<li>distlib 0.3.1</li>

<li>Django 3.1.5</li>

<li>django-appconf 1.0.4</li>

<li>django-bootstrap-toolkit 2.15.0</li>

<li>django-bootstrap3 14.2.0</li>

<li>django-crispy-forms 1.10.0</li>

<li>django-forms-bootstrap 3.1.0</li>

<li>django-registration-redux 2.9</li>

<li>django-taggit 1.3.0</li>

<li>django-user-accounts 3.0.2</li>

<li>filelock 3.0.12</li>

<li>idna 2.10</li>

<li>jsonschema 3.2.0</li>

<li>Markdown 3.3.3</li>

<li>oauthlib 3.1.0</li>

<li>pbr 5.5.1</li>

<li>Pillow 8.1.0</li>

<li>pip 20.3.3</li>

<li>psycopg2 2.8.6</li>

<li>pycparser 2.20</li>

<li>PyJWT 2.0.1</li>

<li>pyrsistent 0.17.3</li>

<li>python3-openid 3.2.0</li>

<li>pytz 2020.5</li>

<li>requests 2.25.1</li>

<li>requests-oauthlib 1.3.0</li>

<li>setuptools 51.3.3</li>

<li>six 1.15.0</li>

<li>social-auth-app-django 4.0.0</li>

<li>social-auth-core 3.3.3</li>

<li>sqlparse 0.4.1</li>

<li>stevedore 3.3.0</li>

<li>urllib3 1.26.2</li>

<li>virtualenv 20.4.0</li>

<li>virtualenv-clone 0.5.4</li>

<li>virtualenvwrapper 4.8.4</li>

<li>wheel 0.36.2</li>

</ui>

</details>


### 5. Клонируем git-репо с вашим проектом или копируем все файлы вручную на сервис PythonAnywhere
#Cloning your Git Repository

а) git clone https://github.com/<git_user_name>/<repo_name>.git

б) для приватных репо

#To private

cd git_repo

git clone https://<git_user_name>:<git_pass> @github.com/<git_user_name>/<repo_name>.git

### 6. Команды для миграции моделей (сущностей) в БД и разворачивания вашего сайта-приложения в облачном сервисе PythonAnywhere
Following commands, ex:

(prdsite) 16:55 ~/prdsite/prdsite_proj $ python manage.py makemigrations <application_name>

(prdsite) 16:55 ~/prdsite/prdsite_proj $ python manage.py migrate

(prdsite) 16:56 ~/prdsite/prdsite_proj $ python populate_mblog.py

(prdsite) 16:57 ~/prdsite/prdsite_proj $ python manage.py createsuperuser

python manage.py collectstatic

### 7. Настраиваем Web-сервис | PythonAnywhere
a) WSGI - user_name_pythonanywhere_com_wsgi.py (см. данный git-репо)

b) необходимые рабочие директории (с кодом, со статикой, медиа) и др. в разделе Web в облачном сервисе PythonAnywhere

### 8. Настраиваем settings.py под ваши нужды
Зависит от функционала сайта.

### 9. Пример получившегося деплоя сайта-блога
nicholasid7.pythonanywhere.com

Всем, peace!

Congratulations!
