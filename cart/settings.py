import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ')o-g4bbm7sh%e$jjrn*$v1f)m^-2l8ok!m+(0@2-^+&1s0*dwz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SEND_GRID_API_KEY = ''
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites', # added for allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'stripe',

    'accounts',
    'products',
    'shopping_cart'
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

ROOT_URLCONF = 'cart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'cart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shopping_cart3',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_root'),
]

VENV_PATH = os.path.dirname(BASE_DIR)

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Stripe and Braintree Settings

if DEBUG:
    # test keys
    STRIPE_PUBLISHABLE_KEY = 'pk_test_51GtaWPCDXHsHt8UfcC8UpLekUmqQIrPFp3G3BO7uBiFHcYwtjP63LBCmCCdxgQMBWnWryF9iYcxq5rE3l7mvpkNC00649pICZo'
    STRIPE_SECRET_KEY = 'sk_test_51GtaWPCDXHsHt8Uf41n7I6yegvbR6vq134pt2SQeHyseUWN4NnBzkvUG8Dpn6ka7Ru5Ta06tqfn2eaiIofGCkXEB00fDnCRNf5'
    BT_ENVIRONMENT='sandbox'
    BT_MERCHANT_ID='r6hztr4rvwgmv8w7'
    BT_PUBLIC_KEY='rhgqmxwf6q5g6chk'
    BT_PRIVATE_KEY='1a66b487a11fffd28a50c7e603e5d180'

else:
    # live keys
    STRIPE_PUBLISHABLE_KEY = 'pk_test_51GtaWPCDXHsHt8UfcC8UpLekUmqQIrPFp3G3BO7uBiFHcYwtjP63LBCmCCdxgQMBWnWryF9iYcxq5rE3l7mvpkNC00649pICZo'
    STRIPE_SECRET_KEY = 'sk_test_51GtaWPCDXHsHt8Uf41n7I6yegvbR6vq134pt2SQeHyseUWN4NnBzkvUG8Dpn6ka7Ru5Ta06tqfn2eaiIofGCkXEB00fDnCRNf5'


# Django AllAuth Settings

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

LOGIN_REDIRECT_URL = '/products'
