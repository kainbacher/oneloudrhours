# tmp
# Django settings for rkamster project.
import os

SITE_NAME = 'oneloudrhours'

# Das kommt von Django CMS
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
gettext = lambda s: s

DATE_FORMAT = 'd.m.Y'

DATETIME_FORMAT = 'd.m.Y H:i:s'

FIXTURE_DIRS = 'fixtures'

ADMINS = (
    ('Roland Kainbacher', 'rka@beautyparlour.at'),
)

# http://docs.djangoproject.com/en/1.1/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = 'rka@beautyparlour.at'

SERVER_EMAIL = DEFAULT_FROM_EMAIL

MANAGERS = ADMINS

#SEND_BROKEN_LINK_EMAILS = True

POSTGIS_SQL_PATH = '/opt/local/share/postgresql84/contrib/'

TEST_RUNNER='django.contrib.gis.tests.run_tests'

# *************************************************************************************

# Save thumbnail images to a directory directly off MEDIA_ROOT, still
# keeping the relative directory structure of the source image.
# Result: MEDIA_ROOT + 'thumbs/photos/1_jpg_150x150_q85.jpg'
THUMBNAIL_BASEDIR = 'thumbs'

# Save thumbnail images to a sub-directory relative to the source image.
# Result: MEDIA_ROOT + 'photos/_thumbs/1_jpg_150x150_q85.jpg'
#THUMBNAIL_SUBDIR = '_thumbs'

# Prepend thumnail filenames with the specified prefix.
# Result: MEDIA_ROOT + 'photos/__1_jpg_150x150_q85.jpg'
#THUMBNAIL_PREFIX = '__'

#THUMBNAIL_QUALITY = 95

#THUMBNAIL_EXTENSION = 'png'

# *************************************************************************************

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
# TIME_ZONE = 'Europe/Vienna'
# TIME_ZONE = 'utc'
TIME_ZONE = 'Europe/Vienna'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'de-at'
LANGUAGE_CODE = 'en'

WEEK_START_DAY = 1

LANGUAGES = (
#    ('fr', gettext('French')),
#    ('de', gettext('German')),
    ('en', gettext('English')),
)
#CMS_LANGUAGES = (
#    ('de', gettext('German')),
#)


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',

#    'django.template.loaders.app_directories.Loader', # Fuer Sitemaps
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
#    'firepython.middleware.FirePythonDjango',

    'django.middleware.common.CommonMiddleware',
    
    'django.middleware.locale.LocaleMiddleware',    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
#    'cms.middleware.page.CurrentPageMiddleware',
#    'cms.middleware.user.CurrentUserMiddleware',
#    'cms.middleware.media.PlaceholderMediaMiddleware',

#    'cms.middleware.multilingual.MultilingualURLMiddleware',
    
#    'caruso.pagination.middleware.PaginationMiddleware',
#	 'caruso.extlinks.middleware.ExtlinksBlankMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
#    'cms.context_processors.media',
)

ROOT_URLCONF = 'oneloudrhours.urls'

IP_PATH = SITE_ROOT + '/data/'

# CMS_TEMPLATE_INHERITANCE = False

CMS_TEMPLATES = (
#    ('preview.html', gettext('Preview')),
    ('standard.html', gettext('Standard')),
    ('startpage.html', gettext('Startpage')),
    ('dashboard.html', gettext('Dashboard')),
        
#    ('base_copy.html', gettext('base')),
#    (BASE_DIR + 'base.html', gettext('default')),
)

"""
CMS_PLACEHOLDER_CONF = {
        'content': {
                'plugins': ('TextPlugin', 'PicturePlugin', 'LinkPlugin'),
                'extra_context': {"theme":"wide"},
                'name':gettext("Content")
},
}
"""

CMS_APPLICATIONS_URLS = (
    ('master.cmsplugin_news.urls', 'News'),
)

CMS_NAVIGATION_EXTENDERS = (
    ('cmsplugin_news.navigation.get_nodes', 'News'),
)

# http://www.django-cms.org/en/documentation/2.0/configuration/

# CMS_SOFTROOT = True

CMS_REDIRECTS = True

#from django.conf.directives import app

CMS_SEO_FIELDS = True


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
#    'django.contrib.sites',
    'django.contrib.admin',
#    'django.contrib.gis',
    'django.contrib.sitemaps',
#    'django.contrib.comments',

#    'sorl.thumbnail',	
#	 'mptt',
#	 'south',
#    'smart_selects',

    'oneloudrhours.main',

)


AUTH_PROFILE_MODULE = 'accounts.UserProfile'
#AUTH_PROFILE_MODULE = 'myapp.UserProfile'


## registration
ACCOUNT_ACTIVATION_DAYS=7
LOGIN_REDIRECT_URL = '/logincheck/'


from settings_local import *
