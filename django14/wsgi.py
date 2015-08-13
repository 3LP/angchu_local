import os
import sys

path = '/Users/jacksonchiefelk/independent/WebApps/angchu'

if path not in sys.path:
	sys.path.append(path)




os.environ['DJANGO_SETTINGS_MODULE'] = 'django14.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())