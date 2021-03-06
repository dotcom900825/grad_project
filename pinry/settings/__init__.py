# -*- Encoding: utf-8 -*-
import os
from django.contrib.messages import constants as messages
from easy_thumbnails.conf import Settings as thumbnail_settings


SITE_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), '../../')


# Changes the naming on the front-end of the website.
SITE_NAME = '喜拾'
SITE_ID = 1
# Set to False to disable people from creating new accounts.
ALLOW_NEW_REGISTRATIONS = True

# Set to False to force users to login before seeing any pins. 
PUBLIC = True


TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
MEDIA_URL = '/media/'
USER_BIG_PIC_URL = 'user_pic_big'
USER_CROP_PIC_URL = 'user_pic_small'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
STATIC_URL = '/static/'
UPLOAD_DIR = USER_BIG_PIC_URL

DEFAULT_USER_PIC_URL = '/static/vendor/utility/default_user_pic.jpg'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pinry.core.middleware.Public',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "pinry.core.context_processors.template_settings",
)

TEMPLATE_DIRS = (
   "/home/thomas/Desktop/pinry2/pinry/core/templates",
)

COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSMinFilter']
ROOT_URLCONF = 'pinry.urls'
LOGIN_REDIRECT_URL = '/'
INTERNAL_IPS = ['127.0.0.1']
MESSAGE_TAGS = {
    messages.WARNING: 'alert',
    messages.ERROR: 'alert alert-error',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}
API_LIMIT_PER_PAGE = 30


AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',
    'south',
    'compressor',
    'taggit',
    'pinry.vendor',
    'pinry.core',
    'pinry.pins',
    'pinry.api',
    'pinry.renren_oauth',
    'pinry.weibo_oauth',
    'pinry.askPeopleOut',
    'accounts',
    'userena',
    'guardian',
    'easy_thumbnails',
    'userena.contrib.umessages',
    'ajaxuploader',
)


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dotcom900825@gmail.com'
EMAIL_HOST_PASSWORD = '19900825'

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.MyProfile'
LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'


RENREN_APP_API_KEY = "666f30c795b94ed4a29a08659541e4b1"
RENREN_APP_SECRET_KEY = '6a194d095c3a409b8675ca77c6c1aa75'

WEIBO_APP_KEY='1418022286'
WEIBO_APP_SECRET='2eabd2d20f6e8c6bd71f3dad0802a949'
WEIBO_REDIRECT='http://10.108.180.176/login/weibo/confirm'

USERENA_ACTIVATION_REQUIRED = False
USERENA_MUGSHOT_GRAVATAR = False
USERENA_MUGSHOT_DEFAULT = '/static/vendor/utility/default_user_pic.jpg'
USERENA_REDIRECT_ON_SIGNOUT = '/'
USERENA_MUGSHOT_SIZE = 200

SCHOOL_LIST = (
    (u'信息与通信工程学院',u'信息与通信工程学院'),
    )
UNIVERSITY_LIST = (
    (u'北京邮电大学', u'北京邮电大学'),
)


YEAR_IN_SCHOOL_CHOICES = (
    (u'大一', u'大一'),
    (u'大二', u'大二'),
    (u'大三', u'大三'),
    (u'大四', u'大四'),
    (u'研一', u'研一'),
    (u'研二',u'研二'),
    (u'研三',u'研三'),
    (u'博士生',u'博士生'),
)