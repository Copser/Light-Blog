import os
import sys

from django.conf import settings 



settings.configure(
    DEBUG=True,
    SECRET_KEY = '5y_6z33j1!bk+0+7q3@lbb=bsgh+_ie2^oy6y!(3$30(t=*-t-',
    ROOT_URLCONF ='vegansite.urls',
    MIDDLEWARE_CLASSES=(),   
    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        'django.contrib.webdesign',
        'vegansite',
    ),
    STATIC_URL = '/static/',
    SITE_PAGES_DORECTORY=os.path.join(BASE_DIR, 'pages'),
)       


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
