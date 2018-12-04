#encoding:utf-8
"""
Django settings for doc_forum project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k-re$o$-l0#-o6-lsjhm1_hr#v5y%n&0fj8wcwsfs4-haw+e!#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_forms_bootstrap',
    'viewflow.frontend',
    'viewflow',
    'material',
    'material.frontend',
    'crispy_forms',
    'uni_form',
    'bootstrap3_datetime',
    'avatar',
    'doc_forum.manager',
    'doc_forum.proposal',
    'doc_forum.agreement',
    'doc_forum.agreementgesp',
    'doc_forum.doctos',
    'doc_forum.institution',
    'doc_forum.accounts',
    'doc_forum.forum',
    'doc_forum.appointment',
    'doc_forum.fmail',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'doc_forum.urls'

WSGI_APPLICATION = 'doc_forum.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'geo_forum',
        'USER': 'geonode',
        'PASSWORD': 'geonode',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'


USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static_root")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "uploaded")

MEDIA_URL = "/uploaded/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static"),
]

SITE_ID = 1

# gravatar settings
AUTO_GENERATE_AVATAR_SIZES = (20, 32, 80, 100, 140, 200)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT,'templates')
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
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console':{
                'level': 'DEBUG',
                'class': 'logging.StreamHandler'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
                },
            'cities': {
                'handlers': ['console'],
                'level': 'INFO'
            },

            }
    }
CRISPY_TEMPLATE_PACK = 'uni_form'

# Settings for Social Apps
REGISTRATION_OPEN = True
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_APPROVAL_REQUIRED = False

# Email configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rtmgsuport@gmail.com'
EMAIL_HOST_PASSWORD = 'HolaHola'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'rtmg.webmaster@centrogeo.edu.mx'

# Email for users to contact admins.
THEME_ACCOUNT_CONTACT_EMAIL = 'rtmg.webmaster@centrogeo.edu.mx'
