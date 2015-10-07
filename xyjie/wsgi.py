"""
WSGI config for xyjie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import sys
path = '/var/www/html/xyjie'
if path not in sys.path:
	sys.path.append(path)

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xyjie.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
