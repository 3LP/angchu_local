import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LIKERT_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "e-xp$itp8$)w=3x)4+higa4x%24@3)-pc6s^^2wly49a624lzr"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'likert_field',
    'likert_test_app',
    'suthern',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

##
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
  
        'DIRS': [
            os.path.join(BASE_DIR, 'global_assets', 'templates')
        ],
        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
##
# List of callables that know how to import templates from various sources.
BASE_PATH = os.path.dirname(__file__)
ROOT_URLCONF = 'django14.urls'
WSGI_APPLICATION = 'django14.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()
# Enable Connection Pooling (if desired)
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Allow all host headers
ALLOWED_HOSTS = ['*'] 
# ALLOWED_HOSTS = ['angchu.herokuapp.com']
# STATIC_ROOT= os.path.join(PROJECT_DIR,'staticfiles/')
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
print(BASE_DIR)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'likert_test_app/static/'),
)
### Whitenoise
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


