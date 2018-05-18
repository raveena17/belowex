# Django settings for encyclopedia project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = '/home/linuxuser/Documents/tamilthedal/encyclopedia/thedal.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

import os
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

FILE_NAME = os.path.join(PROJECT_ROOT, "utilities/error") #'/home/nanditha/projects/tamilthedal/trunk/src/encyclopedia/utilities/error'

INDEX_PATH = os.path.join(PROJECT_ROOT, "utilities/index") #'/home/nanditha/projects/tamilthedal/trunk/src/encyclopedia/utilities/index'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'md&bz&=bo_@b6g7$u@*ssi50dkmfvmy)y6g)!o%)vw%5qo@!#7'

# List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.load_template_source',
#     'django.template.loaders.app_directories.load_template_source',
# #     'django.template.loaders.eggs.load_template_source',
# )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'encyclopedia.urls'
LOGIN_URL = '/login/'

# TEMPLATE_DIRS = (
#      '/home/linuxuser/Documents/tamilthedal/encyclopedia/templates'
# )

PAGE_TEMPLATES = (
    ('pages/nice.html', 'nice one'),
    ('pages/cool.html', 'cool one'),
)

PAGE_DEFAULT_TEMPLATE = 'pages/index.html'
#PAGE_LANGUAGES = get_setting('PAGE_LANGUAGES', raise_error=True)


# gettext_noop = lambda s: s

# PAGE_LANGUAGES = (
#     ('zh-cn', gettext_noop('Chinese Simplified')),
#     ('fr-ch', gettext_noop('Swiss french')),
#     ('en-us', gettext_noop('US English')),
# )

# TEMPLATE_DIRS = (
#     os.path.join(PROJECT_ROOT, "templates"),
#     #"/home/linuxuser/Documents/tamilthedal/encyclopedia/templates" 
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    # 'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.sites',
    'encyclopedia.tamilthedal',
    'pages',
)

# Default language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# This is defined here as a do-nothing function because we can't import
# django.utils.translation -- that module depends on the settings.
gettext_noop = lambda s: s

# here is all the languages supported by the CMS
PAGE_LANGUAGES = (
    ('de', gettext_noop('German')),
    ('fr-ch', gettext_noop('Swiss french')),
    ('en-us', gettext_noop('US English')),
)

# copy PAGE_LANGUAGES
languages = list(PAGE_LANGUAGES)

# redefine the LANGUAGES setting in order to be sure to have the correct request.LANGUAGE_CODE
LANGUAGES = languages

# Map every french based language to fr-fr
def language_mapping(lang):
    if lang.startswith('fr'):
        return 'fr-fr'
    return lang
PAGE_LANGUAGE_MAPPING = language_mapping

TEMPLATE_CONTEXT_PROCESSORS = (
    'pages.context_processors.media',
)

# CACHES = {
#     'pages': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

PAGE_USE_SITE_ID = True
SITE_ID = 1

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static"),
]

TEMPLATE_LOADERS = (
    # 'django.template.loaders.filesystem.load_template_source',
    # 'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
            ]
        }
    }
]