# das darf nicht online sein
# Make this unique, and don't share it with anybody.

# Django settings_local for immoarena project.
from os import path 
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = 'oneloudrhours'             # Or path to database file if using sqlite3.
#DATABASE_USER = 'postgres'             # Not used with sqlite3.
#DATABASE_PASSWORD = 'roland'         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.


#DATABASES = {
#    'default': {
#        'ENGINE': 'postgresql_psycopg2',
#        'NAME': 'oneloudrhours',
#        'USER': 'postgres',
#        'PASSWORD': 'roland',
#        'HOST': '',
#        'PORT': '',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'beautyparlour_oneloudrhours',
        'USER': 'beautyparlour',
        'PASSWORD': 'BedGmd8c',
        'HOST': '',
        'PORT': '',
    }
}


URL = 'http://captain.sites.djangoeurope.com/'

#google maps key
GOOGLE_KEY = 'ABQIAAAAwW8e4vOGD-0EcKHxxa0_QhQCULP4XOMyhPd8d_NrQQEO8sT8XBRwAjay1jJRh1Zq73pRghRFR_6lAg'


BASE_DIR = path.dirname(path.abspath(__file__))
# BASE_DIR = 'Documents/Daten/Inet/Goliat/!Webmeisterei/umweltv.at/umweltv/'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

FORCE_SCRIPT_NAME = ''

#EMAIL_HOST = '192.168.2.1' 
#EMAIL_HOST_PORT = 25 
#EMAIL_USE_TLS = True 
#EMAIL_HOST_USER = 'username' 
#EMAIL_HOST_PASSWORD = 'password'

EMAIL_HOST='smtp.gmail.com'
EMAIL_USE_TLS=1
EMAIL_PORT=587
EMAIL_HOST_USER='roland.kainbacher@gmail.com'
EMAIL_HOST_PASSWORD='osterhase'


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = 'public/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c%v3v31xmhnxv2r806!1e&*5r1du3p9#pbh2qk+1foa%u2sz1^'

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
    os.path.join(PROJECT_ROOT, "templates"),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

#CMS_MEDIA_ROOT = '/opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/django_cms-2.0.2-py2.6.egg/cms/media/cms'
