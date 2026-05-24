import os

from dj_static import Cling
# pyrefly: ignore [untyped-import]
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = Cling(get_wsgi_application())
