"""
Django settings for BlogSite project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hbh9nz&*-vc%t=h%dhs2@8r@#rtnog$w25dwbrjrcjnj$r555!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] 


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'Blog',
    'mdeditor'
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

ROOT_URLCONF = 'BlogSite.urls'

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

WSGI_APPLICATION = 'BlogSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
   'default': {
           # 'ENGINE': 'django.db.backends.mysql',
           # 'NAME': BASE_DIR / 'db.sqlite3',
           'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
           'NAME': 'blogsite', #数据库名称
           'USER':'root', # 连接数据库的用户名称
           'PASSWORD':'123456',  # 用户密码
           'HOST':'127.0.0.1', # 访问的数据库的主机的ip地址
           'PORT':'3306', # 默认mysql访问端口
		   'OPTIONS': {'charset': 'utf8mb4'},
       }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
#设置静态文件目录和名称
STATIC_URL = '/static/'
#这个是设置静态文件夹目录的路径
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#设置文件上传路径，图片上传、文件上传都会存放在此目录里
MEDIA_DIR = os.path.join(BASE_DIR,'media')  # 需要加入的MEDIA_DIR路径变量
#MEDIA_ROOT（主要用于告诉服务器去哪里找媒体文件）
MEDIA_ROOT = MEDIA_DIR             # 加入的变量MEDIA_ROOT
#MEDIA_URL （主要用于客户端可通过URL直接访问）
MEDIA_URL = '/media/'   # 此次加入的变量MEDIA_URL