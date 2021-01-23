# This file contains the WSGI configuration required to serve up your
# web application at http://user_name.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
# 
# The below has been auto-generated for your Django project

import os
import sys

# add your project directory to the sys.path
path = '/home/user_name/prdsite/prdsite_proj/'
if path not in sys.path:
    # sys.path.insert(0, path)
    sys.path.append(path)

os.chdir(path)

# set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'prdsite.settings')

# Import your Django project's configuration
import django
django.setup()

# Import the Django WSGI to handle any requests
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# # serve django via WSGI
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
