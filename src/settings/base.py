import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 1.8.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# ************************SECURITY SETTINGS************************************


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = bool(os.environ.get('DJANGO_DEBUG'))

#print('****************************** IN DEBUG:', DEBUG)

# Application definition
ROOT_URLCONF = 'src.urls'
WSGI_APPLICATION = 'src.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# directory to place static files on collection action
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_files')

# directories to check for static files
STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, 'src', 'static'),
    os.path.join(BASE_DIR, 'static'),
    #'/var/www/static',

)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_files')


SITE_ID = 1

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/manage/'

ATOMIC_REQUESTS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
                os.path.join(BASE_DIR, 'src', 'templates'),
             ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

    # testing the following
    #'django.middleware.security.SecurityMiddleware'

)

INSTALLED_APPS = (
    # include custom User from accounts app before loading the cms
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    'accounts',

    # OAuth client
    'social_django',

    # add in the django-cms apps
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',

    # include django extensions
    'django_extensions',

    # include polymorphism support
    'polymorphic',

    # admin element sorting extension
    'adminsortable2',

    # easy select 2 (filtered multiselect dropdown field for admin)
    'easy_select2',

    # tagging support
    'taggit',

    # ***************** include app installations
    'src',
    'src.apps.core',
    'src.apps.manage',
    'src.apps.module',
    'src.apps.tags',

)

AUTH_USER_MODEL = 'accounts.User'

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)


MIGRATION_MODULES = {

}

THUMBNAIL_QUALITY = 95
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

THUMBNAIL_SUBDIR = 'thumbnails'

