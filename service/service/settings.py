"""
Django settings for service project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5#)p)e8)83e2n2bba)+r+3p@v*e@b4=*%**rx31n$jq5nli-um'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'main',
    'clients',
    'services',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}


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

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# import ldap
# from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
#
#
# # Базовая конфигурация.
# AUTH_LDAP_SERVER_URI = 'ldap://ldap.example.com'
#
# AUTH_LDAP_BIND_DN = 'cn=django-agent,dc=example,dc=com'
# AUTH_LDAP_BIND_PASSWORD = 'phlebotinum'
# AUTH_LDAP_USER_SEARCH = LDAPSearch(
#     'ou=users,dc=example,dc=com',
#     ldap.SCOPE_SUBTREE,
#     '(uid=%(user)s)',
# )
# # Or:
# # AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=users,dc=example,dc=com'
#
# # Настройте основные параметры группы.
# AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
#     'ou=django,ou=groups,dc=example,dc=com',
#     ldap.SCOPE_SUBTREE,
#     '(objectClass=groupOfNames)',
# )
# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr='cn')
#
#
# # Простые групповые ограничения
# AUTH_LDAP_REQUIRE_GROUP = 'cn=enabled,ou=django,ou=groups,dc=example,dc=com'
# AUTH_LDAP_DENY_GROUP = 'cn=disabled,ou=django,ou=groups,dc=example,dc=com'
#
# # Заполните пользователя Django из каталога LDAP.
# AUTH_LDAP_USER_ATTR_MAP = {
#     'first_name': 'givenName',
#     'last_name': 'sn',
#     'email': 'mail',
# }
#
# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     'is_active': 'cn=active,ou=django,ou=groups,dc=example,dc=com',
#     'is_staff': 'cn=staff,ou=django,ou=groups,dc=example,dc=com',
#     'is_superuser': 'cn=superuser,ou=django,ou=groups,dc=example,dc=com',
# }
#
# # This is the default, but I like to be explicit.
# AUTH_LDAP_ALWAYS_UPDATE_USER = True
#
# # Используйте членство в группе LDAP для вычисления разрешений группы.
# AUTH_LDAP_FIND_GROUP_PERMS = True
#
# # Кэшируйте отличительные имена и членство в группах в течение часа, чтобы свести к минимуму
# # Трафик LDAP.
# AUTH_LDAP_CACHE_TIMEOUT = 3600
#
# # Keep ModelBackend around for per-user permissions and maybe a local
# # superuser.
# # Список используемых серверных систем аутентификации
# AUTHENTICATION_BACKENDS = [
#     "django_auth_ldap.backend.LDAPBackend"
#
#     # базовый сервер аутентификации, который проверяет базу данных пользователей Django и запрашивает встроенные разрешения.
#     "django.contrib.auth.backends.ModelBackend",
# ]