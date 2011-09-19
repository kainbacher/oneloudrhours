# Make this unique, and don't share it with anybody.

# Django settings_local for immoarena project.
import os
from os import path 


# Mediatemple
FORCE_SCRIPT_NAME = ""


DEBUG = True
TEMPLATE_DEBUG = DEBUG

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


URL = 'http://oneloudrhours.beautyparlour.at/'

#google maps key
GOOGLE_KEY = 'ABQIAAAAwW8e4vOGD-0EcKHxxa0_QhQCULP4XOMyhPd8d_NrQQEO8sT8XBRwAjay1jJRh1Zq73pRghRFR_6lAg'


BASE_DIR = path.dirname(path.abspath(__file__))
# BASE_DIR = 'Documents/Daten/Inet/Goliat/!Webmeisterei/umweltv.at/umweltv/'


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
# MEDIA_ROOT = 'public/media/'
#MEDIA_ROOT = '/home/1797/users/.home/containers/django/captain/public/media'
#MEDIA_ROOT = '/home/1797/containers/django/captain/public/media/'
#MEDIA_ROOT = "/home/1797/containers/django/captain/public/media"
#MEDIA_ROOT =  os.path.join(os.path.dirname(__file__), 'public/media/')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'public', 'media')
#MEDIA_ROOT = BASE_DIR + '/public/media/'


MEDIA_URL = '/media/'


# wird benoetigt damit die styles im admin angezeigt werden
ADMIN_MEDIA_PREFIX = '/media/admin/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c%v3v31xmhnxv2r806!1e&*5r1du3p9#pbh2qk+1foa%u2sz1^'

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

CMS_MEDIA_ROOT = '/opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/django_cms-2.0.2-py2.6.egg/cms/media/cms'




#MEDIA_ROOT = '/home/1797/users/.home/domains/media.beautyparlour.at/html/'
#MEDIA_URL = '/'
#ADMIN_MEDIA_PREFIX = '/media/'
