import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onadata.settings.kc_environ')

application = get_wsgi_application()
