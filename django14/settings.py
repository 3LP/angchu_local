import os
import sys



BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LIKERT_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)))

#sys.path.append(BASE_DIR)
# sys.path.append(LIKERT_DIR)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p-hw2^%2@%2k5r(r2kbm_j6l_9#%djcp!46dgf=t6#l!g@xxw)'

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = True


DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'downbeat',                      # Or path to database file if using sqlite3.
    # The following settings are not used with sqlite3:
    #'USER': 'admin_downbeat',
    #'PASSWORD': 'chaske420',
    #'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
    #'PORT': '',                      # Set to empty string for default.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'site_media', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
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

ROOT_URLCONF = 'django14.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'django14.wsgi.application'


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


INSTALLED_APPS = [
    'likert_field',
    'likert_test_app',
    'suthern',
    'bootstrap3',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
]





