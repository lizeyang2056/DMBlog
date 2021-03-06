"""
Django settings for DMBlog project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f8yo7dt%r3=b!2o)xfj%b^(otmxk_$%sdk)^$jlnupfg&oavp='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.dmcool.top', '120.79.210.248', '172.18.115.83', '127.0.0.1', '0.0.0.0', 'localhost']
# ALLOWED_HOSTS = "*"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'easy_thumbnails',
    'blog',
    'simditor',
    'mptt',
    'comments',
    'users',

    # The following apps are required:
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.weibo',
]

SITE_ID = 2

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DMBlog.urls'

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

                # `allauth` needs this from django
                'django.template.context_processors.request',

                # 加上微信全局变量
                # 'blog.wx_token.getSignPackage'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'DMBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# fix python manage.py collectstatic error problem
# 当 python manage.py collectstatic 报错时，需查看下列配置是否注释了
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 若存放静态文件的static目录在project目录下，则用该定义
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]

# 图片存放地址
'''
首先在model里定义属性：/%Y/%m/%d分别表示自动创建年月日目录
pic = models.ImageField('图片', upload_to='uploadImages/%Y/%m/%d', default='')
 
修改setting.py
MEDIA_ROOT = 'static/'
MEDIA_URL = '/'
 
数据库对应实体的表中添加pic字段，属性为文本，这个只是用来保存文件路径的
 
上面配置代表的意思大概是：
上传图片到：web程序目录/static/uploadImages/%Y/%m/%d/
访问路径为：http://hostname/static/uploadImages/%Y/%m/%d/filename.jpg
 
基本就是这样，大家可以试一下，很方便，页面调用为modelobjname.pic.url

另外：前端访问的时候需要在前面加上'/static/'例如<img src="/static/{{ post.pic }}">
'''
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# django-simditor配置
# 在settings.py文件中配置相关markdown设置，让我们的富文本编辑器支持markdown
# 在settings.py文件中配置相关markdown设置，让我们的富文本编辑器支持markdown
SIMDITOR_UPLOAD_PATH = 'simditor_uploads/'
SIMDITOR_IMAGE_BACKEND = 'pillow'

SIMDITOR_TOOLBAR = [
    'title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale',
    'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link',
    'image', 'hr', '|', 'indent', 'outdent', 'alignment', 'fullscreen',
    'markdown'
]

SIMDITOR_CONFIGS = {
    'toolbar': SIMDITOR_TOOLBAR,
    'upload': {
        'url': '/simditor/upload/',
        'fileKey': 'upload'
    }
}

# django haystack配置 详情请到 https://www.zmrenwu.com/post/45/ 查看教程
# django haystack 使用的搜索引擎，这里我们使用了 blog.whoosh_cn_backend.WhooshEngine，
# 虽然目前这个引擎还不存在，但我们接下来会创建它。PATH 指定了索引文件需要存放的位置，
# 我们设置为项目根目录 BASE_DIR 下的 whoosh_index 文件夹（在建立索引是会自动创建）。
# *********************************************************************************************** #
# 重点在于如果最后 python manage.py rebuild_index 指令报错可以尝试 python manage.py update_index  #
# *********************************************************************************************** #
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 指定如何对搜索结果分页，这里设置为每 10 项结果为一页。
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 8
# 指定什么时候更新索引，这里我们使用 haystack.signals.RealtimeSignalProcessor，
# 作用是每当有文章更新时就更新索引。由于博客文章更新不会太频繁，因此实时更新没有问题
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# easy_thumbanils Django图片压缩配置
THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (240, 148), 'crop': True},
    },
}

# 其它设置...
AUTH_USER_MODEL = 'users.User'

# 登陆重定向、注销重定向
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'

# 发送邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.mxhichina.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 465
EMAIL_HOST_USER = ''  # 帐号
EMAIL_HOST_PASSWORD = ''  # 密码
DEFAULT_FROM_EMAIL = 'DMBlog <dm_master@dmcool.top>'

# allauth 配置
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_REQUIRED = False

LOGIN_URL = '/accounts/login'
