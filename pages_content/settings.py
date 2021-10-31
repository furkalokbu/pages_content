import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',
    'ckeditor_uploader',
    
    'pages',
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

ROOT_URLCONF = 'pages_content.urls'

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

WSGI_APPLICATION = 'pages_content.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
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

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"


CKEDITOR_CONFIGS = {
    'base': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline', 'TextColor',
             '-', 'Link',
             '-', 'NumberedList', 'BulletedList'
             '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
             '-', 'Smiley',
            ]
        ],
        # 'height': 500,
        # 'width': '100%',
        'toolbarCanCollapse': False,
        'forcePasteAsPlainText': True
    },

    'tgmessage': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link',
             '-', 'Code',
             '-', 'EmojiPanel',
            ]
        ],
        # 'height': 500,
        # 'width': '100%', emoji
         'extraPlugins': ','.join(
            [
                'emoji',
            ]),
        'toolbarCanCollapse': False,
        'forcePasteAsPlainText': True
    },
   'tgcaption': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link',
             '-', 'Code',
             '-', 'EmojiPanel',
            ]
        ],
        'height': 150,
        # 'width': '100%', emoji
        #  'extraPlugins': ','.join(
        #     [
        #         'emoji',
        #     ]),
        'toolbarCanCollapse': False,
        'forcePasteAsPlainText': True
    },
    'default': {
        # 'skin': 'moono',
        'toolbar': 'FreshLime',
        'toolbar_FreshLime': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'SpecialChar', 'PageBreak']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        ],
        'autoGrow_maxHeight': '400',
        'width': "758",
        'height': "350",
        'needsNbspFiller': False,
        'extraPlugins': ','.join(
            [
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'filetools',
                'uploadimage',
                # 'lineheight',
                'richcombo',
            ]),
        # 'filebrowserBrowseUrl': '/ckeditor/browse/',
        # 'filebrowserUploadUrl': '/ckeditor/upload/',
        # 'toolbarCanCollapse': True,
        'allowedContent': True,
        # 'line_height': '1px;2px;3px;4px;5px;6px;7px;8px;9px;10px;11px;12px;13px;14px;15px;16px;17px;18px;19px;20px;21px;22px;23px;24px;25px;26px;27px;28px;29px;30px;31px;32px;33px;34px;35px;36px;37px;38px;39px;40px;41px;42px;43px;44px;45px;46px;47px;48px;49px;50px;51px;52px;53px;54px;55px;56px;57px;58px;59px;60px;61px;62px;63px;64px;65px;66px;67px;68px;69px;70px;71px;72px',
    },
    'front': {
        # 'skin': 'moono',
        'toolbar': 'FreshLime',
        'toolbar_FreshLime': [
            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-',
                'Undo', 'Redo'
            ]},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'insert', 'items': [
                'Image', 'Table', 'HorizontalRule', 'SpecialChar',
            ]}, '/',
            {'name': 'basicstyles', 'items': [
                'Bold', 'Italic', 'Underline', 'Strike', '-',
                'TextColor', 'BGColor', '-',
                'Subscript', 'Superscript', '-',
                'RemoveFormat', '-',
                'NumberedList', 'BulletedList', 'Blockquote', '-',
                'Link', 'Unlink', 'Anchor'
            ]}, '/',
            {'name': 'paragraph', 'items': [
                'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-',
                'BidiLtr', 'BidiRtl', '-', 'Maximize', 'ShowBlocks'
            ]},
            {'name': 'document', 'items': ['Source']},
        ],
        # 'autoGrow_maxHeight': '400',
        'width': "99%",
        'height': "100%",
        'needsNbspFiller': False,
        # 'contentsCss': [
        #     '/static/css/fonts.min.css',
        #     '/static/css/media.min.css',
        #     '/static/css/main.min.css'
        # ],
        'extraPlugins': ','.join(
            [
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'filetools',
                # 'uploadimage',
                # 'lineheight',
                'richcombo',
            ]),
        # 'filebrowserBrowseUrl': '/ckeditor/browse/',
        # 'filebrowserUploadUrl': '/ckeditor/upload/',
        # 'toolbarCanCollapse': True,
        'allowedContent': True,
        # 'line_height': '1px;2px;3px;4px;5px;6px;7px;8px;9px;10px;11px;12px;13px;14px;15px;16px;17px;18px;19px;20px;21px;22px;23px;24px;25px;26px;27px;28px;29px;30px;31px;32px;33px;34px;35px;36px;37px;38px;39px;40px;41px;42px;43px;44px;45px;46px;47px;48px;49px;50px;51px;52px;53px;54px;55px;56px;57px;58px;59px;60px;61px;62px;63px;64px;65px;66px;67px;68px;69px;70px;71px;72px',
    }
}
