"""
WSGI config for recipeBox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
#-- if you were deploying, could connect nginx or apache into wsgi.py and
    # allow it to serve our app w/o having to deal with django webserver
    # professional version of django: offers server debugging inside built-in debugger
    # can debug on the fly.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipeBox.settings')

application = get_wsgi_application()
