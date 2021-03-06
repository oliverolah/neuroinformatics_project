from pathlib import Path
import os
import dotenv
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Find .env file to load hidden variables
# dotenv_file = os.path.join(BASE_DIR, '.env')
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.getenv('DEBUG')) == '1' # ('DEBUG', cast=bool)

# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ALLOWED_HOSTS = ['synaptive.azurewebsites.net']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # added apps
    'homeroots',
    'neurons', 
    'theme', # This is for tailwindcss
    'submitdata',
    'contactus',
    'aboutcontent',
    'keysources',
    
    # 3rd party apps
    'tailwind', # Tailwindcss
    'django_extensions', # Django
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'neuroinformaticsProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ 
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'neuroinformaticsProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# from os.environ.get() --> os.getenv()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME_1'),
        'USER': os.getenv('DB_USER_1'),
        'PASSWORD': os.getenv('DB_PASSWORD_1'),
        'HOST': os.getenv('DB_HOST_1'),
        'PORT': os.getenv('DB_PORT_1')
    },
    'neurons_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME_2'),
        'USER': os.getenv('DB_USER_2'),
        'PASSWORD': os.getenv('DB_PASSWORD_2'),
        'HOST': os.getenv('DB_HOST_2'),
        'PORT': os.getenv('DB_PORT_2')
    },
    'submitdata_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME_3'),
        'USER': os.getenv('DB_USER_3'),
        'PASSWORD': os.getenv('DB_PASSWORD_3'),
        'HOST': os.getenv('DB_HOST_3'),
        'PORT': os.getenv('DB_PORT_3')
    },
    'contact_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME_4'),
        'USER': os.getenv('DB_USER_4'),
        'PASSWORD': os.getenv('DB_PASSWORD_4'),
        'HOST': os.getenv('DB_HOST_4'),
        'PORT': os.getenv('DB_PORT_4')
    },
    'keysources_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME_5'),
        'USER': os.getenv('DB_USER_5'),
        'PASSWORD': os.getenv('DB_PASSWORD_5'),
        'HOST': os.getenv('DB_HOST_5'),
        'PORT': os.getenv('DB_PORT_5')
    },
}

DATABASE_ROUTERS = [
    'routers.db_routers.DefaultAdminAuthRouter', 
    'routers.db_routers.NeuronsRouter',
    'routers.db_routers.SubmitDataRouter',
    'routers.db_routers.ContactUsDataRouter',
    'routers.db_routers.KeySourcesDataRouter',
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'theme/static/css/dist',
        'static-files',
]

STATIC_ROOT = BASE_DIR / 'static'

# Tailwind CONFIG
TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# testing email settings  *change in production mode to 3rd party vendor
# in production change from 'console' to 'smtp'
    # from 'django.core.mail.backends.console.EmailBackend'
    # to 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = config('EM_HOST')
# EMAIL_PORT = config('EM_PORT')
# EMAIL_POST_USER = config('ADMIN_EMAIL_USER')
# EMAIL_HOST_PASSWORD = config('ADMIN_EMAIL_PASSWORD')
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False