from pathlib import Path
from datetime import timedelta
import os



# Voskのログレベルを設定
os.environ["KALDI_ROOT"] = "log-level=ERROR"

# TensorFlowのログレベルを設定
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-_qv0fxcogfc^1gxjyx)7_3u9b=c&l15$vlv1-^bmk%m&o5oxeq"

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'CRITICAL',  # ログレベルをCRITICALに設定
            'class': 'logging.FileHandler',
            #'class': 'logging.NullHandler',  # NullHandlerを使用してログを無効にする
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'CRITICAL',  # ログレベルをCRITICALに設定
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'CRITICAL',  # ログレベルをCRITICALに設定
            'propagate': True,
        },
        'corsheaders': {
            'handlers': ['file'],
            'level': 'CRITICAL',  # ログレベルをCRITICALに設定
            'propagate': True,
        },
        # VoskのKaldiログレベルを設定
        'vosk': {
            'handlers': ['file'],
            'level': 'CRITICAL',
            'propagate': False,
        },
        'tensorflow': {
            'handlers': ['file'],
            'level': 'CRITICAL',
            'propagate': False,
        },
    },
}




INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'rest_framework.authtoken',
    #'rest_framework_simplejwt',
    'corsheaders',
    'djoser',
    'accounts.apps.AccountsConfig',
    'ceList',
    'spareParts',
    'taskList',
    'nearMiss',
    'sustainability',
    'repairingCost',
    'junctionTable',
    'module',
    'calculation.apps.CalculationConfig',
    'agora',
    'workOrder',
    'benefit',
    'reliability',
    'workingReport',
    'audio_recognition',
    'channels',
    'scada',
    'ai',
]




#JWT_AUTH設定
#SIMPLE_JWT = {
    #'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    #'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # その他の設定...
#}



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:4001",
    "http://127.0.0.1:4001",
    "http://localhost:8001",
    "http://127.0.0.1:8001",
]

CORS_ALLOW_CREDENTIALS = True # 開発中はすべてのオリジンを許可しますが、本番環境ではセキュリティを考慮して設定する必要あり。

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

#INTERNAL_IPS = ['127.0.0.1',]


#Django rest frame work setting
#REST_FRAMEWORK = {
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    #'PAGE_SIZE': 10,
    #'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
   # ),
    #'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.SessionAuthentication',
        #'rest_framework.authentication.BasicAuthentication',
       # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    #),
#}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = 'accounts.CustomUser'


# ASGI Application
ASGI_APPLICATION = 'main.asgi.application'


# Channel Layers
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}