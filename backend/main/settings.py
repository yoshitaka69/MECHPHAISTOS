from pathlib import Path
import os

# 環境変数で無効にするアプリケーションを指定
disabled_apps = os.getenv('DISABLE_APPS', '').split(',')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-_qv0fxcogfc^1gxjyx)7_3u9b=c&l15$vlv1-^bmk%m&o5oxeq"
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'rest_framework.authtoken',
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
    'test_app',
    'simulation',
]

# INSTALLED_APPSから無効にするアプリを除外
INSTALLED_APPS = [app for app in INSTALLED_APPS if app not in disabled_apps]

if 'audio_recognition' not in disabled_apps:
    INSTALLED_APPS.append('audio_recognition')

if 'ai' not in disabled_apps:
    INSTALLED_APPS.append('ai')

if 'scada' not in disabled_apps:
    INSTALLED_APPS.append('scada')

if 'channels' not in disabled_apps:
    INSTALLED_APPS.append('channels')

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

CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'accounts.CustomUser'

ASGI_APPLICATION = 'main.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


