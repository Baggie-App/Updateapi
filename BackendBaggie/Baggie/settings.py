import os
import datetime
#import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&uc+%$q5j0r9b$f81q!0w@zd0ka%38^hx8fq9060%oq^5a%iqu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd-party apps
    'rest_framework',
    'rest_framework.authtoken',
    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount', # new
    #'rest_framework_simplejwt.token_blacklist',
    'drf_yasg', # new
    'django_filters', #new
    'corsheaders',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    'imagekit',

    # Third-party
    #'crispy_forms',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

    #local app
    'users',
    'productsCategory',
    'products',
    'orders',
    'orderDetails',
    'productsImage',
    'cartview',
    'reviewproduct',
    'poll',
    'wishlist',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Baggie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Baggie.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql',
                                                 # 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, 'baggie.db'),  # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# DATABASES = {
# 'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'postgres',
#     'USER': 'postgres',
#     'PASSWORD': 'postgres',
#     'HOST': 'localhost',
#     'PORT': 5432
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME', 'postgres'),
#         'USER': os.environ.get('DB_USER', 'postgres'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'password'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#         'TEST': {
#             'NAME': 'test_db'
#         }
#     },
# }
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30,

    #'EXCEPTION_HANDLER':'utils.exception_handler.custom_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'errors',

    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",

    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ('v1',)
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=24*60),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=30),
}
#password validator
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#some user auth
#ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
#ACCOUNT_AUTHENTICATION_METHOD = 'email'
#ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
AUTH_USER_MODEL = 'users.CustomUser'
# django-crispy-forms
#CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django-allauth config
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT = '/'

SITE_ID = 1


# JWT
# JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

# Email Configurations
#DOMAIN = os.environ.get('DOMAIN', '')
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
# EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '')
# #DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
# ACCOUNT_SESSION_REMEMBER = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER ='muhammad.cse11@gmail.com'
EMAIL_HOST_PASSWORD ='abdullahcse1107'
#'abdullahcse1107' #fvueahgievn
ACCOUNT_SESSION_REMEMBER = True

# CORS WHITELIST
# CORS_ORIGIN_WHITELIST = [
#     #"http://localhost:3000",
#     "https://relaxed-curie-e9a516.netlify.app",
#     "http://127.0.0.1:8000"
# ]
#
# CORS_ORIGIN_REGEX_WHITELIST = [
#     r"^https://\w+\.netlify\.app$",
# ]
CORS_ORIGIN_ALLOW_ALL = True
#CORS_ORIGIN_WHITELIST = (os.environ.get('CORS_WHITELIST').split('/'))



#EMAIL_HOST_USER = os.environ.get('fahimrahman.xyz')
#EMAIL_HOST_PASSWORD = os.environ.get('nVK@7Tr]')


# AUTHENTICATION_BACKENDS = (
#     # 'social_core.backends.facebook.FacebookOAuth2',
#     # 'social_core.backends.github.GithubOAuth2',
#     'social_core.backends.google.GoogleOAuth2',
#     # 'social_core.backends.twitter.TwitterOAuth',
#     'django.contrib.auth.backends.ModelBackend',
#     'account.authentication.EmailAuthBackend',
# )
#
# SOCIAL_AUTH_URL_NAMESPACE = 'social'

# SOCIAL_AUTH_FACEBOOK_KEY = 'XXXXXX'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'XXXXXX'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#     'fields': 'id, name, email'
# }

# SOCIAL_AUTH_GITHUB_KEY = 'XXXXXX'
# SOCIAL_AUTH_GITHUB_SECRET = 'XXXXXX'
# SOCIAL_AUTH_GITHUB_SCOPE = ['email']
# SOCIAL_AUTH_GITHUB_PROFILE_EXTRA_PARAMS = {
#     'fields': 'id, name, email'
# }
#
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '187984114799-c88f3f6vujt8dfmgf77umo4r815im5mj.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'gdjC0b_6cZysnytj7vJlkyiL'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']
# SOCIAL_AUTH_GOOGLE_PROFILE_EXTRA_PARAMS = {
#     'fields': 'id, name, email'
# }
#
# SOCIAL_AUTH_PIPELINE = (
# 'social_core.pipeline.social_auth.social_details',
# 'social_core.pipeline.social_auth.social_uid',
# 'social_core.pipeline.social_auth.auth_allowed',
# 'social_core.pipeline.social_auth.social_user',
# 'social_core.pipeline.user.get_username',
# 'social_core.pipeline.social_auth.associate_by_email',
# 'social_core.pipeline.user.create_user',
# 'social_core.pipeline.social_auth.associate_user',
# 'social_core.pipeline.social_auth.load_extra_data',
# 'social_core.pipeline.user.user_details', )

# SOCIAL_AUTH_TWITTER_KEY = 'XXXXXX'
# SOCIAL_AUTH_TWITTER_SECRET = 'XXXXXX'
# SOCIAL_AUTH_TWITTER_OAUTH2_SCOPE = ['email']
# SOCIAL_AUTH_TWITTER_PROFILE_EXTRA_PARAMS = {
#     'fields': 'id, name, email'
# }
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
# SECURE_SSL_REDIRECT = not DEBUG
