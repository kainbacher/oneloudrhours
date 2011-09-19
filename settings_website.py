# Django settings for shapingthings project.

# Djanog 1.0 ... Needed for Mediatemple
FORCE_SCRIPT_NAME="" 
SITE_ID = 3

import os

BASE_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('rka', 'rka@beautyparlour.at'),
)

MANAGERS = ADMINS

# DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or acle'.
# DATABASE_NAME = 'db1797_website'             # Or path to database file if using sqlite3.
# DATABASE_USER = 'beautyparlour'             # Not used with sqlite3.
# DATABASE_PASSWORD = 'ZfSpHvYz'         # Not used with sqlite3.
# DATABASE_HOST = 'external-db.s1797.gridserver.com'             # Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.




#DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'or 
#DATABASE_NAME = 'beautyparlour_oneloudrhours'           # Or path to database file if using sqlite3.
#DATABASE_USER = 'beautyparlour'             # Not used with sqlite3.
#DATABASE_PASSWORD = 'ZfSpHvYz'         # Not used with sqlite3.
#DATABASE_HOST = 'external-db.s1797.gridserver.com'             # Set to empty string for localhost. Not used with 
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.


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






# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Vienna'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/1797/users/.home/domains/media.beautyparlour.at/html/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media.beautyparlour.at/website/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'k+lz-9$&nfi@p#5um(y9i^@*m77vbyz)0f!pmbb9g^v%p)l!cu'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'website.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/home/1797/containers/django/website/templates',
    #'http://media.beautyparlour.at/website/templates',
    '/home/1797/users/.home/domains/media.beautyparlour.at/html/website/templates',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'treemenus',
    'template_utils',
    #'django.contrib.admindocs',
    'website.filebrowser',
    'website.management',
    'website.portfolio',
    'website.countries',
)
