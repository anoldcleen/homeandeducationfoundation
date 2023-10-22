"""
WSGI config for RomicFinal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

project_home = '/home/a/RomicFinal/'

if project_home not in  sys.path:
	sys.path.insert(0 , project_home)
	pass


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RomicFinal.settings')

application = get_wsgi_application()
